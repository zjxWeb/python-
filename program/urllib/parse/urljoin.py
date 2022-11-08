# -*- coding: utf-8 -*- 
# @Time : 2022/11/8 17:33 
# @Author : 拼搏的小浣熊 
# @File : urljoin.py

from urllib.parse import urljoin
print(urljoin( 'https://www.baidu.com', 'FAQ.html'))
print(urljoin( 'https ://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
print(urljoin ( 'https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.htmi'))
print(urljoin( 'https://ww.baidu.com/about.htm2', 'https://cuiqingcai.com/FA.html?question-2'))
print(urljoin( ' https://www.baidu.com?wd=abc ', 'https://cuiqingcai.com/index.php'))
print(urljoin( 'https://ww.baidu.com', '?category=2#comment'))
