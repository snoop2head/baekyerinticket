from selenium import webdriver
from bs4 import BeautifulSoup

#find artist
artist_number=698776
artist_id=str(artist_number)
melon_ticket_url="https://ticket.melon.com/artist/index.htm?artistId="+artist_id


# setup Driver|Chrome
driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver")
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# get melon url
driver.get(melon_ticket_url)

driver.get(melon_ticket_url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.find_all('div',{'class':{'show_infor'}})

for n in notices:
    print(n.text.strip())

