# cookie生成文件

import urllib.request,http.cookiejar

filename = 'cookie.txt'
# MozillaCookieJar是CookieJar的子类，可以将Cookie保存成 Mozilla 型浏览器的Cookie格式
# cookie = http.cookiejar.MozillaCookieJar(filename)

# 另外,LwPCookieJar同样可以读取和保存Cookie,只是Cookie文件的保存格式和MozillaCookieJar不一样,它会保存成LWP( libwww-perl)格式。
cookie = http.cookiejar.LWPCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://baidu.com' )
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思       是如果cookies已经过期也将它保存并且文件已存在时将覆盖，
cookie.save(ignore_discard=True, ignore_expires=True )
