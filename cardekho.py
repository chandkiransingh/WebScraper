import numpy as np
import pandas as pd

from bs4 import BeautifulSoup

import requests as rq

car = rq.get("https://www.cardekho.com/used-maruti-celerio+cars+in+delhi-ncr")

soup = BeautifulSoup(car.text)

soup.prettify()

carsList = []
# carsList.append(['sno', 'title', 'price', 'location', 'milage', 'fule_type', 'city'])
sno = 0
for i in soup.findAll("div", {"class": "holder"}):
    sno += 1
    title = i.find("div", {"class": "title"}).find('a').text
    price = i.find("div", {"class": "price"}).text
    location = ""
    if i.find("span", {"class": "truncate"}):
        location = i.find("span", {"class": "truncate"}).text
    milage = i.find("div", {"class": "dotlist"}).findAll('span')[0].text
    fule_type = i.find("div", {"class": "dotlist"}).findAll('span')[1].text
    city = i.find("div", {"class": "dotlist"}).findAll('span')[2].text
    mycar = [sno, title, price, location, milage, fule_type, city]
    carsList.append(mycar)

df = pd.DataFrame(carsList, columns=['sno', 'title', 'price', 'location', 'milage', 'fule_type', 'city'])
df.to_csv('carlist.csv', index=False)