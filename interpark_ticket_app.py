from selenium import webdriver
from bs4 import BeautifulSoup

#find artist
singer_name="ADOY"
target_interpark_url="http://isearch.interpark.com/isearch?q="+ singer_name #This contains ticket URL


# setup Driver|Chrome
driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver")
driver.implicitly_wait(3) # waiting web source for three seconds implicitly
# get interpark url
#driver.get(target_interpark_url)


driver.get(target_interpark_url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#notices = soup.find_all("ul", {"class": "ticketListWrap"}) #Including titles but not pretty
notices = soup.find_all("div", {"class": "pdInfo"}) #Not including titles but pretty


for n in notices:
    print(n.text.strip())

