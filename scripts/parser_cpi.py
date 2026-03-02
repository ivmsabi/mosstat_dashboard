import os
import requests
import pandas as pd

URL = "https://77.rosstat.gov.ru/storage/mediabank/Динамика%20индекса%20потребительских%20цен%20на%20товары%20и%20услуги%20в%202000-2026%20гг..xlsx"
RAW_PATH = "data/raw/cpi.xlsx"
PROCESSED_PATH = "data/processed/cpi_cleaned.csv"

def download_file():
    os.makedirs("data/raw", exist_ok=True)
    r = requests.get(URL, verify=False)  # отключаем проверку SSL
    r.raise_for_status()
    with open(RAW_PATH, "wb") as f:
        f.write(r.content)
    print("Файл скачан")

def preprocess():
    os.makedirs("data/processed", exist_ok=True)
    df = pd.read_excel(RAW_PATH, skiprows=3)
    df = df.rename(columns={df.columns[0]: "month"})
    df = df.dropna(subset=["month"])
    df = df.melt(id_vars=["month"], var_name="year", value_name="value")
    df = df.dropna(subset=["value"])
    df["value"] = df["value"].astype
    
    URL = "https://77.rosstat.gov.ru/storage/mediabank/Динамика%20индекса%20потребительских%20цен%20на%20товары%20и%20услуги%20в%202000-2026%20гг..xlsx"

r = requests.get(URL, verify=False)
r.raise_for_status()

with open("cpi.xlsx", "wb") as f:
    f.write(r.content)

print("Файл скачан")