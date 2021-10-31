# example authentication implementation in Python

"""
Python SDK is recommended as it has already implemented the authentication process for every API:
"""

import time
import hashlib
import hmac
import requests
import json

def gen_sign(method, url, query_string=None, payload_string=None):
    key = ''        # api_key
    secret = ''     # api_secret

    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}

if __name__ == "__main__":
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    common_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/futures/orders'
    body = {"contract": "BTC_USD", "size": 100, "price": "30", "tif": "gtc"}
    request_content = json.dumps(body)
    sign_headers = gen_sign('POST', prefix + url, "", request_content)
    sign_headers.update(common_headers)
    print('signature headers: %s' % sign_headers)
    res = requests.post(host + prefix + url, headers=sign_headers, data=request_content)
    print(res.status_code)
    print(res.content)