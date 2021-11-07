# example authentication implementation in Python

"""
Python SDK is recommended as it has already implemented the authentication process for every API:
"""

import time
import hashlib
import hmac
from environs import Env

env = Env()
env.read_env()

def gen_sign(method, url, query_string=None, payload_string=None):
    key = env('GATEIO_API_KEY')        # api_key
    secret = env('GATEIO_SECRET_KEY')     # api_secret

    t = time.time()
    m = hashlib.sha512()
    m.update((payload_string or "").encode('utf-8'))
    hashed_payload = m.hexdigest()
    s = '%s\n%s\n%s\n%s\n%s' % (method, url, query_string or "", hashed_payload, t)
    sign = hmac.new(secret.encode('utf-8'), s.encode('utf-8'), hashlib.sha512).hexdigest()
    return {'KEY': key, 'Timestamp': str(t), 'SIGN': sign}