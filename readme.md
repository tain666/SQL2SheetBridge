# SQL2SheetBridge

一鍵將 **MS SQL Server 資料表** 匯入至 **Google Sheets** 的自動化工具。

---

## 功能特色

- 匯入多張 SQL Server 資料表  
- 自動寫入 Google Sheets 指定工作表與欄位  
- 支援 Service Account 憑證與 `.env` 環境設定  
- 整合日誌記錄功能，方便除錯與追蹤  
- 可打包為 `.exe` 提供同事使用  
- 內建 GUI 執行介面，點選即可執行  

---

## 介面
 
> 勾選資料表 → 按「開始匯入」→ 自動推送資料到 Google Sheets

---
    
## 專案結構

```plaintext
SQL2SheetBridge/
├── .env               # 環境設定檔
├── .gitattributes     # 設定 LF 執行
├── .gitignore         # 忽略憑證、快取等敏感檔案
├── LICENSE            # 授權條款（私有）
├── README.md          # 專案說明文件
├── build.bat          # PyInstaller 打包腳本
├── requirements.txt   # 依賴套件清單
├── SQL2SheetBridge.py # 程式主進入點
├── credentials/       # Google Sheets API 憑證（請勿公開）
└── core/              # 程式邏輯模組
    ├── config.py      # 參數設定
    ├── database.py    # SQL 查詢邏輯
    ├── queries.py     # SQL 語句定義
    ├── sheets.py      # Google Sheets 寫入邏輯
    └── ui.py          # GUI 執行介面
```

---

## 使用方式

### 1. 編輯 `.env`

```
SQL_SERVER=你的資料庫IP或名稱
SQL_DATABASE=資料庫名稱
SQL_USERNAME=帳號
SQL_PASSWORD=密碼
GOOGLE_CREDENTIAL_JSON=credentials/xxx.json
```

### 2. 準備憑證

將 Google Sheets API 的服務帳號 JSON 放入 `credentials/` 資料夾

### 3. 執行程式

```bash
python SQL2SheetBridge.py
```

### 4. 修改查詢語句

根據實際資料庫結構，調整 `core/queries.py` 中的 SQL

---

## License

This project is proprietary and confidential.  
Unauthorized use, reproduction, or distribution is strictly prohibited.  
© 2025 tain666. All rights reserved.

---

## 作者

Maintained by [tain666](https://github.com/tain666)  
如有建議、錯誤回報或需求，請聯繫我：  
📧 s86951103@gmail.com
