import pyodbc
from core.config import SQL_SERVER, SQL_DATABASE, SQL_USERNAME, SQL_PASSWORD

def connect_sql():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"UID={SQL_USERNAME};"
            f"PWD={SQL_PASSWORD}"
        )
        return conn
    except Exception as e:
        raise ConnectionError(f"SQL 連線失敗: {e}")
