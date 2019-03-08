#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import os, sys
from urllib import request
from bs4 import BeautifulSoup


from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
from tkinter.messagebox import *
#import tkinter.filedialog as tkFileDialog
#import tkinter.simpledialog as tkSimpleDialog    #askstring()
from tkinter import filedialog
from PIL import Image

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('弹琴吧乐谱下载 tanqinba-downloader')
        # To center the window on the screen.
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws / 2) - (363 / 2)
        y = (hs / 2) - (345 / 2)
        self.master.geometry('%dx%d+%d+%d' % (363,345,x,y))
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Command2Var = StringVar(value='下载')
        self.style.configure('TCommand2.TButton', font=('微软雅黑',9))
        self.Command2 = Button(self.top, text='下载', textvariable=self.Command2Var, command=self.Command2_Cmd, style='TCommand2.TButton')
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda : self.Command2Var.get()
        self.Command2.place(relx=0.066, rely=0.835, relwidth=0.884, relheight=0.119)

        self.Check2Var = IntVar(value=0)
        self.style.configure('TCheck2.TCheckbutton', font=('微软雅黑',9))
        self.Check2 = Checkbutton(self.top, text='以黑白底色输出（不选择底色为黄色）', variable=self.Check2Var, style='TCheck2.TCheckbutton')
        self.Check2.setValue = lambda x: self.Check2Var.set(x)
        self.Check2.value = lambda : self.Check2Var.get()
        self.Check2.place(relx=0.066, rely=0.464, relwidth=0.62, relheight=0.072)

        self.Check1Var = IntVar(value=0)
        self.style.configure('TCheck1.TCheckbutton', font=('微软雅黑',9))
        self.Check1 = Checkbutton(self.top, text='新建以乐谱标题为名的文件夹来放置多张乐谱', variable=self.Check1Var, style='TCheck1.TCheckbutton')
        self.Check1.setValue = lambda x: self.Check1Var.set(x)
        self.Check1.value = lambda : self.Check1Var.get()
        self.Check1.place(relx=0.066, rely=0.371, relwidth=0.73, relheight=0.072)

        self.Command1Var = StringVar(value='浏览')
        self.style.configure('TCommand1.TButton', font=('微软雅黑',9))
        self.Command1 = Button(self.top, text='浏览', textvariable=self.Command1Var, command=self.Command1_Cmd, style='TCommand1.TButton')
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda : self.Command1Var.get()
        self.Command1.place(relx=0.749, rely=0.278, relwidth=0.179, relheight=0.072)

        self.Text2Var = StringVar(value='')
        self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=('微软雅黑',9))
        self.Text2.setText = lambda x: self.Text2Var.set(x)
        self.Text2.text = lambda : self.Text2Var.get()
        self.Text2.place(relx=0.066, rely=0.278, relwidth=0.664, relheight=0.072)

        self.Label3Var = StringVar(value='保存位置：')
        self.style.configure('TLabel3.TLabel', anchor='w', font=('微软雅黑',9))
        self.Label3 = Label(self.top, text='保存位置：', textvariable=self.Label3Var, style='TLabel3.TLabel')
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda : self.Label3Var.get()
        self.Label3.place(relx=0.066, rely=0.22, relwidth=0.245, relheight=0.049)

        self.Text3Var = StringVar(value='输出')
        self.Text3 = Entry(self.top, textvariable=self.Text3Var, font=('微软雅黑',9))
        self.Text3.setText = lambda x: self.Text3Var.set(x)
        self.Text3.text = lambda : self.Text3Var.get()
        self.Text3.place(relx=0.066, rely=0.557, relwidth=0.862, relheight=0.235)

        self.Combo1List = ['钢琴谱', '吉他谱']
        self.Combo1Var = StringVar(value='乐谱类型')
        self.Combo1 = Combobox(self.top, text='Add items in design or code!', textvariable=self.Combo1Var, values=self.Combo1List, font=('微软雅黑',9))
        self.Combo1.setText = lambda x: self.Combo1Var.set(x)
        self.Combo1.text = lambda : self.Combo1Var.get()
        self.Combo1.place(relx=0.066, rely=0.139, relwidth=0.421)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('微软雅黑',9))
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda : self.Text1Var.get()
        self.Text1.place(relx=0.507, rely=0.139, relwidth=0.421, relheight=0.072)

        self.Label1Var = StringVar(value='乐谱类型：')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('微软雅黑',9))
        self.Label1 = Label(self.top, text='乐谱类型：', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.066, rely=0.081, relwidth=0.245, relheight=0.049)

        self.Label2Var = StringVar(value='乐谱编号 ID：')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('微软雅黑',9))
        self.Label2 = Label(self.top, text='乐谱编号ID：', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.507, rely=0.081, relwidth=0.245, relheight=0.049)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command2_Cmd(self, event=None):
        if self.getUrl() == 0:
            return
        if self.download():
            return



    def Command1_Cmd(self, event=None):
        '''浏览 点击后打开选择文件夹窗口'''
        path = filedialog.askdirectory()
        self.Text2Var.set(path)

    def download(self):
        if self.newDict():
            return 1
        n = 1
        while True:
            try:
                request.urlretrieve(self.imgUrlStr, '%s/%s.png' % (self.path, str(n)))  # 下载图片
                self.picToBlackWhite('%s/%s.png' % (self.path, str(n)))  # 黑白
                self.imgUrlStr = self.imgUrlStr.replace(str(n - 1) + '.png', str(n) + '.png')
                n += 1
            except:
                # print('Done!')
                yesNo = askyesno('Done!', '“' + self.title + '” 下载完成！打开文件夹？')
                if yesNo == True:
                    os.startfile(self.path)
                break

    def getUrl(self):
        id = self.Text1Var.get()
        url = 'http://www.tan8.com/codeindex.php?d=web&c=weixin&m=piano&id={}'.format(id)
        try:
            req = requests.get(url=url)  # 爬取网站源码
            bf = BeautifulSoup(req.text, 'html.parser')  # 转为BS对象
            imgUrlInPageList = bf.find_all('img', width='100%')  # 找到所有图片链接源代码
            self.imgUrlStr = imgUrlInPageList[0].get('src')  # 找到第一个链接
            titleInPageList = bf.find_all('h3', class_='content_title_1113')
            self.title = titleInPageList[0].text
        except IndexError:
            showerror('ERROR', 'ID Error!')
            return 1

    def picToBlackWhite(self, filePath):
        if self.Check2Var.get() == 1:
            img = Image.open(filePath)
            imgBlackWhite = img.convert('L')
            imgBlackWhite.save(filePath)

    def newDict(self):
        if self.emptyPath():
            return 1
        if self.Check1Var.get() == 1:
            self.path = self.Text2Var.get() + '/' + self.title
            if os.path.exists(self.path):
                showerror('目录存在', '目录 『' + self.path + '』已经存在！')
                return 1
            os.makedirs(self.path)
        else:
            self.path = self.Text2Var.get()

    def emptyPath(self):
        if self.Text2Var.get() == '':
            showerror('Error', 'Path Error')
            return 1

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

