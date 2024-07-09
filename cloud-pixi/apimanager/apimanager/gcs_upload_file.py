from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.cloud import storage
from apimanager.settings import gcs_client
import os
import logging

logger = logging.getLogger(__name__)

class GCSFileUploadWithStructureView(APIView):

    def post(self, request):
        try:
            # Get the GCS bucket
            bucket_name = 'cpixi-test-suites'
            # import ipdb; ipdb.set_trace()
            bucket = gcs_client.get_bucket(bucket_name)

            # Get folder structure and file(s) from request
            folder_structure = request.data.get('folder_structure', '')
            files = request.FILES.getlist('files')

            if not files:
                # If no files were uploaded (empty list), treat it as an error
                return Response({'error': 'No files uploaded.'}, status=status.HTTP_400_BAD_REQUEST)

            uploaded_files = []

            for file_obj in files:
                file_name = file_obj.name
                file_path = folder_structure + file_name  # Concatenate folder structure and file name
                blob = bucket.blob(file_path)

                # Upload file to GCS
                blob.upload_from_file(file_obj)

                # Log and collect uploaded file info
                uploaded_files.append({
                    'file_name': file_name,
                    'file_path': file_path,
                    'file_url': f'https://storage.googleapis.com/{bucket_name}/{blob.name}'
                })

            # Return success response with uploaded files info
            return Response({'message': 'Files uploaded successfully.', 'uploaded_files': uploaded_files}, status=status.HTTP_201_CREATED)

        except Exception as e:
            logger.error(f"Error uploading files to GCS: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
