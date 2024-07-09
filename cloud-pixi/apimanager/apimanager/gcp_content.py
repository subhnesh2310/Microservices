import urllib.parse
import logging
import json
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.cloud import storage
from google.cloud.exceptions import GoogleCloudError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from apimanager.settings import gcs_client
import yaml  # Import PyYAML for YAML processing

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class FileContentView(APIView):
    
    def get(self, request):
        try:
            # import ipdb; ipdb.set_trace()
            file_label = request.query_params.get('label')
            
            if not file_label:
                return Response({'error': 'File label not provided'}, status=status.HTTP_400_BAD_REQUEST)

            parsed_label = urllib.parse.unquote(file_label)
            parsed_url = urllib.parse.urlparse(parsed_label)
            path_components = parsed_url.path.split('/')
            
            if not path_components:
                return Response({'error': 'Invalid file label provided'}, status=status.HTTP_400_BAD_REQUEST)

            file_name = path_components[-1]
            file_extension = file_name.split('.')[-1].lower()

            if file_extension == 'xlsx':
                return self.process_excel_file(parsed_url.path)
            elif file_extension in ['yml', 'yaml']:
                return self.process_yaml_file(parsed_url.path)
            else:
                return Response({'error': 'Unsupported file format'}, status=status.HTTP_400_BAD_REQUEST)

        except GoogleCloudError as gce:
            logger.error(f"Google Cloud Storage error: {str(gce)}")
            return Response({'error': f"Google Cloud Storage error: {str(gce)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return Response({'error': f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def process_excel_file(self, file_path):
        try:
            bucket_name = 'cpixi-test-suites'
            bucket = gcs_client.get_bucket(bucket_name)
            blob = bucket.blob(file_path)

            if not blob.exists():
                return Response({'error': f'File {file_path} not found in GCS'}, status=status.HTTP_404_NOT_FOUND)

            file_bytes = blob.download_as_bytes()
            df = pd.read_excel(file_bytes, engine='openpyxl')

            # Filter out rows that are in comment format (if applicable)
            df = self.filter_comment_rows(df)

            data = df.to_json(orient='records')

            logger.info(f"Loaded Excel file: \n {df}")
            print(f"Loaded Excel file: \n {df}")
            return Response(data, status=status.HTTP_200_OK)

        except pd.errors.ParserError as pe:
            logger.error(f"Error parsing Excel file: {str(pe)}")
            return Response({'error': f"Error parsing Excel file: {str(pe)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error processing Excel file: {str(e)}")
            return Response({'error': f"Error processing Excel file: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def filter_comment_rows(self, df):
        # Assuming your comment format is marked in some specific way, e.g., rows starting with '#'
        return df[~df.apply(lambda row: row.astype(str).str.startswith('#')).any(axis=1)]

    
    def process_yaml_file(self, file_path):
        try:
            bucket_name = 'cpixi-test-suites'
            bucket = gcs_client.get_bucket(bucket_name)
            blob = bucket.blob(file_path)

            if not blob.exists():
                return Response({'error': f'File {file_path} not found in GCS'}, status=status.HTTP_404_NOT_FOUND)

            file_bytes = blob.download_as_bytes()
            content = yaml.safe_load(file_bytes)
            data = json.dumps(content)

            logger.info(f"Loaded YAML file: \n {data}")
            print(f"Loaded YAML file: \n {data}")
            return Response(data, status=status.HTTP_200_OK)

        except yaml.YAMLError as ye:
            logger.error(f"Error parsing YAML file: {str(ye)}")
            return Response({'error': f"Error parsing YAML file: {str(ye)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error processing YAML file: {str(e)}")
            return Response({'error': f"Error processing YAML file: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
