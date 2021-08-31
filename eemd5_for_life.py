#!/bin/env python3
#> python3 eemd5_for_life.py | grep "HTB{.*}"

from hashlib import md5
from bs4 import BeautifulSoup as bs
import requests

def encode(string):
        res = md5(string.encode())
        return res.hexdigest()

with requests.session() as session:
        data = session.get("http://138.68.140.119:32471")
        soup = bs(data.text, "html.parser")
        md5 = encode(soup.find('h3').get_text())
        resp = session.post("http://138.68.140.119:32471",data={'hash':md5})
        print(resp.text)
