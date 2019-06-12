import requests
import bs4

def get_content(city):
    url="https://yandex.ru/pogoda/"+city 
    response=requests.get(url)
    soup=bs4.BeautifulSoup(response.content,"lxml")
    return soup
def get_temp(soup):
    result=soup.find("span",{"class":"temp__value"})
    return result.text 
def get_condition(soup):
    result=soup.find("div",{"class":"link__condition"}) 
    return result.text
def main(city):
    soup=get_content(city)
    
    print(get_temp(soup))
    print(get_condition(soup))
main("Berlin")