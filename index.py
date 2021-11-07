import time
import math
import datetime
import json
from checker.scrapper import get_last_anouncement, get_last_news
from sender.send_message import telegram_bot_sendtext
from gateioapi.reqs import get_specific_currency, list_spot_account, spot_candlesticks, calculate, create_order, check_single_order
from database.store_file import reading_file, writing_file


if __name__ == '__main__':
    last_message = ''
    last_news_mes = ''
    binance = 'https://www.binance.com'
    while True:
        last_announcement = get_last_anouncement()
        message = ''.join(last_announcement['TEXT'] + ' ' + binance + last_announcement['LINK'])
        #message = ''.join('Binance Adds ALGO/RUB, AUD/USDC, LAZIO/BUSD, LUNA/BIDR, MANA/TRY, OXT/BUSD & SHIB/UAH Trading Pairs').replace('&', "and")
         
        if last_message == last_announcement['TEXT']:               # сверка с последней новостью, чтоб не спамил
            last_news = get_last_news()
            news = ''.join(last_news['TEXT']  +  binance + last_news['LINK'])
            last_news_mes = reading_file('./database/last_news.json')
            if last_news_mes == last_news['TEXT']:
                print('Новых новостей нет, ' + str(datetime.datetime.now())) 
            else:
                telegram_bot_sendtext(news)
            writing_file('./database/last_news.json', last_news['TEXT'])              # запись файл для сравнения
            #last_news_mes = last_news['TEXT']
            time.sleep(2)
        else:
            if last_announcement['JUST_NEWS'] == False:             # если это не просто новость, т.е. анонс монеты новой, которую можно купить
                length = len(last_announcement['NAME'])             # смотрим количество монет заанонсированных
                for i in range(0, length):                          # проходимся по всем
                    have_coin = get_specific_currency(last_announcement['NAME'][i][1:-1])           # ищем монету i
                    if have_coin:                                                                   # если монета есть
                        prev_pr, cur_pr = spot_candlesticks(last_announcement['NAME'][i][1:-1], '1m')   # смотрим свечи по ней, берем текущую и предыдущую цену
                        wallet_available = list_spot_account()
                        bolean_buy = calculate(prev_pr, cur_pr)
                        if float(wallet_available) > 1:
                            available_sum = float(wallet_available/(length-i))          #* 0.10      # доступная сумма (10%)
                            count = available_sum/(float(cur_pr)+(float(cur_pr)*0.1))
                            new_order = create_order(last_announcement['NAME'][i][1:-1], 'buy', math.floor(count), (float(cur_pr)+(float(cur_pr)*0.1)))
                            time.sleep(0.25)
                            currency_price = float(cur_pr)+(float(cur_pr)*0.01)
                            # selling 
                            if new_order['status'] == 'closed':
                                new_sell_order = create_order(last_announcement['NAME'][i][1:-1], 'sell', (math.floor(count)*100/101), currency_price + currency_price * 0.99)
                            else:
                                status = 'open'
                                for i in range(100):
                                    if status == 'open':
                                        status = check_single_order(new_order['id'])
                                        time.sleep(0.25)
                                    else:
                                        break
                                new_sell_order = create_order(last_announcement['NAME'][i][1:-1], 'sell', (math.floor(count)*100/101), currency_price+currency_price * 0.8)    
                telegram_bot_sendtext(message)
            else:
                telegram_bot_sendtext(message)
            last_message = last_announcement['TEXT']