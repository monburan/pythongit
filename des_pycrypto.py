#coding:GB2312
#__author__:monburan
from Crypto.Cipher import DES3
from Tkinter import *
import tkMessageBox

class converter():
    def __init__(self,monster):
        dataframe = Frame(monster).grid(row = 0,column = 0)
        Label(dataframe,text = "加密/解密的数据".decode("GB2312"),width = 15).grid(row = 0,sticky = E)
        Entry(dataframe,textvariable = var1,width = 35).grid(row = 0,column = 1)
        Label(dataframe,text = "请输入Key".decode("GB2312"),width = 15).grid(row = 1,sticky = E)
        Entry(dataframe,textvariable = var2,width = 35).grid(row = 1,column = 1)
        Label(dataframe,text = "请输入IV".decode("GB2312"),width = 15).grid(row = 2,sticky = E)
        Entry(dataframe,textvariable = var3,width = 35).grid(row = 2,column = 1)
        Button(dataframe,text = "加密".decode("GB2312"),width = 10,command = lambda:self.DES_crypt("encode")).grid(row = 3,column = 0,sticky = W)
        Button(dataframe,text = "解密".decode("GB2312"),width = 10,command = lambda:self.DES_crypt("decode")).grid(row = 3,column = 1,sticky = E)
        Label(dataframe,text = "加密/解密的结果".decode("GB2312"),width = 15).grid(sticky = E)
        Entry(dataframe,textvariable = var4,width = 35).grid(row = 4,column = 1)
        Label(dataframe,text = "注意:key长度为8位".decode("GB2312"),width = 15).grid(row = 5,column = 0,sticky = W)
        Button(dataframe,text="退出".decode("GB2312"),width = 10,bg = '#B22222',fg = '#F5F5F5',command=monster.quit).grid(row = 5,column = 1,sticky = E) 
  
    def DES_crypt(self,choice):
        data = var1.get()
        if len(data) == 0:
            tkMessageBox.showerror("错误".decode("GB2312"),"请输入数据!".decode("GB2312"))
        des_key = var2.get()
        if len(des_key) == 0:
            des_key = b'0000000000000000'  #默认key
        if len(des_key) < 16 or len(des_key) > 24:
            tkMessageBox.showerror("错误".decode("GB2312"),"请输入8位key!".decode("GB2312"))
        else:
            des_key = var2.get()
        IV = var3.get()
        if len(IV) == 0:
            VI = "\0\0\0\0\0\0\0\0"
        if len(IV) < 8 or len(IV) > 8:
            tkMessageBox.showerror("错误".decode("GB2312"),"请输入8位IV!".decode("GB2312"))
        cipher = DES3.new(des_key,3,IV) #3代表CBC模式
        if choice == "encode": 
            en_result = cipher.encrypt(data)
            var4.set(en_result.encode("hex"))
        if choice == "decode":
            de_result = cipher.decrypt(data.decode("hex"))
            var4.set(de_result)

if __name__ == "__main__":
    win = Tk()
    win.title("Des加密/解密 author:monburan".decode("GB2312"))
    global var1,var2,var3,var4
    var1=StringVar()
    var2=StringVar()
    var3=StringVar()
    var4=StringVar()
    app = converter(win)
    win.mainloop()
