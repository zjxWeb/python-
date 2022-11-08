import socket
import urllib.request
import urllib.error

# reason属性返回的不一定是字符串，也可能是一个对象
try:
    response = urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('Time OUT')
# reason属性的结果是socket.timeout类。所以这里可以用isintance方法来判断它的类型，做出更详细的异常普安段。