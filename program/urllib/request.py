# -*- coding: UTF-8 -*-
from urllib import request,parse
# class urllib.request.Request(url,data=None,headers=f, origin_req_host=None，unverifiable=False，method=None)
url = 'www.httpbin.org/post'
headers = {
    'User-Agent': 'Mozi11a/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'www.httpbin.org'
}

dict = {"name": 'germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode('utf-8'))