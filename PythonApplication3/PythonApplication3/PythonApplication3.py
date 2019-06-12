#влажность 

import requests
import bs4
url="https://yandex.ru/pogoda/astrahan"
response=requests.get(url)
soup=bs4.BeautifulSoup(response.content,"lxml")
def davlenie(soup): 
    result=soup.find("#text",{"class":"term__value"})
    return result.text
print(davlenie(soup))