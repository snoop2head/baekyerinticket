import requests                                   # 파싱 할 곳의 html을 얻기 위한 requests
from bs4 import BeautifulSoup                     # 파싱을 편리하게 해주는 라이브러리

singer_name="백예린"
target_melon_url = "https://ticket.melon.com/search/index.htm?q="+ singer_name
target_interpark_url="http://isearch.interpark.com/isearch?q="+ singer_name

print(target_interpark_url)


