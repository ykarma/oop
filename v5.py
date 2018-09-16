import requests
import json
from urllib import parse

baseurl = 'http://fanyi.baidu.com/sug'

data = {
    'kw': 'girl'
}

#data = parse.urlencode(data).encode("utf-8")

headers = {
    'Content-Length': str(len(data))
}

rsp = requests.post(baseurl, data=data, headers=headers)

#json_data = rsp.read().decode("utf-8")
print(rsp.text)
print(rsp.json())


#for item in json_data['data']:
#    print(item['k']), "--", item['v']

