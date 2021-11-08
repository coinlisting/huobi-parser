import requests
from environs import Env

env = Env()
env.read_env()

def telegram_bot_sendtext(bot_message):
    token = env('BOT_TOKEN')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {
        'chat_id': env('BOT_SEND_TO_TEST'),
        'parse_mode': 'Markdown',
        'text': bot_message
    }
    response = requests.get(url, params=params)
    return response.json()

def telegram_bot_sendtextwhenhavenothing(bot_message, send_to):
    token = env('BOT_TOKEN')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    params = {
        'chat_id': env('BOT_SEND_TO_TEST'),
        'parse_mode': 'Markdown',
        'text': bot_message
    }
    response = requests.get(url, params=params)
    return response.json()

