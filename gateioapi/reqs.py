# coding: utf-8
import requests
import time
import hashlib
import hmac
import json



from gateioapi.gtio_auth import gen_sign

host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}


# 
def get_specific_currency(name):
    url = '/spot/currencies/{}'.format(name)
    r = requests.request('GET', host + prefix + url, headers=headers)
    if len(r.json()) < 4:
        if r.json()['label'] == 'INVALID_CURRENCY':
            print(r.json())
            return False
    else:
        return True


# def get_a_single_order(order_id, currency_pair):
#     url = '/spot/orders/{}'.format(order_id)
#     query_param = 'currency_pair={}'.format(currency_pair)
#     # for `gen_sign` implementation, refer to section `Authentication` above
#     sign_headers = gen_sign('GET', prefix + url, query_param)
#     headers.update(sign_headers)
#     r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
#     print(r.json())


# def currency_pairs(coin):
#     # url = '/spot/currency_pairs/{}_USDT'
#     # query_param='{}_USDT'.format(coin)
#     # r = requests.request('GET', host + prefix + url, headers=headers)
#     # print(r.json())
#     url = '/spot/currency_pairs'
#     query_param = ''
#     r = requests.request('GET', host + prefix + url, headers=headers)
#     print(r.json())    


# def retrieve_market_trades(coin):
#     url = '/spot/trades'
#     query_param = 'currency_pair={}_USDT'.format(coin)
#     r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
#     print(r.json())
#     return r.json()


def check_single_order(order_id, cur_short):
    url = '/spot/orders/12345'
    query_param = 'currency_pair={}_USDT'.format(cur_short)
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    # r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    # print(r.json())
    # return r.json()['status']




def create_order(cur_short, oper_name, amount, price):
    print(price)
    url = '/spot/orders'
    query_param = ''
    q = {
        "currency_pair":"{}_USDT".format(cur_short),
        "type":"limit",
        "account":"spot",
        "side":"{}".format(oper_name),
        "amount":"{}".format(amount),
        "price":"{}".format(price)
    }
    body = json.dumps(q)
    print(body)
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())
    return r.json()

def list_spot_account():
    url = '/spot/accounts'
    query_param = ''
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url, headers=headers)
    usdt_ac = [item for item in r.json() if item.get('currency') == 'USDT']
    print('usdt_ac: ', usdt_ac)
    if usdt_ac[0]['locked'] == 1:
        return 'locked=True'
    else:
        return usdt_ac[0]['available']
    


def spot_candlesticks(coin, interval):
    url = '/spot/candlesticks'
    query_param = 'currency_pair={}_USDT&interval={}'.format(coin, interval)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    prev_price = r.json()[len(r.json())-2:-1][0]
    current_price = r.json()[len(r.json())-1:][0]
    return prev_price[2:3][0], current_price[3:4][0]


def calculate(prev_price, cur_price):
    print(prev_price)
    prev_price = float(prev_price) + float(prev_price) * 0.55
    print(cur_price)
    if float(cur_price) <= prev_price:
        print('покупаем')
        return True
    else:
        print('Не покупаем')
        return False