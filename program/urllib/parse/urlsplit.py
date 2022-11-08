# -*- coding: utf-8 -*- 
# @Time : 2022/11/8 17:15 
# @Author : 拼搏的小浣熊
# @File : urlsplit.py
from urllib.parse import urlsplit
result = urlsplit('https://www.baidu.con/index.html;user?id=5#comment')
print(result)
# 可以发现，返回结果是SplitResult，这其实也是一个元组，即可以用属性名获取其值，也可以用索引获取
print(result.scheme,result[0])