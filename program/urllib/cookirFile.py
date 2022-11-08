# cookie生成文件

import urllib.request,http.cookiejar

filename = 'cookie.txt'
# MozillaCookieJar是CookieJar的子类，可以将Cookie保存成 Mozilla 型浏览器的Cookie格式
cookie = http.cookiejar.MozillaCookieJar(filename)

# 
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://baidu.com' )
cookie.save(ignore_discard=True, ignore_expires=True )