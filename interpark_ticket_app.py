from selenium import webdriver
from bs4 import BeautifulSoup
from pymongo import MongoClient

def interpark_db_update(singer_name):
    #database setting
    client = MongoClient('localhost',27017)
    db = client.dbsparta
    ticket_db = db.ticket_db.find() #creating collection named interpark_ticket

    #find artist
    target_interpark_url="http://ticket.interpark.com/search/ticket.asp?search="+ singer_name #This contains ticket URL


    # setup Driver|Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver", chrome_options=options)
    driver.implicitly_wait(10) # waiting web source for three seconds implicitly

    #get interpark url
    driver.get(target_interpark_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #parsing
    active_ticket_information_soup = soup.find_all("div", {"class": "result_Ticket", "id": "ticketplay_result"}) #Not including titles but pretty
    title_href = active_ticket_information_soup[0]
    #print(title_href)
    h4_titles = title_href.find_all("h4")
    #print(h4_titles)

    b=[]
    for i in h4_titles:
        links = i.find_all('a')
        #print(links)
        for link in links:
            url = link['href']
            b.append({i.text:url})
            db.ticket_db.insert_one({'title':i.text,'url':url})
            print(b)



