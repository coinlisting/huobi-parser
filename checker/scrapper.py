# Глобальные пакеты
from hashlib import new
import requests
import sys
import datetime
import logging
from proxy.init import proxy_list

from urllib.parse import urlparse

sys.path.append('..')
from bs4 import BeautifulSoup
from environs import Env
# Это для получения конфигов 
env = Env()
env.read_env()
proxy_list
# Стандартная уришка
url = 'https://medium.com'
#	https://medium.com/@erbolbaysalov

# Отправляет запрос в указанный линк и возвращает структуру страницы
def get_page(link):
    logging.info('Starting  get_page {}:, {}'.format(datetime.datetime.now(), str(link)))
    response = requests.get(url+link, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')
    logging.info('End get_page {}:, {}'.format(datetime.datetime.now(), str(link)))
    return soup

def get_page_content(url):
    '''Возвращаем страницу которую парсим'''
    soup = get_page(url)                                            # отправляем запрос, получаем структуру страницы
    last_record = soup.select('h1.hw a')                            # ищем нужный на тэг с нужной айдишкой
    rec_text = last_record[0].text
    link = urlparse(last_record[0]['href'])._replace(query=None).geturl(); 
    content = {'TEXT': rec_text, 'LINK': link}
    return content


