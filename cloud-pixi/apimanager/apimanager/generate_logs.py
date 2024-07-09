import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LogFileView(APIView):
    api_directory = os.path.dirname(__file__)
    logs_folder_name = 'pixie_logger'
    logs_folder_path = os.path.abspath(os.path.join(api_directory, '..', logs_folder_name))

    def ensure_logs_folder_exists(self):
        try:
            if not os.path.exists(self.logs_folder_path):
                os.makedirs(self.logs_folder_path)
        except OSError as e:
            return False, f"Failed to create directory: {self.logs_folder_path}. Error: {str(e)}"
        return True, None

    def get_latest_log_file(self):
        success, error_message = self.ensure_logs_folder_exists()
        if not success:
            return None, error_message
        # Get a list of all files in the logs folder
        try:
            files = os.listdir(self.logs_folder_path)
        except OSError as e:
            return None, f"Failed to list files in directory: {self.logs_folder_path}. Error: {str(e)}"
        
        # Filter out directories and get modification times of files
        files_with_mtime = [(file, os.path.getmtime(os.path.join(self.logs_folder_path, file))) 
                            for file in files if os.path.isfile(os.path.join(self.logs_folder_path, file))]
        
        # Select the file with the most recent modification time
        latest_file = max(files_with_mtime, key=lambda x: x[1])[0] if files_with_mtime else None
        
        return latest_file, None

    def get(self, request):
        latest_file, error_message = self.get_latest_log_file()
        
        if error_message:
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if latest_file:
            try:
                # import ipdb; ipdb.set_trace()
                with open(os.path.join(self.logs_folder_path, latest_file), 'r') as log_file:
                    logs = log_file.readlines()
                
                if logs:  # Check if logs list is not empty
                    # Print logs directly in the terminal
                    for log in logs:
                        print(log.strip())
                    return Response(logs)
                else:
                    return Response({'message': 'Empty logs'})
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'No log files found'}, status=status.HTTP_404_NOT_FOUND)
