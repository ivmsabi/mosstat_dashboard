import os
import requests
import pandas as pd
# --- Пути для хранения ---
RAW_PATH = "data/raw/health_diseases.xlsx"
PROCESSED_PATH = "data/processed/health_diseases_cleaned.csv"
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# --- Скачивание файла с Мосстата ---
URL = "https://77.rosstat.gov.ru/storage/mediabank/Заболеваемость%20населения%20по%20основным%20классам%20болезней%20в%202020-2024%20гг(1).xlsx"
r = requests.get(URL, verify=False)  # отключаем проверку SSL
r.raise_for_status()
with open(RAW_PATH, "wb") as f:
    f.write(r.content)
print("Файл скачан")