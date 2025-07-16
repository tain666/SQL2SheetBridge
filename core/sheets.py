import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from core.config import GOOGLE_CREDENTIAL_JSON, SHEET_NAME

def connect_sheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds_path = os.path.join("credentials", GOOGLE_CREDENTIAL_JSON)
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        return gspread.authorize(creds)
    except Exception as e:
        raise ConnectionError(f"Sheets 認證失敗: {e}")

def write_sheet(client, name: str, df: pd.DataFrame):
    try:
        sheet = client.open(SHEET_NAME).worksheet(name)
        sheet.clear()
        sheet.update("A1", [df.columns.tolist()] + df.values.tolist())
    except Exception as e:
        raise RuntimeError(f"寫入 {name} 失敗: {e}")
