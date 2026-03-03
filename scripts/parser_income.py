import pandas as pd
import requests
import os

URL = "https://77.rosstat.gov.ru/storage/mediabank/Динамика%20денежных%20доходов%20населения%20г.%20Москвы%20за%202014-2024%20гг.(2).xlsx"
# Скачиваем файл
r = requests.get(URL, verify=False)
r.raise_for_status()
with open("income.xlsx", "wb") as f:
    f.write(r.content)
print("Файл скачан")
