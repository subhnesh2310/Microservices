import requests
import os

url = 'http://127.0.0.1:8000/api/upload_with_structure/'

# Define the exact folder structure as a string
folder_structure = '8653f628-b28e-5fa5-961d-d4e649df8bba/g30/cli/c1cada39-4c9f-528b-88bd-bd2e203224ae/'

file_name = 'G32_PROVISIONING_DUAL_SERVICE_CLI_0010.xlsx'

# Get the directory path of the current script
directory_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory_path, file_name)

files = []
try:
    with open(file_path, 'rb') as f:
        files.append(('files', (file_name, f.read())))
except FileNotFoundError:
    print(f"File '{file_name}' not found at '{file_path}'")
    exit(1)
except Exception as e:
    print(f"Error opening file '{file_name}': {e}")
    exit(1)

try:
    response = requests.post(url, data={'folder_structure': folder_structure}, files=files)
    print("Response status:", response.status_code)
    print("Response content:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
