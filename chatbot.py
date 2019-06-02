import sys
import chatbotmodel
import telegram
from pymongo import MongoClient

#database setting
client = MongoClient('localhost',27017)
db = client.dbsparta
melon_ticket = db.melon_ticket.find() #indexing from database

baekcloud_token = '733519455:AAFn6_CUmVo2GCYz6Y9sl3JpuoZoJ_U2PWo'
baekcloud = telegram.Bot(token = baekcloud_token)
updates = baekcloud.getUpdates()

def firecracker():
    return 'ㅇㅅㅇ'

def proc_rolling(bot, update):
    msg = db.melon_ticket.find_one()
    baekcloud.sendMessage(msg['title'])
    sound = firecracker()
    baekcloud.sendMessage(sound)
    baekcloud.sendMessage('르르..')

def proc_stop(bot, update):
    baekcloud.sendMessage('Bye Bye My Blue')
    baekcloud.stop()


baekcloud= chatbotmodel.baekcloud_bot()
baekcloud.add_handler('rolling', proc_rolling)
baekcloud.add_handler('stop', proc_stop)
baekcloud.start()

