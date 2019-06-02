from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

#database setting
client = MongoClient('localhost',27017)
db = client.dbsparta
melon_ticket = db.melon_ticket.find()

#find artist
artist_number=698776
artist_id=str(artist_number)
melon_ticket_url="https://ticket.melon.com/artist/index.htm?artistId="+artist_id

#setup driver|chrome
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver", chrome_options=options)
driver.implicitly_wait(3) # waiting web source for three seconds implicitly

# get melon url
driver.get(melon_ticket_url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#parsing information
all_text_notices = soup.find_all('div',{'class':{'show_infor'}})
urls_and_titles = soup.find_all('span',{'class':{'show_title'}})

#{title:url} database for tickets

b =[]
for i in urls_and_titles:
    links = i.find_all('a')
    for link in links:
        url='https://ticket.melon.com/'+link['href']
        b.append({i.text:url})
        db.melon_ticket.insert_one({'title':i.text,'url':url})

#print (b)





'''
#all text notices including status of ticket selling
for n in all_text_notices:
    print(n.text.strip())

#titles
for i in urls_and_titles:
    print(i.text.strip())
'''
