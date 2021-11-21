import datetime
import logging
import re
from checker.scrapper import get_page_content
from database.store_file import reading_file, writing_file
from sender.send_message import telegram_bot_sendtext

parent_links = {
                'huobi_listing': "/support/en-us/detail/"
                }
def preparation_before_sending(parent):
    huobi = 'https://www.huobi.com/support/en-us/detail/'
    content = get_page_content()
    content['PARENT'] = parent
    logging.info('Start {}:, {}'.format(datetime.datetime.now(), str(parent)))
    news = content['TEXT'] + ' ' + huobi + content['LINK']
    last_news_mes = reading_file('./database/files/' + content['PARENT'] + '.json')
        
    #проверяет есть ли похожие новости
    if last_news_mes['TEXT'] != content['TEXT']:
        telegram_bot_sendtext(str(news))
        logging.info("New News: " + content['LINK'] + ' ' + format(datetime.datetime.now()))
    writing_file('./database/files/' + content['PARENT']+ '.json', content)  
    logging.info('End {}:, {}'.format(datetime.datetime.now(), str(parent)))