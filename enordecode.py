﻿#coding:UTF-8
from Tkinter import *
import tkMessageBox
import base64

def menu_about():#弹出作者和版本信息
        tkMessageBox.showinfo("About This","author:monburan version:0.1")
def getText_native():#实现加密的过程
        var4.set(base64.b64encode(var3.get()))
def getText_base64():#实现解密的过程
        var2.set(base64.b64decode(var1.get()))
        
class converter():
    def __init__(self,monster):
        menubar = Menu(monster)#生成菜单 
        menubar.add_command(label="help")
        menubar.add_command(label="about",command=menu_about)
        monster.config(menu=menubar)

        showframe = Frame(monster)#显示内容的框架
        showframe.pack(side=TOP)
        self.showLabel = Label(showframe,text="这是一个简单的转换工具").pack(fill=Y,pady=5)

        input_native = Frame(showframe)#输入native部分的框架
        input_native.pack(side=TOP)
        self.input_native = Label(input_native,text="base64加密：").pack()
        self.inputText_native = Entry(input_native,textvariable=var3,width=500).pack()
        self.input_nativeButton = Button(input_native,text="Sure",command=getText_native).pack(fill=Y,pady=5)
        output_base64 = Frame(showframe)#输出base64部分的框架
        output_base64.pack(side=TOP)
        self.output_base64 = Label(output_base64,text="加密结果：").pack()
        self.output_Text_base64 = Entry(output_base64,textvariable=var4,width=500).pack(fill=X)

        input_base64 = Frame(showframe)#输入base64部分的框架
        input_base64.pack(side=TOP)
        self.input_base64 = Label(input_base64,text="base64解密：").pack()
        self.inputText_base64 = Entry(input_base64,textvariable=var1,width=500).pack()
        self.input_base64Button = Button(input_base64,text="Sure",command=getText_base64).pack(fill=Y,pady=5)
        output_base64 = Frame(showframe)#输出native部分的框架
        output_base64.pack(side=TOP)
        self.output_native = Label(output_base64,text="解密结果：").pack()
        self.output_Text_native = Entry(output_base64,textvariable=var2,width=500).pack()

        bottomframe = Frame(monster)#底部退出按键
        bottomframe.pack()
        self.button = Button(bottomframe,text="Quit",command=bottomframe.quit).pack(fill=Y,pady=10)
        
win = Tk()#创建窗口
win.title("转换工具")#窗口标题

global var1#全局变量
var1=StringVar()
global var2
var2=StringVar()
global var3
var3=StringVar()
global var4
var4=StringVar()

app=converter(win)
win.mainloop()
