from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.cloud import storage
from apimanager.settings import gcs_client
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import logging
import pandas as pd
import yaml
import datetime
import urllib.parse

logger = logging.getLogger(__name__)

current_date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

@method_decorator(csrf_exempt, name='dispatch')
class GCSFileListView(APIView):

    def get(self, request):
        bucket_name = 'cpixi-test-suites'
        try:
            bucket = gcs_client.get_bucket(bucket_name)
            logger.info(f"Bucket name: {bucket_name}")
            
            folder_structure = self.list_folder_structure(bucket)
            logger.info(f"Folder structure: {folder_structure}")
            formatted_structure = self.format_folder_structure(folder_structure)
            logger.info(f"Response: {formatted_structure}")

            print(f"Folder structure: {folder_structure}")  # Example of using print
            print(f"Response: {formatted_structure}")  # Example of using print

            return Response(formatted_structure, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error retrieving folder structure: {str(e)}")
            print(f"Error retrieving folder structure: {str(e)}")  # Example of using print
            error_message = {'error': str(e)}
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list_folder_structure(self, bucket):
        blobs = bucket.list_blobs()
        root = {}

        for blob in blobs:
            path = blob.name.split('/')
            current = root

            for folder_name in path[:-1]:
                if folder_name not in current:
                    current[folder_name] = {}
                current = current[folder_name]

            if not blob.name.endswith('/'):
                filename = path[-1]
                if 'files' not in current:
                    current['files'] = []
                current['files'].append(filename)

        return root

    def format_folder_structure(self, structure):
        def convert_to_list_format(structure):
            result = []
            for key, value in structure.items():
                item = {'name': key, 'label': key}
                if 'files' in value:
                    item['children'] = [{'label': file} for file in value['files']]
                if isinstance(value, dict):
                    if 'files' in value:
                        item['children'] = [{'label': file} for file in value['files']]
                    else:
                        item['children'] = convert_to_list_format(value)
                result.append(item)
            return result

        return convert_to_list_format(structure)

    def post(self, request):
        bucket_name = 'cpixi-test-suites'
        try:
            bucket = gcs_client.get_bucket(bucket_name)

            file_obj = request.FILES['file']
            file_name = request.data.get('file_name') or file_obj.name
            folder_path = request.data.get('folder_path', '')

            if folder_path:
                blob = bucket.blob(folder_path + '/' + file_name)
            else:
                blob = bucket.blob(file_name)

            blob.upload_from_file(file_obj)

            response_data = {
                'message': f'File {file_name} added to {folder_path}',
                'file_url': f'https://storage.googleapis.com/{bucket_name}/{blob.name}'
            }

            logger.info(f"File {file_name} uploaded successfully to {folder_path}")
            print(f"File {file_name} uploaded successfully to {folder_path}")  # Example of using print
            return Response(response_data, status=status.HTTP_201_CREATED)

        except KeyError:
            logger.error("File not found in request")
            print("File not found in request")  # Example of using print
            error_message = {'error': 'File not found in request'}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Error uploading file: {str(e)}")
            print(f"Error uploading file: {str(e)}")  # Example of using print
            error_message = {'error': str(e)}
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        bucket_name = 'cpixi-test-suites'
        try:
            bucket = gcs_client.get_bucket(bucket_name)

            file_name = request.data['file_name']
            folder_path = request.data.get('folder_path', '')
            new_content = request.data['content']

            blob = bucket.blob(folder_path + '/' + file_name)
            blob.upload_from_string(new_content)

            response_data = {
                'message': f'File {file_name} in {folder_path} updated successfully',
                'file_url': f'https://storage.googleapis.com/{bucket_name}/{blob.name}'
            }

            logger.info(f"File {file_name} updated successfully in {folder_path}")
            print(f"File {file_name} updated successfully in {folder_path}")  # Example of using print
            return Response(response_data, status=status.HTTP_200_OK)

        except KeyError:
            logger.error("Missing required parameters")
            print("Missing required parameters")  # Example of using print
            error_message = {'error': 'Missing required parameters'}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Error updating file: {str(e)}")
            print(f"Error updating file: {str(e)}")  # Example of using print
            error_message = {'error': str(e)}
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        bucket_name = 'cpixi-test-suites'
        try:
            bucket = gcs_client.get_bucket(bucket_name)

            file_path = request.data.get('file_path')

            if not file_path:
                logger.error("File path is required")
                print("File path is required")  # Example of using print
                error_message = {'error': 'File path is required'}
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

            blob = bucket.blob(file_path)
            blob.delete()

            response_data = {
                'message': f'File or folder {file_path} deleted successfully'
            }

            logger.info(f"File or folder {file_path} deleted successfully")
            print(f"File or folder {file_path} deleted successfully")  # Example of using print
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Error deleting file or folder: {str(e)}")
            print(f"Error deleting file or folder: {str(e)}")  # Example of using print
            error_message = {'error': str(e)}
            return Response(error_message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
