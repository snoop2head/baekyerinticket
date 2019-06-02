import sys
import chatbotmodel
import telegram
from pymongo import MongoClient
import pprint

#database setting
client = MongoClient('localhost',27017)
db = client.dbsparta
melon_ticket = db.melon_ticket.find() #indexing from database
dbaccess_an_item = db.melon_ticket.find_one()
dbaccess_multiple_item = db.melon_ticket.find({})

#token settings
baekcloud_token = '733519455:AAFn6_CUmVo2GCYz6Y9sl3JpuoZoJ_U2PWo'
baekcloud = telegram.Bot(token = baekcloud_token)
updates = baekcloud.getUpdates()


def proc_ticket(bot, update):
    for object in db.melon_ticket.find():
        message = str(object['title']) + "\n" + str(object['url'])
        #print(message)
        baekcloud.sendMessage(message)

def proc_stop(bot, update):
    baekcloud.sendMessage('Bye Bye My Blue')
    baekcloud.stop()


baekcloud= chatbotmodel.baekcloud_bot()
baekcloud.add_handler('ticket', proc_ticket)
baekcloud.add_handler('stop', proc_stop)
baekcloud.start()
