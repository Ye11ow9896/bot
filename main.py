import requests
from bs4 import BeautifulSoup
import nums_from_string
from db import SQLiteDB
from datetime import datetime
import time

text = None
# Проверяем еслть ли текущая дата в БД
cur_date = str(datetime.now())
cur_date = cur_date.split()
cur_date = cur_date[0]
db = SQLiteDB() 
last_date = db.get_last_id()
# Если есть - обновляем цену и записываем ее в БД
if last_date[0][3] != cur_date:
    url = 'https://aliexpress.ru/item/1005003577312703.html?spm=a2g2w.productlist.search_results.0.79524aa6maM2Ft&sku_id=12000026945335517' # url страницы
    while(text is None):
        r = requests.get(url)
        with open('test.html', 'w', encoding='utf-8') as output_file:
            output_file.write(r.text)
        with open("test.html", "r", encoding='utf-8') as f:
            contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        text = soup.find('div', class_="snow-price_SnowPrice__mainS__18x8np")
        if text is None:
            time.sleep(3700)
    nums = nums_from_string.get_nums(text.text)
    price = (nums[0] * 1000) + (nums[1]) + (nums[2] / 100)
    SQLiteDB().insert_varible_into_table('Orangepi 3LTS', price, cur_date, url)




