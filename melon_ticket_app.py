from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

def database_update(artist_number):
    #database setting
    client = MongoClient('localhost',27017)
    db = client.dbsparta
    melon_ticket = db.melon_ticket.find() #creating collection named melon_ticket

    #find artist
    artist_id=str(artist_number) #yerin baek's artist number 698776, ADOY's artist number 1704627
    melon_ticket_url="https://ticket.melon.com/artist/index.htm?artistId="+artist_id
    #artist_name="ADOY"
    #melon_ticket_url_2="https://ticket.melon.com/search/index.htm?q="+artist_name+"#"

    #setup driver|chrome

    #webdriver option without showing chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver", chrome_options=options)
    driver.implicitly_wait(10) # waiting web source for three seconds implicitly

    # get melon url
    driver.get(melon_ticket_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #parsing information
    all_text_notices = soup.find_all('div',{'class':{'show_infor'}})
    urls_and_titles = soup.find_all('span',{'class':{'show_title'}})
    on_sale=soup.find_all('span',{'class':{'ico_list ico_list4'}})

    #drop database collection when function is called
    db.drop_collection("melon_ticket")

    #{title:url} database for tickets)
    b =[]

    for i in urls_and_titles:
        links = i.find_all('a')
        #limiting the length of list smaller than plays available
        if len(b) < len(on_sale):
            for link in links:
                #print(link)
                url='https://ticket.melon.com/'+link['href']
                b.append({i.text:url})
                db.melon_ticket.insert_one({'title':i.text,'url':url})
                print(b)
        else:
            break


#print list of the ticket database
#print (b)

'''
            former_data = {'title':,'url':}
            new_data = {'$set':{'title':i.text,'url':url}} 
            db.melon_ticket.update_one(former_data,new_data) # this is replacing dataset 
'''
'''
#all text notices including status of ticket selling
for n in all_text_notices:
    print(n.text.strip())

#titles
for i in urls_and_titles:
    print(i.text.strip())
'''
