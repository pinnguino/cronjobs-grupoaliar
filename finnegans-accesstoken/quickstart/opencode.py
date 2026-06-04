import json
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDENTIALS_FILE = "google_credentials_local.json"
TOKEN_FILE = "token.json"

creds = None

# Si ya existe token.json, lo cargamos
if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "r") as f:
        creds = google.oauth2.credentials.Credentials.from_authorized_user_info(
            json.load(f), SCOPES
        )

# Si no hay credenciales válidas, corremos el flujo OAuth
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)

    # Guardamos el token (incluye refresh_token)
    with open(TOKEN_FILE, "w") as f:
        f.write(creds.to_json())

print("✅ Autorización completada. token.json guardado.")