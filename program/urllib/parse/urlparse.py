# 该方法可以实现URL的而识别和分段
from urllib.parse import urlparse

result = urlparse('https://www.baidu.con/index.html;user?id=5#comment',allow_fragments=False)
print(type(result))
# 这里我们利用urlparse方法对一个URL进行了解析，然后输出了解析结构的类型以及结果本身
print(result)
# 可以看到,解析结果是一个ParseResult类型的对象,包含6部分,分别是scheme , netloc, path、params,query 和fIagment