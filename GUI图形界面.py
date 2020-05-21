# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:04:12 2020

@author: 30509
"""

from tkinter import *
import json

#定义类
class majorList:
    def __init__(self,department1="",department2="",major="",target=""):
        self.d1=department1
        self.d2=department2
        self.m=major
        self.t=target
    def setList1(self,department1):
        self.d1=department1
    def setList2(self,department2):
        self.d2=department2
    def search1(self,department1):
        if self.d1 in L1:
            a=t1[self.d1]
            for m in a:
                print(m)
        else:
            print("未找到相关招生单位，请重新输入！")
        #entry1.delete(0,END)
        department1=""
    def search2(self,department1):
        if self.d1 in L2:
            print(t2[self.d1])
        else:
            print("未找到相关招生单位，请重新输入！")
        #entry1.delete(0,END)
    def search3(self,department1):
        if self.d1 in L3:
            print(t3[self.d1])
        else:
            print("未找到相关招生单位，请重新输入！")
        #entry1.delete(0,END)
    def search4(self,department1):
        if self.d1 in L4:
            print(t4[self.d1])
        else:
            print("未找到相关招生单位，请重新输入！")
        #entry1.delete(0,END)  
    def search5(self,department2):
        if self.d2 in L5:
            print("网址为："+t5[self.d2])
        else:
            print("未找到相关招生专业，请重新输入！")
#定义相关函数
def Search1():
    department1=entry1.get()
    a1.setList1(department1)
    if department1=="":
       print("请输入单位编号和单位名称,例（(101)中国语言文学系）：")
       return
    else:
        a1.search1(department1)
def Search2():
    department1=entry1.get()
    a1.setList1(department1)
    if department1=="":
       print("请输入单位编号和单位名称,例（(101)中国语言文学系）：")
       return
    else:
        a1.search2(department1)
def Search3():
    department1=entry1.get()
    a1.setList1(department1)
    if department1=="":
       print("请输入单位编号和单位名称,例（(101)中国语言文学系）：")
       return
    else:
        a1.search3(department1)
def Search4():
    department1=entry1.get()
    a1.setList1(department1)
    if department1=="":
       print("请输入单位编号和单位名称,例（(101)中国语言文学系）：")
       return
    else:
        a1.search4(department1)
def Search5():
    department2=entry2.get()
    a1.setList2(department2)
    if department2=="":
       print("请输入专业编号和专业名称,例（(071400)统计学）：")
       return
    else:
        a1.search5(department2)
        
with open ("华东师范大学2020年硕士研究生招生专业目录.json","r") as f:
    t1=json.load(f)
    L1=list(t1.keys())
with open("简介.json","r") as g:
    t2=json.load(g)
    L2=list(t2.keys())
with open("特色.json","r") as h:
    t3=json.load(h)
    L3=list(t3.keys())
with open("团队.json","r") as j:
    t4=json.load(j)
    L4=list(t4.keys())   
with open("招生专业网址.json","r") as k:
    t5=json.load(k)
    L5=list(t5.keys())  
    
window=Tk()
window.geometry("550x400")
window.title("华东师范大学2020年硕士研究生招生专业简易查询系统")

#GUI布局
frm1=Frame(window)
frm1.grid()

lbl=Label(frm1,text="华东师范大学2020年硕士研究生招生专业简易查询系统",width=50)
lbl.grid(row=1,column=0,columnspan=4)

lbl1=Label(frm1,text="请输入单位编号和单位名称,例（(101)中国语言文学系）：",width=45)
lbl1.grid(row=2,column=0,columnspan=2)
entry1=Entry(frm1,width=30)
entry1.grid(row=2,column=2,columnspan=2)

btn1 = Button(frm1,width=10,text="下属专业", command=Search1) 
btn1.grid(row=3,column=0)
btn2 = Button(frm1,width=10,text="单位简介", command=Search2) 
btn2.grid(row=3,column=1)
btn3 = Button(frm1,width=10,text="单位特色", command=Search3) 
btn3.grid(row=3,column=2)
btn4 = Button(frm1,width=10,text="单位团队", command=Search4) 
btn4.grid(row=3,column=3)

lbl2=Label(frm1,text="请输入专业编号和专业名称,例（(071400)统计学）       ：",width=45)
lbl2.grid(row=4,column=0,columnspan=2)
entry2=Entry(frm1,width=30)
entry2.grid(row=4,column=2,columnspan=2)
btn5 = Button(frm1,width=10,text="专业网址", command=Search5) 
btn5.grid(row=5,column=0,columnspan=4)

a1=majorList()
window.mainloop()
    