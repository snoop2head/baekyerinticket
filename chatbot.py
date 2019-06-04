import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters  # import modules
import melon_ticket_app
import artist_finder
import chatbotmodel
import telegram
from pymongo import MongoClient

#database setting
client = MongoClient('localhost',27017)
db = client.dbsparta
collection = db.melon_ticket
#index = db.melon_ticket.find() #indexing from database
dbaccess_an_item = collection.find_one()
dbaccess_multiple_item = collection.find({})


#token settings
baekcloud_token = '733519455:AAFn6_CUmVo2GCYz6Y9sl3JpuoZoJ_U2PWo'
baekcloud = telegram.Bot(token = baekcloud_token)
updates = baekcloud.getUpdates()

# message reply function
# update is json format
def get_message(bot , update) :
    if update.message.text == "bye":
        baekcloud.sendMessage('Bye Bye My Blue')
        baekcloud.stop()
    else:
        update.message.reply_text("got your artist: " + str(update.message.text) + "\n" + "please wait for a moment")
        print(update.message.text)
        artist_no=artist_finder.artist(update.message.text)
        print(artist_no)
        melon_ticket_app.database_update(artist_no)
        print(collection.count_documents({}))
        if collection.count_documents({}) == 0:
            baekcloud.sendMessage("there are no tickets on sale at the moment")
        else:
            update.message.reply_text("Here are tickets on sale at the moment")
            for object in collection.find():
                message = str(object['title']) + "\n" + str(object['url'])
                #print(message)
                baekcloud.sendMessage(message)

updater = Updater(baekcloud_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)


'''
        
#find and set artist
def proc_inquire_artist(bot, update):
    print("artist received")
    baekcloud.sendMessage("which artist are you looking for?")
    proc_artist(bot, update)

def proc_artist(bot, update):
    print(1)
    print(update)
    text = update.message.text
    print(text)
    #artist_finder(text)
    #print(artist_finder(text))
    
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

baekcloud.add_handler('artist',proc_inquire_artist)
baekcloud.add_handler('update', proc_update)
baekcloud.add_handler('ticket', proc_ticket)
baekcloud.add_handler('bye', proc_stop)


'''

baekcloud= chatbotmodel.baekcloud_bot()

updater.start_polling(timeout=3, clean=True)
updater.idle()

baekcloud.start()


