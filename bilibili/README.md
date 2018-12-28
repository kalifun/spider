# bilibili相簿（绘你所想，拍你所爱）
## 前言
### 逛了这么久b站才知道有相簿这玩意。里面分两大块，绘画和摄像。[哔哩哔哩相簿，绘你所想，拍你所爱](https://h.bilibili.com/)
### 里面的插画不错，可以用来作壁纸。如果对cos感兴趣的也可以逛一逛。
## 1.分析网页
### 我对爬虫并不是很熟悉，每次在分析这块就让我放弃了（还不是因为懒）。  又是熟悉的F12，打开网页刷一刷，找找接口什么的啊。
[![](https://image.kalifun.top/upload/1812/3860cc8577026b0e.png)](https://image.kalifun.top/upload/1812/3860cc8577026b0e.png)
### 这个是API接口，你用浏览器一看就知道了。
## 2.撸代码
## 3.遇到的问题
### 我获取到接口后我一直对接口的Network去分析，结果一直报错。
``` python
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.vc.bilibili.com', port=443):
Max retries exceeded with url: /link_draw/v2/Photo/list?category=sifu&type=hot&page_num= 
(Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x00000000031E4D30>: 
Failed to establish a new connection: [Errno 10060] ',))
```
### 各种百度，答案千奇百怪。有的说是keep_alive的错误，需要设置为False，还是无果。
### 我就想是不是公司的网络的限制，因为连自己服务器都需要代理，让我爬虫是不可能的。
### 在自己服务器debug，发现没有任何报错。
### 执行程序
``` python
python bilibili.py
```
#### 在你执行的程序目录下会创建文件夹，如果你觉得没必要根据uid进行创建目录，去除username并将函数改成传递一个参即可。
