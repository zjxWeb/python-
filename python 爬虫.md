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

- 前面安装好的Selenium 需要ChromeDriver配合使用。因为只有安装ChromeDriver，才能驱动Chrome浏览器完成相应的操作。
- 安装步骤：
  1. 下载ChromeDriver
     - 官方网站:https://sites.google.com/a/chromium.org/chromedriver
     - 下载地址:https://chromedriver.storage.googleapis.com/index.html

  2. 查看chrome版本，并下载相对应的ChromeDriver版本，**如果没有可以下载相近的。**
     - 点击 Chrome 菜单“帮助”→“关于Google Chrome”,即可查看Chrome的版本号
     - ![1](src/1.png)

  3. 环境变量配置
     - 在Windows下，建议直接将chromedriver.exe文件拖到Python的Scripts目录下，此外，也可以单独将其所在路径配置到环境变量。
     - ![2](src/2.png)
     - 验证安装
     
       - 在 `cmd`下执行`chromedriver`
     
       - ![3](src/3.png)
     
       - 随后执行一下的python代码进行测试
     
       - ```python
         from selenium import webdriver
         brower = webdriver.Chrome()
         ```
     
         - ![4](src/4.png)
         - 运行之后，如果弹出一个空白的Chrome浏览器，则证明所有的配置都没有问题。如果没有弹出,请检查之前的每一步配置。
         - 如果弹出后闪退,则可能是 ChromeDriverer版本和 Chrome版本不兼容，请更换 ChromeDriver版本。
         - 如果没有问题,接下来就可以利用Chrome来做网页抓取了。
     
#### 1.4 GeckoDriver的安装 

+ 对于Firefox配置基本和chrome一样

+ 下载地址

  + GitHub: https://github.com/mozilla/geckodriver
  + 下载地址:https://github.com/mozilla/geckodriver/releases

+ 验证代码：

  + ```python
    from selenium import webdriver
    brower = webdriver.Firefox()
    ```

#### 1.5 PhantomJs（无界面浏览器）的安装

+ PhantomJS是一个无界面的、可脚本编程的WebKit浏览器引擎,它原生支持多种Web标准：DOM操作、CSS选择器、JSON、Canvas以及SVG。

+ Selenium支持 PhantomJS,这样在运行的时候就不会再弹出一个浏览器了。而且 PhantomJS的运行效率也很高,还支持各种参数配置，使用非常方便。下面我们就来了解一下 PhantomJS的安装过程。

+ 下载

  + https://phantomjs.org/download.html
  + 和上面安装过程一样 **将.exe文件放到 python的script文件中。**

+ 验证

  + 在`cmd`中执行 `phantomjs`

  + ```python
    from selenium import webdriver
    browser = webdriver. PhantomJS()
    browser.get(' https://www.baidu.com')
    print(browser.current_url)
    ```

  + 这里Selenium已经放弃了phantomjs，所以要使用上述代码进行检验需要 **卸载最新版本，下载低版本**

#### 1.6 aiohttp安装

+ 之前介绍的 requests库是一个阻塞式HTTP请求库,当我们发出一个请求后，程序会直等待服务器响应，直到得到响应后，程序才会进行下一步处理。其实，这个过程比较耗费时间。如果程序可以在这个等待过程中做一些其他的事情,如进行请求的调度、响应的处理等,那么爬取效率一定会大大提高。
+ aiohttp就是这样一个提供异步Web服务的库,从Python 3.5版本开始,Python中加入async/await关键字,使得回调的写法更加直观和人性化。aiohttp的异步操作借助于async/await关键字的写法变得更加简洁，架构更加清晰。使用异步请求库进行数据抓取时，会大大提高效率，下面我们来看一下这个库的安装方法。
+ 官方文档:http://aiohttp.readthedocs.io/en/stable
+ GitHub: https://github.com/aio-libs/aiohttp
+ PyPI: https://pypi.python.org/pypi/aiohttp
+ 安装
  + `pip3 install aiohttp`
  + 另外,官方还推荐安装如下两个库:个是字符编码检测库 cchardet,另一个是加速DNS的解析库aiodns。安装命令如下:
    + `pip3 install cchardet aiodns `
+ 验证
  + `import aiohttp`,在python下输入没有报错，则证明安装成功。

## 二. 

