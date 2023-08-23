import time

import requests
from bs4 import BeautifulSoup

while True:
    url = "https://www.bloomberght.com"

    response =requests.get("https://www.bloomberght.com")
    html_content = response.content
    clean_content = BeautifulSoup(html_content,"html.parser")
    
    names = []
    values = []
    changing = []

    for i in clean_content.find_all("small",{"class":"title"}):
        name = (i.text).strip()
        names.append(name)

    for i in clean_content.find_all("small",{"data-type":"son_fiyat"}):
        value = (i.text).strip()
        values.append(value)

    for i in clean_content.find_all("small",{"data-type":"yuzde_degisim"}):
        change = (i.text).strip()
        changing.append(change)

    for k,m,n in zip(names,values,changing):
        print("{} : {}    {}".format(k,m,n))
        time.sleep(1.1)
    print("\n")