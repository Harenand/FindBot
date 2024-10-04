import time
from bs4 import BeautifulSoup
import requests
import urllib.parse # библика для декодирования ссылки
from requests.adapters import HTTPAdapter #чтобы как то сессии и время ожидания к сайту настроить хззз
from urllib3.util.retry import Retry
import csv
import numpy as np
import asyncio
import aiohttp
from aiohttp import ClientTimeout
from bs4 import BeautifulSoup
import csv
import urllib.parse
import time
import pandas as pd

# Асинхронная функция для поиска на DuckDuckGo
async def duckduckgo_search(query):
    url = f'https://html.duckduckgo.com/html/?t=h_&q={query}&ia=web'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            r = await response.text()
            soup = BeautifulSoup(r, 'lxml')
            a_tags = soup.find_all('a', class_='result__snippet')
            results = []
            for a_tag in a_tags:
                link = a_tag.get('href')
                if 'uddg=' in link:
                    query_params = urllib.parse.parse_qs(urllib.parse.urlparse(link).query)
                    if 'uddg' in query_params:
                        decoded_link = query_params['uddg'][0]
                        results.append(decoded_link)
            return results


# Асинхронная функция для поиска текста по ссылкам
async def text_search(result_links):
    results = []

    async with aiohttp.ClientSession(timeout=ClientTimeout(total=10)) as session:
        tasks = []
        for url in result_links:
            tasks.append(fetch_text(session, url))

        # Запускаем все задачи одновременно
        results_text = await asyncio.gather(*tasks)

        # Собираем результаты в список
        for result in results_text:
            if result:
                results.extend(result)

    return results


# Вспомогательная функция для загрузки текста страницы
async def fetch_text(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                r = await response.text()
                soup = BeautifulSoup(r, 'lxml')
                get_text_br = [item.get_text(strip=True) for item in soup.find_all('br')]
                get_text_p = [item.get_text(strip=True) for item in soup.find_all('p')]
                return get_text_br + get_text_p
            else:
                print(f"Ошибка: Статус ответа {response.status} для {url}")
                return []
    except Exception as e:
        print(f"Ошибка при доступе к {url}: {e}")
        return []


# Главная функция для запуска асинхронных задач
async def main():
    query = input('Введите запрос: ')
    result_list = await duckduckgo_search(query)
    result_text = await text_search(result_list)




    # Объединение двух массивов в один
    combined_data = list(zip(result_list, result_text))
    # Сохраняем данные в CSV-файл
    # Объединение данных (предполагается, что combined_data уже существует)
    head = ['link','p']
    df = pd.DataFrame(combined_data, columns=head)

    # Указываем путь и имя файла
    file_path = r'D:\рабочий стол\project_bot\data.csv'

    # Сохраняем в CSV с правильной кодировкой и разделителем
    df.to_csv(file_path, sep=';', encoding='utf-8-sig', index=False)

    print(len(combined_data))
# Запуск программы
if __name__ == '__main__':
    asyncio.run(main())
