from urllib import request,error

try:
    response = request.urlopen('https://cuiqingcai.com/404')
except error.URLError as e:
    # reason属相，即返回错误的原因
    print(e.reason)