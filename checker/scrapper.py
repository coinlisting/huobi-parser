# Глобальные пакеты
from hashlib import new
import requests
import time
import json
import sys
import re
import itertools

sys.path.append('..')
from bs4 import BeautifulSoup
from environs import Env

# Локальные пакеты
from sender.send_message import telegram_bot_sendtext
from sender.tgchatsid import groups
from database.store_file import writing_file
# Это для получения конфигов 
env = Env()
env.read_env()

# Стандартная уришка
url = 'https://www.binance.com'


# Отправляет запрос в указанный линк и возвращает структуру страницы
def get_page(link):
    response = requests.get(url+link)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

# Возвращает последний анонсированный токен
def get_last_anouncement():
    new_listing_page = '/en/support/announcement/c-48'      # стандартная страница только анонсированных токенов
    just_news = False
    soup = get_page(new_listing_page)                       # отправляем запрос, получаем структуру страницы
    last_record = soup.find_all('a', id='link-0-0-p1')      # ищем нужный на тэг с нужной айдишкой
    rec_text = last_record[0].text.replace('&', "and")      # определяем содержимый текст
    coin = {'JUST_NEWS': False}
    coin['TEXT'] = rec_text
    coin['LINK'] = last_record[0]['href']                   # 
    exclusions = ['Futures', 'Margin', 'adds']              # а это исключающие слова, нужны они для того, чтобы не лопатить все ненужные нам в листинге статьи
    for item in exclusions:                                 # проходимся по исключениям
        if item in rec_text:                                # если исключающее слово есть в содержимом тексте тега, то возвращаем NONE
            coin['JUST_NEWS'] = True
        if 'Will List' not in rec_text:                     # и если в содержимом тексте тега отсутствиет слова, то тоже возвращаем NONE
            coin['JUST_NEWS'] = True
    if coin['JUST_NEWS'] == True:
        return coin
    else:        
        coin['NAME'] = re.findall(r'\(.*?\)', rec_text)
        return coin

def get_last_news():
    new_listing_page = '/en/support/announcement/c-49?navId=49'      # стандартная страница только анонсированных токенов
    soup = get_page(new_listing_page)                                # отправляем запрос, получаем структуру страницы
    last_record = soup.find_all('a', id='link-0-0-p1')               # ищем нужный на тэг с нужной айдишкой
    rec_text = last_record[0].text.replace('&', "and") 
    news = {'TEXT': rec_text, 'LINK': last_record[0]['href']}
    return news

def get_activities():
    new_listing_page = '/en/support/announcement/c-93?navId=93'      # стандартная страница только анонсированных токенов
    soup = get_page(new_listing_page)                                # отправляем запрос, получаем структуру страницы
    last_record = soup.find_all('a', id='link-0-0-p1')               # ищем нужный на тэг с нужной айдишкой
    rec_text = last_record[0].text.replace('&', "and") 
    activities = {'TEXT': rec_text, 'LINK': last_record[0]['href']}
    return activities


