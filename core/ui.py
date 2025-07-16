import customtkinter as ctk
import pandas as pd
from core.database import connect_sql
from core.sheets import connect_sheet, write_sheet
from core.queries import queries

def launch_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("GGSMIDA - SQL 資料上傳工具")
    app.geometry("700x640")
    app.minsize(650, 600)

    title_label = ctk.CTkLabel(app, text="📊 GGSMIDA SQL → Google Sheets", font=("Microsoft JhengHei", 22, "bold"))
    title_label.pack(pady=12)

    main_card = ctk.CTkFrame(app, corner_radius=15)
    main_card.pack(padx=20, pady=10, fill="both", expand=True)

    checkbox_title = ctk.CTkLabel(main_card, text="✅ 請選擇要上傳的資料表", font=("Microsoft JhengHei", 16))
    checkbox_title.pack(pady=(15, 5))

    sheet_vars = {}
    sheet_list = list(queries.keys())

    checkbox_frame = ctk.CTkFrame(main_card, fg_color="transparent")
    checkbox_frame.pack(pady=5)

    for i, sheet in enumerate(sheet_list):
        var = ctk.BooleanVar()
        cb = ctk.CTkCheckBox(checkbox_frame, text=sheet, variable=var)
        cb.grid(row=i // 2, column=i % 2, padx=10, pady=5, sticky="w")
        sheet_vars[sheet] = var

    log_label = ctk.CTkLabel(main_card, text="🪵 執行紀錄", font=("Microsoft JhengHei", 16))
    log_label.pack(pady=(15, 0))

    logbox = ctk.CTkTextbox(main_card, height=200, corner_radius=10, wrap="word")
    logbox.pack(padx=20, pady=(5, 10), fill="both", expand=False)

    progress_bar = ctk.CTkProgressBar(app, width=580)
    progress_bar.set(0)
    progress_bar.pack(pady=(5, 10))

    def log(msg):
        logbox.insert("end", msg + "\n")
        logbox.see("end")

    def run_import():
        selected = [s for s, v in sheet_vars.items() if v.get()]
        if not selected:
            log("⚠️ 請至少選擇一個工作表")
            return

        progress_bar.set(0)
        total = len(selected)
        step = 1 / total if total > 0 else 1

        try:
            conn = connect_sql()
            log("✅ SQL Server 已連線")
        except Exception as e:
            log(str(e))
            return

        try:
            gclient = connect_sheet()
            log("✅ Google Sheets 已連線")
        except Exception as e:
            log(str(e))
            conn.close()
            return

        for i, sheet in enumerate(selected, 1):
            try:
                df = pd.read_sql(queries[sheet], conn)
                write_sheet(gclient, sheet, df)
                log(f"📤 寫入 {sheet} 共 {len(df)} 筆")
            except Exception as e:
                log(f"❌ 匯入 {sheet} 失敗: {e}")
            progress_bar.set(i * step)

        conn.close()
        log("🎉 所有資料表處理完成！")

    btn = ctk.CTkButton(app, text="🚀 開始匯入", font=("Microsoft JhengHei", 15), command=run_import)
    btn.pack(pady=10)

    app.mainloop()
