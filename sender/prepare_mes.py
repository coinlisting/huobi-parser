import datetime
import logging
from checker.scrapper import get_page_content
from database.store_file import reading_file, writing_file
from sender.send_message import telegram_bot_sendtext

parent_links = {
                'crypto_listing': "/en/support/announcement/c-48?navId=48",
                'last_news': "/en/support/announcement/c-49?navId=49",
                'activities': '/en/support/announcement/c-93?navId=93'
                }

def preparation_before_sending(parent):
    binance_url = 'https://www.binance.com'
    url = parent_links[parent]
    content = get_page_content(url)
    content['PARENT'] = parent

    if 'Will List' not in content['TEXT']:
        news = content['TEXT'] +' ' + binance_url + content['LINK']
        last_news_mes = reading_file('./database/' + content['PARENT'] + '.json')

        #проверяет есть ли похожие новости
        if last_news_mes['TEXT'] != content['TEXT']:
            telegram_bot_sendtext(news)
            logging.info("Новая новость: " + content['LINK'])
        writing_file('./database/' + content['PARENT'] + '.json', content)  
    