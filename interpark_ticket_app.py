from selenium import webdriver
from bs4 import BeautifulSoup

#find artist
singer_name="백예린"
target_interpark_url="http://isearch.interpark.com/isearch?q="+ singer_name #This contains ticket URL


# setup Driver|Chrome
driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver")
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# get interpark url
#driver.get(target_interpark_url)


driver.get(target_interpark_url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#notices = soup.find_all('div',{'class':{'ticketImgList'}})
notices = soup.find_all("ul", {"class": "ticketListWrap"})

for n in notices:
    print(n.text.strip())

