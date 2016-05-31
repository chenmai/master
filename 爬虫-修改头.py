#python3.4 爬虫教程
#一个简单的示例爬虫
#林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)
import urllib.request
weburl = "http://www.douban.com/"
webheader = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
req = urllib.request.Request(url=weburl, headers=webheader)  
webPage=urllib.request.urlopen(req)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
