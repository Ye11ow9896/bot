import telebot 
from telebot import types 
import requests
from bs4 import BeautifulSoup
import nums_from_string
from db import SQLiteDB
from datetime import datetime

cur_date = str(datetime.now())
cur_date = cur_date.split()
cur_date = cur_date[0]
bot = telebot.TeleBot('5857308703:AAHQlDfKPnEU_CuhdTk_DgFC5ZDnNbU8V8k')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	# клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	but1 = types.KeyboardButton("Stats")
	but2 = types.KeyboardButton("Update stats")
	markup.add(but1, but2)

	bot.reply_to(message, "Hello, {0.first_name}\nPress button".format(message.from_user)
  ,parse_mode='html',reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "Stats":
        db = SQLiteDB() 
        last_date = db.get_last_id()
        table = db.get_database_table('database.sqlite')
        for i in range (len(table)):
            bot.send_message(message.chat.id, str(table[i][3]) + ' - ' + str(table[i][2]))

    elif message.text == "Update stats":
        db = SQLiteDB() 
        last_date = db.get_last_id()
        table = db.get_database_table('database.sqlite')
        if last_date[0][3] != cur_date:
            r = requests.get('https://aliexpress.ru/item/1005003577312703.html?spm=a2g2w.productlist.search_results.0.79524aa6maM2Ft&sku_id=12000026945335517')
            with open('test.html', 'w', encoding='utf-8') as output_file:
                output_file.write(r.text)
            with open("test.html", "r", encoding='utf-8') as f:
                contents = f.read()
            soup = BeautifulSoup(contents, 'html.parser')
            text = soup.find('div', class_="snow-price_SnowPrice__mainS__18x8np")
            if text is None:
                bot.send_message(message.chat.id, "Алиэкспресс требует ввести ебучую капчу, попробуй попозже обновить")
            else:
                nums = nums_from_string.get_nums(text.text)
                price = (nums[0] * 1000) + (nums[1]) + (nums[2] / 100)
                SQLiteDB().insert_varible_into_table('Orangepi 3LTS', price, cur_date, 'https://aliexpress.ru/item/1005003577312703.html?spm=a2g2w.productlist.search_results.0.79524aa6maM2Ft&sku_id=12000026945335517')
        else:
            bot.send_message(message.chat.id, "Данные за этот день уже есть, обнови завтра, чурка")

bot.polling(none_stop=True, interval=0)
