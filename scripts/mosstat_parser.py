import requests
import os

def download_file(url, save_path):
    """
    Функция скачивает файл по URL и сохраняет в указанное место
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Файл сохранён: {save_path}")
    else:
        print(f"Ошибка при скачивании файла: {url}")

# -------------------------------
# 1.1 Динамика индекса потребительских цен
download_file(
    "https://77.rosstat.gov.ru/folder/64640/yourfile.xlsx",
    "data/consumer_price_index.xlsx"
)

# 1.2 Динамика денежных доходов населения Москвы
download_file(
    "https://77.rosstat.gov.ru/storage/mediabank/Динамика%20денежных%20доходов%20населения%20г.%20Москвы%20за%202014-2024%20гг.(2).xlsx"
)

# 1.3 Доля населения с доходами ниже прожиточного минимума
download_file(
    "https://77.rosstat.gov.ru/folder/64641/yourfile.xlsx",
    "data/poverty_rate.xlsx"
)

# 1.4 Заболеваемость населения по основным классам болезней
download_file(
    "https://77.rosstat.gov.ru/folder/64643/yourfile.xlsx",
    "data/morbidity.xlsx"
)

# 1.5 Численность медицинских кадров
download_file(
    "https://77.rosstat.gov.ru/folder/64643/yourfile.xlsx",
    "data/medical_staff.xlsx"
)
