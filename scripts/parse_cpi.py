import requests
from bs4 import BeautifulSoup
import re
import urllib3
from pathlib import Path

# Отключаем предупреждения SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Создаём папку для данных
data_dir = Path("data/raw/cpi")
data_dir.mkdir(parents=True, exist_ok=True)

url = 'https://77.rosstat.gov.ru/folder/64640'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

print(f"Загружаем страницу: {url}")
# Отключаем проверку SSL
r = requests.get(url, headers=headers, verify=False)

soup = BeautifulSoup(r.text, 'html.parser')
print('Найдены ссылки на Excel файлы:')

# Сохраняем список ссылок
links_found = []

for link in soup.find_all('a', href=True):
    href = link['href']
    text = link.get_text().strip()
    if re.search(r'\.xlsx?$', href, re.I):
        if href.startswith('http'):
            full_url = href
        else:
            full_url = f'https://77.rosstat.gov.ru{href}'
        
        print(f'📄 {text[:50]:50} -> {full_url}')
        links_found.append({'text': text, 'url': full_url})

# Сохраняем ссылки в файл
with open('cpi_links.txt', 'w') as f:
    for link in links_found:
        f.write(f"{link['text']}\t{link['url']}\n")

print(f"\nНайдено ссылок: {len(links_found)}")
print("Ссылки сохранены в cpi_links.txt")

# Скачиваем первые 2 файла для теста
for i, link in enumerate(links_found[:2]):
    print(f"\nСкачиваем {i+1}: {link['text']}")
    try:
        file_response = requests.get(link['url'], verify=False)
        filename = f"cpi_test_{i+1}.xlsx"
        filepath = data_dir / filename
        with open(filepath, 'wb') as f:
            f.write(file_response.content)
        print(f"✅ Сохранено: {filepath}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
