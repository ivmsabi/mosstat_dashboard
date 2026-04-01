import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# --- Пути для хранения ---
RAW_PATH = "data/raw/medical_staff.xlsx"
PROCESSED_PATH = "data/processed/medical_staff_cleaned.csv"
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# --- Скачивание файла ---
URL = "https://77.rosstat.gov.ru/storage/mediabank/%D0%A7%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C%20%D0%BC%D0%B5%D0%B4%D0%B8%D1%86%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D1%85%20%D0%BA%D0%B0%D0%B4%D1%80%D0%BE%D0%B2%20%D0%B7%D0%B0%202020-2024%20%D0%B3%D0%B3(1).xlsx"  # вставьте реальный URL с Мосстата
r = requests.get(URL, verify=False)
r.raise_for_status()
with open(RAW_PATH, "wb") as f:
    f.write(r.content)
print("Файл скачан")