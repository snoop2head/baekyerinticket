import requests                                   # 파싱 할 곳의 html을 얻기 위한 requests
from bs4 import BeautifulSoup                     # 파싱을 편리하게 해주는 라이브러리

singer_name="백예린"
target_melon_url = "https://ticket.melon.com/search/index.htm?q="+ singer_name
target_interpark_url="http://isearch.interpark.com/isearch?q="+ singer_name #This contains ticket URL
target_interpark_ticket_url= "http://ticket.interpark.com/search/ticket.asp?search=%uC544%uB3C4%uC774" #This is the target url


data = requests.get(target_interpark_ticket_url)         # get 요청으로 html을 가져와라
soup = BeautifulSoup(data.text, 'lxml')    # 가져온 html을 BeautifulSoup 라이브러리로 예쁘게 만들자
#print(soup)

on_sale = soup.find_all('div',{'class':{'result_Ticket'}})
print(on_sale)
