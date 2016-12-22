from bs4 import BeautifulSoup
from flask import request
import requests
import re
import pprint

class crawler(object):
    def __init__(self, a):
        self.a = a

    def tv_show():
        URL = "https://eztv.ag"
        name = request.form.get('text', "default_value")
        a = {}
        r = requests.get(URL + "/search/" + name, timeout=5)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        for link in soup.find_all('a', {'class': 'magnet'}, limit=5):
            result = (link.get('title'))
            result = result.replace(' Magnet Link', '')
            result = result.replace(' Torrent:', '')
            magnet = (link.get('href'))
            magnet = magnet.replace('&amp;', '&')
            dic = {result:magnet}
            a.update(dic)
        return a
