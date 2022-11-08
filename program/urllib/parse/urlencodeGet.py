# -*- coding: utf-8 -*- 
# @Time : 2022/11/8 17:39 
# @Author : 拼搏的小浣熊 
# @File : urlencodeGet.py

from urllib.parse import urlencode

params = {
    'name': 'germey',
    'age': 25
}

base_url = 'https://www.baidu.com'
url = base_url + urlencode(params)
print(url)