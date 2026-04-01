import requests
import os

url = "https://77.rosstat.gov.ru/storage/mediabank/Динамика%20индекса%20потребительских%20цен%20на%20товары%20и%20услуги%20в%202000-2026%20гг..xlsx"
print(f"Скачивание: {url}")

try:
    response = requests.get(url, verify=False, timeout=30)
    print(f"Статус: {response.status_code}")
    print(f"Размер: {len(response.content)} bytes")
    
    if len(response.content) > 10000:
        os.makedirs("data/raw", exist_ok=True)
        with open("data/raw/test_cpi.xlsx", "wb") as f:
            f.write(response.content)
        print("✅ Файл сохранен")
    else:
        print("⚠️ Файл слишком маленький")
except Exception as e:
    print(f"❌ Ошибка: {e}")
