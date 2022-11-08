from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy_hander = ProxyHandler({
    # 可以添加多个代理
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
})

opener = build_opener(proxy_hander)

try:
    reponse = opener.open('https://baidu.com')
    print(reponse.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
