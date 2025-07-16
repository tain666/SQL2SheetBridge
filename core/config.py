import os
from dotenv import load_dotenv

load_dotenv()

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
GOOGLE_CREDENTIAL_JSON = os.getenv("GOOGLE_CREDENTIAL_JSON")
SHEET_NAME = "品號供需明細表"
