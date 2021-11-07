import requests
from environs import Env

env = Env()
env.read_env()

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + env('BOT_TOKEN') + '/sendMessage?chat_id=' + env('BOT_SEND_TO') + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def telegram_bot_sendtextwhenhavenothing(bot_message, send_to):
    send_text = 'https://api.telegram.org/bot' + env('BOT_TOKEN') + '/sendMessage?chat_id=' + send_to + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()