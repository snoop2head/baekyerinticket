import sys
import chatbotmodel
import telegram
from pymongo import MongoClient

#database setting
client = MongoClient('localhost',27017)
db = client.dbsparta
melon_ticket = db.melon_ticket.find() #indexing from database
dbaccess = db.melon_ticket.find_one()

baekcloud_token = '733519455:AAFn6_CUmVo2GCYz6Y9sl3JpuoZoJ_U2PWo'
baekcloud = telegram.Bot(token = baekcloud_token)
updates = baekcloud.getUpdates()

def firecracker():
    return ''

def proc_ticket(bot, update):
    message = str(dbaccess['title']) + "\n" + str(dbaccess['url'])
    baekcloud.sendMessage(message)
    sound = firecracker()
    baekcloud.sendMessage(sound)

def proc_stop(bot, update):
    baekcloud.sendMessage('Bye Bye My Blue')
    baekcloud.stop()


baekcloud= chatbotmodel.baekcloud_bot()
baekcloud.add_handler('ticket', proc_ticket)
baekcloud.add_handler('stop', proc_stop)
baekcloud.start()

