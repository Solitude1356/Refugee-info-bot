import configparser
import json
from sheetsApi import sheet_values

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id = 27947853
api_hash = '831c49c38b291d15e7dba077a22c0451'
username = 'refugee-bot-data-picking'

client = TelegramClient(username, api_id, api_hash)
client.start()

def check_and_get(url):
    if url.find('t.me/') != -1:
        id_index = url.rfind('/')
        id = url[id_index + 1:]
        url = url[:id_index]
        channel = client.get_entity(url) #t.me/infouaitalia/10)
        tg_message = client.get_messages(channel, ids=id)
        print(tg_message)
        return tg_message

# def get_text_msg(channel, id):
#     tg_message = client.get_messages(channel, ids=id)
#     return tg_message
    
# print(get_text_msg(channel, 96))