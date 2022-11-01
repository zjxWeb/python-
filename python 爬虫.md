---
typora-root-url: src
---

# python 爬虫

## 一. 开发环境配置

### 1. 请求库的安装

+ 爬虫可以简单分为几步：抓取页面、分析页面和存储数据
+ 在抓取页面的过程中，我们需要模拟浏览器向服务器发出请求，所以需要用到一些Python库来实现HTTP请求操作。这里使用到的第三方库有`requests`、`Selenium`、`aiohttp`等。

#### 1.1 requests安装

+ 由于requests属于第三方库，也就是Python默认不会自带这个库，所以需要我们手动安装。这里采用的是`pip3`的方法安装。

+ 验证安装

  + ```py
    import requests
    ```

  + 首先输入python3,进入命令行模式，然后输入上述内容，如果什么错误提示也没有，就证明已经成功安装了requests。

#### 1.2 Selenium 的安装

+ Selenium 是一个自动化测试工具，利用它我们可以驱动浏览器执行特定的动作，如点击、下拉等操作。这里采用的是`pip3`的方法安装。

+ 验证安装

  + ```python
    import selenium 
    ```

  + 后面需要配合浏览器来共工作

#### 1.3 ChromeDriver的安装

+ 

