# coding: utf-8
import requests
import time
import hashlib
import hmac


from gtio_auth import gen_sign

host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

# 
def get_specific_currency(name):
    url = '/spot/currencies/{}'.format(name)
    query_param = ''
    r = requests.request('GET', host + prefix + url, headers=headers)
    print(r.json())


def get_a_single_order(order_id, currency_pair):
    url = '/spot/orders/{}'.format(order_id)
    query_param = 'currency_pair={}'.format(currency_pair)
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen_sign('GET', prefix + url, query_param)
    headers.update(sign_headers)
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    print(r.json())


def create_order(cur_sh, oper_name, amount, price):
    url = '/spot/orders/'
    query_param = ''
    body = '{"text": "t-123456", "currency_pair": "{}_USDT", "type": "limit", "account":"spot", "side": "{}", "iceberg": "0", "amount": "{}", "price": "{}"}'.format(cur_sh, oper_name, amount, price)
    sign_headers = gen_sign('POST', prefix + url, query_param, body)
    headers.update(sign_headers)
    r = requests.request('POST', host + prefix + url, headers=headers, data=body)
    print(r.json())