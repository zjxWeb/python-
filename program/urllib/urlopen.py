# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse


# urlopen
# urllib. request模块提供了最基本的构造HTTP请求的方法,利用这个模块可以模拟浏览器的请求发起过程，同时它还具有处理授权验证(Authentication )、重定向(Redirection )、浏览器Cookie以,及其他一些功能。


# response = urllib.request.urlopen("https://www.python.org")

# print(response.read().decode('utf-8'))

# 响应是一个 HTTPResposne类型的对象，主要包含 read,readinto、 getheader.getheaders、 fileno 等方法，以及msg, version ,status. reason、debuglevel .closed等属性。
# print(type(response))

# urllib.request.urlopen(url,data=None, [timeout, ]*, cafile-None , capatheNone ,cadefault=False, context-None)
# data 参数
# timeout 参数 0.1
# context 参数 该参数必须是ssl.SSLContext类型，用来指定SSL的设置。
data = bytes(urllib.parse.urlencode({"id": 32}), encoding='utf-8')
# post 请求，传参"id": 32
try:
    response = urllib.request.urlopen("http://127.0.0.1:3000/idLightMsg", data=data, timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason.socket.timeout):
        print('time out')
print(response.read().decode('utf-8'))

