# 简单爬虫の站点图库
### 前言
>#### 由于网站换了主题，需要大量二次元的照片，可是我又不知道哪里有这样的图片，所以只能随便找一个有二次元图片的网站爬了。
### 1.站点分析
![![](https://image.kalifun.top/upload/1904/fb880c41f0bafeae.png)](https://image.kalifun.top/upload/1904/fb880c41f0bafeae.png)
#### 1.1获取URL
##### 第一页URL：
```
http://www.xxxxxxx.com/wallpaper_192_0_0_1.html
```
![![](https://image.kalifun.top/upload/1904/096d34ba81fc2050.png)](https://image.kalifun.top/upload/1904/096d34ba81fc2050.png)
##### 点击一个图片将会获取一组照片
![![](https://image.kalifun.top/upload/1904/c06278fdd79d457f.png)](https://image.kalifun.top/upload/1904/c06278fdd79d457f.png)
##### 从下面获取一组照片的链接
##### 你会发现你获取的照片是压缩照片
```
http://ppp.xxxxx.com/wallpaper/2019-04-04/5ca56f37ae4f6_120_80.jpg
上面的是获取的封面图，我们需要获取的是大图。修改成下面的链接即可。
http://pic1.win4000.com/wallpaper/2019-04-04/5ca56f37ae4f6.jpg
```
#### 1.2获取分页的URL
```
<div class="pages">
<div> <span class="curr">1</span><a class="num" rel="nofollow" href="http://xxxxxxx/wallpaper_192_0_0_2.html">2</a><a class="num" rel="nofollow" href="http://xxxxxxx/wallpaper_192_0_0_3.html">3</a><a class="num" rel="nofollow" href="http://xxxxxxx/wallpaper_192_0_0_4.html">4</a><a class="num" rel="nofollow" href="http://xxxxxxx/wallpaper_192_0_0_5.html">5</a> <a class="next" href="http://xxxxxxx/wallpaper_192_0_0_2.html">下一页</a></div>                </div>
```
##### 获取到分页就是和之前一样了。
#### 页面所以图片的URL--->获取每组照片的URL--->获取照片保存
### 2.代码
#### 使用的是BeautifulSoup没啥讲的，代码也很简单。而且很多优化的地方。
## [Github](https://github.com/kalifun/spider_py/tree/master/meizhuo)
