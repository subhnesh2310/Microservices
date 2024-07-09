import requests
from google.oauth2.service_account import Credentials
from google.cloud import bigquery

# Vault server URL and path to your secret
vault_url = "http://10.100.112.125:8200"
secret_path = "v1/cpixi-storage/v1-secret"
role_id = "29ba25e9-fcfe-a378-e44b-1a7232c35bee"
secret_id = "ae6cfb91-501d-25d0-8e96-519d19f24c14"

def vault_authenticate(vault_url, role_id, secret_id):
    auth_url = f"{vault_url}/v1/auth/approle/login" # auth with approle
    data = {"role_id": role_id, "secret_id": secret_id}
    response = requests.post(auth_url, json=data)
    print(response)
    if not response.ok:
        raise Exception(f"Authentication failed: {response.text}")
    return response.json()['auth']['client_token']

def get_gcp_credentials(vault_url, secret_path, vault_token):
    headers = {"X-Vault-Token": vault_token}
    secret_url = f"{vault_url}/{secret_path}"
    response = requests.get(secret_url, headers=headers).json()
    if 'errors' in response and response['errors']:
        raise Exception(f"Error from Vault: {response['errors']}")
    
    credentials = response.get('data', {}).get('credentials')
    if not credentials:
        raise Exception("GCP credentials not found in secret data.")

    return credentials

vault_token = vault_authenticate(vault_url, role_id, secret_id)
gcp_credentials_json = get_gcp_credentials(vault_url, secret_path, vault_token)
print (gcp_credentials_json)