from bs4 import BeautifulSoup
import requests
import re

class crawler(serie):
    URL = "https://eztv.ag"
    name = "elementary"
    r = requests.get(URL + "/search/" + name, timeout=5)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a', {'class': 'epinfo'}):
        toto = (link.get('title'))
        result = re.search(r".*720.*", toto)
        if result:
            print (result.group(0))
