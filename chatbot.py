import melon_ticket_app
import artist_finder
import chatbotmodel
import telegram
from pymongo import MongoClient

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

#find and set artist
def proc_artist(bot, update):
    print("which artist are you looking for?")
    baekcloud.sendMessage("which artist are you looking for?")

#database update
def proc_update(bot, update):
    melon_ticket_app.database_update()
    print("database updated")
    baekcloud.sendMessage("concert information updated")

#get ticket information
def proc_ticket(bot, update):
    for object in db.melon_ticket.find():
        message = str(object['title']) + "\n" + str(object['url'])
        #print(message)
        baekcloud.sendMessage(message)

#stop chatbot
def proc_stop(bot, update):
    baekcloud.sendMessage('Bye Bye My Blue')
    baekcloud.stop()

baekcloud= chatbotmodel.baekcloud_bot()
baekcloud.add_handler('update', proc_update)
baekcloud.add_handler('ticket', proc_ticket)
baekcloud.add_handler('bye', proc_stop)
baekcloud.add_handler('artist',proc_artist)
baekcloud.start()
