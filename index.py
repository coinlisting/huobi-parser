import time
import logging
import datetime
from sender.prepare_mes import preparation_before_sending
logging.basicConfig(filename='./logs/news.log', level=logging.INFO, format='%(levelname) 2s-%(asctime) 4s:%(message)s')

if __name__ == '__main__':
    try:
        logging.info('Starting bot {}'.format(datetime.datetime.now()))
        while True:
            preparation_before_sending('crypto_listing')            #https://www.binance.com/en/support/announcement/c-48?navId=48
            preparation_before_sending('last_news')                 #https://www.binance.com/en/support/announcement/c-49?navId=49
            preparation_before_sending('activities')                #https://www.binance.com/en/support/announcement/c-93?navId=93
            time.sleep(1)
    except Exception as err: 
        logging.error('Error {}:, {}'.format(datetime.datetime.now(), str(err)))
    except KeyboardInterrupt as error:
        logging.info('Exit by user {}'.format(datetime.datetime.now()))