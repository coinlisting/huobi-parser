# Глобальные пакеты
from hashlib import new
import requests
import sys
import re

sys.path.append('..')
from bs4 import BeautifulSoup
from environs import Env
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

def get_page_content(url):
    '''Возвращаем страницу которую парсим'''
    soup = get_page(url)                                            # отправляем запрос, получаем структуру страницы
    last_record = soup.find_all('a', id='link-0-0-p1')               # ищем нужный на тэг с нужной айдишкой
    rec_text = last_record[0].text
    content = {'TEXT': rec_text, 'LINK': last_record[0]['href']}
    return content


