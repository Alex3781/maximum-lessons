import requests
import bs4
from datetime import datetime
url="http://www.cbr.ru/scripts/XML_daily.asp"
today=datetime.now().strftime("%d/%m/%y")
payload={"data_req":today}
response=requests.get(url,params=payload)
soup=bs4.BeatifulSoup(response.content,"lxml")
def get_course(id):
    valute=soup.find("valute",{"id":id})
    nominal=valute.nominal
    name=nominal.next_sibling
    value=valute.value
    return "За {} {} дают {}".format(nominal.text,value.text)
valutes=soup.find_all("valute")
print(valutes)
for valute in valutes:
    print(get_course(valute["id"])