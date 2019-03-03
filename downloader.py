import requests
from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.tan8.com/codeindex.php?d=web&c=weixin&m=piano&id=1231231'

try:
    req = requests.get(url=url)  # 爬取网站源码
    bf = BeautifulSoup(req.text, 'html.parser')  # 转为BS对象
    imgUrlInPageList = bf.find_all('img', width='100%')  # 找到所有图片链接源代码
    imgUrlStr = imgUrlInPageList[0].get('src')  # 找到第一个链接
except IndexError:
    print('ID ERROR')
n = 1
while True:
    try:
        request.urlretrieve(imgUrlStr, '%s/%s.png'%('D:\programsTest',str(n)))  # 下载图片
        imgUrlStr = imgUrlStr.replace(str(n-1)+'.png', str(n)+'.png')
        print('第%s张下载完成'%(str(n)))
        n += 1
    except:
        print('Done!')
        break
