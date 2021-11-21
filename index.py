import time
import logging
import datetime
from sender.prepare_mes import preparation_before_sending
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname) 2s-%(asctime) 4s: %(message)s',
    handlers=[logging.FileHandler("logs/news.log", mode='a+'), stream_handler]
)

if __name__ == '__main__':
    try:
        logging.info('Starting bot {}'.format(datetime.datetime.now()))
        while True:
            preparation_before_sending('huobi_listing')            
            time.sleep(10)
    except Exception as err: 
        logging.error('Error {}:, {}'.format(datetime.datetime.now(), str(err)))
    except KeyboardInterrupt as error:
        logging.info('Exit by user {}'.format(datetime.datetime.now()))