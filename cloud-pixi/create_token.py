import requests
from google.oauth2.service_account import Credentials
from google.cloud import bigquery

# Vault server URL and path to your secret
vault_url = ""
secret_path = ""
role_id = ""
secret_id = ""

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
