import os
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from logger import get_logger

log = get_logger(__name__)

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDENTIALS_FILE = os.path.join("google_credentials_local.json")
TOKEN_FILE = os.path.join("google_refresh_token.json")

credentials = None

if os.path.exists(TOKEN_FILE):
    log.info("Loading existing token from %s", TOKEN_FILE)
    try:
        with open(TOKEN_FILE, "r") as token_file:
            credentials = Credentials.from_authorized_user_info(
                json.load(token_file), SCOPES
            )
        log.info("Existing token loaded successfully")
    except (json.JSONDecodeError, IOError) as e:
        log.error("Failed to load token from %s: %s", TOKEN_FILE, e)
        raise

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        log.info("Token expired, refreshing...")
        try:
            credentials.refresh(Request())
            log.info("Token refreshed successfully")
        except Exception as e:
            log.error("Failed to refresh token: %s", e)
            raise
    else:
        log.info("No valid token found, starting OAuth flow...")
        try:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
            log.info("OAuth flow completed, new credentials obtained")
        except Exception as e:
            log.error("OAuth flow failed: %s", e)
            raise

    log.info("Saving new token to %s", TOKEN_FILE)
    try:
        with open(TOKEN_FILE, "w") as token_file:
            token_file.write(credentials.to_json())
        log.info("Token saved successfully")
    except IOError as e:
        log.error("Failed to save token to %s: %s", TOKEN_FILE, e)
        raise