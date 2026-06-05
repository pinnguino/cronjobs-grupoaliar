import os

from dotenv import load_dotenv
import requests
import gspread
from google_auth import credentials
from logger import get_logger

log = get_logger(__name__)

load_dotenv()

sheet_id = os.getenv("GOOGLE_SHEET_ID")
sheet_name = os.getenv("GOOGLE_SHEET_NAME")
sheet_cell = os.getenv("GOOGLE_SHEET_CELL")

log.info("Requesting Finnegans access token...")
finnegans_url = os.getenv("FINNEGANS_BASE_URL")
query_params = {
    "grant_type": "client_credentials",
    "client_id": os.getenv("FINNEGANS_CLIENT_ID"),
    "client_secret": os.getenv("FINNEGANS_CLIENT_SECRET")
}

try:
    response = requests.get(finnegans_url + "/oauth/token", params=query_params)
    response.raise_for_status()
    access_token = response.text.strip() # Finnegans access token
    log.info("Access token obtained successfully. Saving to Google Sheets...")

    gspread_client = gspread.authorize(credentials) # Usa las credenciales obtenidas para autorizar el cliente de gspread
    sheet = gspread_client.open_by_key(sheet_id).worksheet(sheet_name) # Abre la hoja de cálculo por ID y selecciona la hoja por nombre
    sheet.update_acell(sheet_cell, access_token) # Actualiza la celda especificada con el token de acceso obtenido

    log.info("Access token saved to Google Sheets.")

except requests.exceptions.RequestException as e:
    log.error("Failed to obtain Finnegans access token: %s", e)
    raise
except (KeyError, ValueError) as e:
    log.error("Unexpected response format: %s", e)
    raise
except Exception as e:
    log.error("Failed to save token to Google Sheets: %s", e)
    raise