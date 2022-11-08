# -*- coding: utf-8 -*- 
# @Time : 2022/11/8 17:28 
# @Author : 拼搏的小浣熊 
# @File : urlunsplit.py

from urllib.parse import urlunsplit
data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))