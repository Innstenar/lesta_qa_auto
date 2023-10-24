import requests
from bs4 import BeautifulSoup
import re
from dataclasses import dataclass

# Отправляем GET-запрос на URL сайта
url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
response = requests.get(url)

# Используем BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Найдем таблицу с данными
table = soup.find('table', {'class': 'wikitable'})

# Создадим датакласс для хранения данных из таблицы
@dataclass
class TableData:
    website: str
    popularity: str
    frontend: str
    backend: str
    database: str
    notes: str

table_data_list = []

# Функция для удаления квадратных скобок и их содержимого
def remove_square_brackets(text):
    return re.sub(r'\[.*?\]', '', text)

# Итерируемся по строкам таблицы
for row in table.find_all('tr')[1:]:  # Пропускаем заголовок
    columns = row.find_all('td')
    if len(columns) == 0:
        continue  # Пропустим строки заголовка и другие пустые строки

    website = remove_square_brackets(columns[0].get_text(strip=True))
    popularity = remove_square_brackets(columns[1].get_text(strip=True))
    frontend = remove_square_brackets(columns[2].get_text(strip=True))
    backend = remove_square_brackets(columns[3].get_text(strip=True))
    database = remove_square_brackets(columns[4].get_text(strip=True))
    notes = remove_square_brackets(columns[5].get_text(strip=True))

    # Создадим экземпляр датакласса и добавим его в список
    table_data = TableData(website, popularity, frontend, backend, database, notes)
    table_data_list.append(table_data)

# Пример вывода данных в терминале
for data in table_data_list:
    print(f"Website: {data.website}")
    print(f"Popularity: {data.popularity}")
    print(f"Frontend: {data.frontend}")
    print(f"Backend: {data.backend}")
    print(f"Database: {data.database}")
    print(f"Notes: {data.notes}")
    print()
