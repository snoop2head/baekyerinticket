from selenium import webdriver
from bs4 import BeautifulSoup

def artist(name):
    #webdriver option without showing chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver", chrome_options=options)
    driver.implicitly_wait(10) # waiting web source for three seconds implicitly

    # get melon url
    artist_url = "https://www.melon.com/search/total/index.htm?q="+str(name)+"&section=&linkOrText=T&ipath=srch_form"
    driver.get(artist_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #parsing information
    #artist_info = soup.find_all('div',{'class':{'info_01'}})
    #artist_info_specific = artist_info.find_all("a", {'class':{'atistname'}})
    #print(artist_info)
    #print(artist_info_specific)
    artist_number = soup.find('input',{'name':{'artistId'}})['value']
    #print(artist_number)
    return artist_number


