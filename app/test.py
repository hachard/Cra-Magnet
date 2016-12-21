from bs4 import BeautifulSoup
import requests
import re
import pprint

class crawler():
    
    URL = "https://eztv.ag"
    name = "elementary"
    a = {}
    r = requests.get(URL + "/search/" + name, timeout=5)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a', {'class': 'magnet'}, limit=5):
        #print (link)
        result = (link.get('title'))
        result = result.replace(' Magnet Link', '')
        magnet = (link.get('href'))
        magnet = magnet.replace('&amp;', '&')
        dic = {result:magnet}
        a.update(dic)
    pprint.pprint(a)