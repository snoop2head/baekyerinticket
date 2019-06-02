import re
from bs4 import BeautifulSoup                     # 파싱을 편리하게 해주는 라이브러리
from urllib.request import urlopen

singer_name="ADOY"
target_melon_url = "https://ticket.melon.com/search/index.htm?q="+ singer_name
target_interpark_url="http://isearch.interpark.com/isearch?q="+ singer_name #This contains ticket URL
target_interpark_ticket_url= "http://ticket.interpark.com/search/ticket.asp?search=%uC544%uB3C4%uC774" #This is the target url


artist_number=698776
artist_id=str(artist_number)
melon_ticket_url="https://ticket.melon.com/artist/index.htm?artistId="+artist_id

html=urlopen(melon_ticket_url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
print(soup)
dummy = soup.find_all('div',{'class':{'show_infor'}})
print(dummy)

#on_sale = soup.find_all('div',{'class':{'result_Ticket'}})
#print(on_sale)
#target_interpark_url 백예린 Ticket search result
#<a data-payco="{&quot;nclickUrlPrefix&quot;:&quot;http://cc.toast.com/cc?m=0&amp;a=izq3UOdkl8IDC4p&amp;sid=154493546467573415&amp;adid=&amp;pgid=2dfa5ff68ff4cdeb&amp;platform=interpark:nx:pc&amp;query=%eb%b0%b1%ec%98%88%eb%a6%b0&amp;area=main&amp;pr=interpark%3Anx%3Apc&amp;sub_service=entPlayO&amp;c=entPlayO%3A1900591317001071&quot;}" data-egs="1" data-egs-srchobj="{&quot;section_id&quot;:&quot;searchlist_ticket&quot;, &quot;item_no&quot;:&quot;19005913&quot;, &quot;section_order&quot;:&quot;1&quot;, &quot;section_info&quot;:&quot;ticket&quot;,&quot;list_order&quot;:&quot;&quot; }" href="http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=19005913&amp;pis1=ticket&amp;pis2=product" class="name" target="_blank">레인보우 뮤직＆캠핑 페스티벌 2019</a>

