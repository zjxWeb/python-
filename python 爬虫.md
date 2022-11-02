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

## 二. 爬虫基础

### 2.1 Http基本原理

+ URI和URL

  + URI即统一资源标志符；URL即统一资源定位符。

+ GET和POST请求方法有如下区别

  + GET请求中的参数包含在URL里面，数据可以在URL中看到；而POST请求的URL不会包含这些数据，数据都是通过表单形式传输的，会包含在请求体中。
  + GET请求提交的数据最多只有1024字节，post方式则没有限制

  + 登录时一般需要提交用户名和密码，其中密码是敏感信息，如果使用GET方式请求，密码就会暴漏在URL里面，造成密码泄露，所以这时候最好以POST方式发送。上传文件时，由于文件内容比较大，一次也会选POST方式。
  + GET：请求页面并返回页面内容。
  + HEAD：类似于GET请求，只不过返回的响应中没有具体内容，用于获取报头
  + POST：大多用于提交表单或上传文件，数据包含咋子请求体中
  + PUT：用客户端传向服务器的数据取代指定文档中的内容
  + DELETE：请求服务器删除指定的页面
  + CONNECT：把服务器当作跳板，让服务器代替客户端访问其他网页
  + OPTIONS：允许客户端查看服务端的性能
  + TRACE：回显服务器收到的请求。主要用于测试或诊断。

+ 请求的网址：

  + 请求的网址，它可以唯一确定客户端向请求的资源。

#### 2.1.1 请求头：

  + 请求头，用来说明服务器要使用的附加信息，比较重要的信息有Cookie、Refere、User-Agent等。
  + Accept：请求报头域，用于指定客户端可接受那些类型的信息。
  + Accept-Language： 用于指定客户端可接受的语言类型。
  + Accept-Encoding：用于致电给客户端可接受的内容编码。
  + Host：用于指定请求资源的主机IP和端口号，其内容为请求URL的原始服务器或网关的位置。
    + 从HTTP1.1版本开始，请求必须包含此内容。
  + Cookie：也常用复数形式Cookies，这是网站未来辨别用户，进行会话跟踪而存储在用户本地的数据。它的主要功能时维持当前访问会话。
  + Refer：用于表示请求是从哪个页面发过来的，服务器可以拿到这以信息并做相应的处理，如做来源统计，防盗链处理等。
  + User-Agent：简称UA，这是一个特殊的字符串头，可以使服务器识别客户端使用的操作系统及版本、浏览器及版本等信息。做爬虫时如果加上此信息，可以伪装为浏览器；如果不加，很可能会被识别出来。
  + Content-type：也叫互联网媒体类型或者MIME类型，在HTTP协议消息头中，它用来表示具体请求中的媒体类型信息。
    + text/html代表HTML格式，image/gif代表GIF图片，application/json代表JSON类型。

#### 2.1.2 请求体：

  + 请求体，一般承载的内容时POST请求中的表单数据，对于GET请求，请求体为空。
  + 登录之前,需要先填写用户名和密码信息，登录时这些内容会以表单数据的形式提交给服务器,此时需要注意Request Headers中指定Content-Type为application/x-www-form-urlencoded。只有这样设置Content-Type,内容才会以表单数据的形式提交。另外,也可以将Content-Type设置为appolication/json来提交JSON 数据,或者设置为multipart/form-data来上传文件。
  + |           Content-Type            | POST提交数据的方式表单数据 |
    | :-------------------------------: | :------------------------: |
    | application/x-www-form-urlencoded |          表单数据          |
    |        multipart/form-data        |        表单文件上传        |
    |         application/json          |       序列化JSON数据       |
    |              texUxml              |          XML数据           |

#### 2.1.3 响应（状态码）：

  + 响应,即 Response,由服务器返回给客户端,可以分为三部分:响应状态码( Response Status Code),响应头( Response Headers)和响应体(Response Body)。

  + 响应状态码

    + | 状态码 |      说明       |                             详情                             |
      | :----: | :-------------: | :----------------------------------------------------------: |
      |  100   |      继续       | 请求者应当继续提出请求。服务器已接收到请求的部分，正在等待其余部分 |
      |  101   |    切换协议     |      请求者已要求服务器切换协议，服务器已确认并准备切换      |
      |  200   |      成功       |                    服务器已成功处理了请求                    |
      |  201   |     已创建      |               请求成功并且服务器创建了新的资源               |
      |  202   |     已接受      |                 服务器已接收请求，但尚未处理                 |
      |  203   |   非授权信息    |     服务器已成功处理了请求,但返回的信息可能来自另一个源      |
      |  204   |     无内容      |           服务器成功处理了请求，但没有返回任何内容           |
      |  205   |    重置内容     |               服务器成功处理了请求,内容被重置                |
      |  206   |    部分内容     |                   服务器成功处理了部分请求                   |
      |  300   |    多种选择     |                针对请求，服务器可执行多种操作                |
      |  301   |    永久移动     |          请求的网页已永久移动到新位置，即永久重定向          |
      |  302   |    临时移动     |          请求的网页暂时跳转到其他页面，即暂时重定向          |
      |  303   |  查看其他位置   |     如果原来的请求是 POST，重定向目标文档应该通过GET提取     |
      |  304   |     未修改      |        此次请求返回的网页未经修改，继续使用上次的资源        |
      |  305   |    使用代理     |                 请求者应该使用代理访问该网页                 |
      |  307   |   临时重定向    |                 临时从其他位置响应请求的资源                 |
      |  400   |    错误请求     |                     服务器无法解析该请求                     |
      |  401   |     未授权      |               请求没有进行身份验证或验证未通过               |
      |  403   |    禁止访问     |                       服务器拒绝此请求                       |
      |  404   |     未找到      |                    服务器找不到请求的网页                    |
      |  405   |    方法禁用     |                 服务器禁用了请求中指定的方法                 |
      |  406   |     不接收      |               无法使用请求的内容响应请求的网页               |
      |  407   |  需要代理授权   |                    请求者需要使用代理授权                    |
      |  408   |    请求超时     |                        服务器请求超时                        |
      |  409   |      冲突       |                  服务器在完成请求时发生冲突                  |
      |  410   |     已删除      |                     请求的资源已永久删除                     |
      |  411   |  需要有效长度   |          服务器不接收不含有效内容长度标头字段的请求          |
      |  412   | 未满足前提条件  |        服务器未满足请求者在请求中设置的某一个前提条件        |
      |  413   |  请求实体过大   |              请求实体过大,超出服务器的处理能力               |
      |  414   |   请求URL过长   |                 请求网址过长,服务器无法处理                  |
      |  415   |   不支持类型    |                   请求格式不被请求页面支持                   |
      |  416   |  请求范围不符   |                    页面无法提供请求的范围                    |
      |  417   |  为满足期望值   |              服务器未满足期望请求标头字段的要求              |
      |  500   | 服务器 内部错误 |                 服务器遇到错误,无法完成请求                  |
      |  501   |     未实现      |                  服务器不具备完成请求的能力                  |
      |  502   |    错误网关     |       服务器作为网关或代理,接收到上游服务器的无效响应        |
      |  503   |   服务不可用    |                      服务器目前无法使用                      |
      |  504   |    网关超时     |     服务器作为网关或代理，没有及时从上游服务器接收到请求     |
      |  505   | HTTP版本不支持  |             服务器不支持请求中使用的HTTP协议版本             |

      

