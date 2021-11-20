# Глобальные пакеты
from hashlib import new
import requests
import sys

sys.path.append('..')
from bs4 import BeautifulSoup
from environs import Env
# Это для получения конфигов 
env = Env()
env.read_env()
# Стандартная уришка

# Отправляет запрос в указанный линк и возвращает структуру страницы
def get_page():
    search = '마켓 디지털 자산'
    url = f'https://api-manager.upbit.com/api/v1/notices/search?'
    params = {
        'search': search,
        'page': '1',
        'per_page': '1',
        'before': '',
        'target': 'non_ios',
        'thread_name': 'general'
    }
    response = requests.get(url, params=params)
    return response.json()

def get_page_content():
    '''Возвращаем страницу которую парсим'''
    soup = get_page()                                            # отправляем запрос, получаем структуру страницы
    last_record = soup['data']['list'][0]                        # ищем нужный на тэг с нужной айдишкой
    rec_text = last_record['title']
    rec_link = str(last_record['id'])
    content = {'TEXT': rec_text, 'LINK': rec_link}
    return content


