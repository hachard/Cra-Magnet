from bs4 import BeautifulSoup
import requests
import re


a = []

class crawler():
    URL = "https://eztv.ag"
    name = "elementary"
    r = requests.get(URL + "/search/" + name, timeout=5)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a', {'class': 'epinfo'}):
        result = (link.get('title'))
        a.append(result)
        print (a)
