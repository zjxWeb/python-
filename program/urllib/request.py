# -*- coding: UTF-8 -*-
from urllib import request,parse
# class urllib.request.Request(url,data=None,headers=f, origin_req_host=None，unverifiable=False，method=None)
url = 'http://127.0.0.1:3000/idLightMsg'
# headers = {
#     'User-Agent': 'Mozi11a/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'www.httpbin.org'
# }

dict = {"id": 32}
data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url=url, data=data, headers=headers, method="POST")
req = request.Request(url=url, data=data, method="POST")
# 使用此方法记得将 “：” 变成  “，”
req.add_header('User-Agent', 'Mozi11a/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))