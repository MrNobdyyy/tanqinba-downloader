# 接口已经被修复，该程序已经不可用

# tanqinba-downloader
弹琴吧乐谱下载器 下载钢琴或者吉他谱（包括VIP）

## 简介

### 声明

- 程序只适用于学习开发和研究，禁止用于商业用途，一切操作造成的后果作者不予承担。使用程序代表用户同意此免责声明。
- 使用方法在本文已经阐述十分明白，故不再赘述。
- 程序的实现原理还有很长的篇幅，这里只是简介，有兴趣的请移步（Evernote）：

### 使用方法

- 程序截图

![程序截图](https://s2.ax1x.com/2019/03/09/ASBJPK.png)

- 乐谱类型

  选择乐谱类型，“钢琴谱”或者“吉他谱”，必选项

- 乐谱编号（ID）

  ![](https://s2.ax1x.com/2019/03/09/ASBBVI.png)

钢琴谱为例，链接中的数字就是ID，如`http://www.tan8.com/yuepu-100.html`中**100**就是ID，吉他谱同理。将ID输入到文本框中即可，此为必填项。

- 保存位置

  乐谱图片保存位置，单击浏览按钮可以选择文件夹，也可以自行输入。注意此路径不包括下文新建文件夹的路径。为必填项。

- 新建以乐谱标题为名的文件夹来放置多张乐谱

  复选框，下载图片时会新建一个文件夹，图片就存在这个文件夹中。文件夹名称为乐谱名称，上面那张图为例，文件夹名字就叫『钢琴谱：Always with me（千与千寻片尾曲，久石让）』，不包括括号。

- 以黑白底色输出（不选择底色为黄色或者透明）

  处理图片，具体说明在下文『程序原理与简介』的『图片处理』中。

- 输出框

  显示程序运行状态。

- 下载按钮

  点击后开始下载任务，完成后弹出窗口，询问是否打开文件夹。

### 程序原理与简介

#### 文件功能

- 程序使用Python3.6编写，downloader.py文件是本程序最基本的实现部分。downloaderGUI.py是主程序，使用GUI界面，主要由Tkinter编写，界面部分由VB界面转Tk源码的工具Tkinter Designer制作。

#### 抓取图片

- 钢琴谱通过微信分享链接中的隐藏链接获取，吉他谱直接由PC端的网页分析得出。
- 使用requests、BeautifulSoup、urllib等模块抓取图片。

#### 图片处理

- 钢琴谱下载后的图片底色为淡黄色，为了打印和浏览方便，程序带有将底色转换为白色的功能；吉他谱下载后图片底色为透明色，为了打印和浏览方便，程序带有将底色上色为白色的功能。
- 功能主要使用PIL模块处理图片。钢琴谱直接把颜色处理模式换成“灰度”即可获得黑白图片；吉他谱实现原理是将图片中alpha值为0的像素的alpha值改为100，因为需要遍历图片所有像素，速度稍慢，希望有朋友能使用更优雅的解决方案。

#### 新建文件夹放置图片

- 考虑到乐谱众多，新建文件夹并且输入乐谱名称十分麻烦，建立新建文件夹放置功能。
- 新建文件夹使用os模块，爬取乐谱标题使用了requests和BeautifulSoup模块。
