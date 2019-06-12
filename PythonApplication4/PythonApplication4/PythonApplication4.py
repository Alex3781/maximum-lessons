#влажность
import requests
import bs4
url="https://yandex.ru/pogoda/astrahan"
response=requests.get(url)
soup=bs4.BeautifulSoup(response.content,"lxml")
def get_pressure(soup):
    result=soup.find("i",{"class":"icon icon_pressure-white term__fact-icon"})
    return result.text 
print(get_pressure(soup))