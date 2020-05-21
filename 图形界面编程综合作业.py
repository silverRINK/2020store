from tkinter import *
import tkinter.messagebox

#定义类
class moneyList:
    def __init__(self,month="",money=0):
        self.time=month
        self.balance=money
        self.income=0
        self.outcome=0
    def setList(self,month,money):
        self.time=month
        self.balance=money
    def calculate(self,month,money):
        self.balance+=i
        self.balance-=o
        self.time=month
        self.income+=i
        self.outcome+=o
        if self.balance < 0:
            self.balance=self.balance*(-1)
            messagebox.showinfo(title=self.time+"月账单",message="您本月收入为"+str(self.income)+"元\n"+"支出为"+str(self.outcome)+"元\n"+"很遗憾，本月你多支出"+str(self.balance)+"元")
        elif self.balance == 0:
            messagebox.showinfo(title=self.time+"月账单",message="您本月收入为"+str(self.income)+"元\n"+"支出为"+str(self.outcome)+"元\n"+"本月收支平衡")
        else:
            messagebox.showinfo(title=self.time+"月账单",message="您本月收入为"+str(self.income)+"元\n"+"支出为"+str(self.outcome)+"元\n"+"恭喜您，本月您结余"+str(self.balance)+"元")
        entry2.delete(0,END)
        entry3.delete(0,END)
    def clear(self):
        entry1.delete(0,END)
        self.income=0
        i=0
        o=0
        self.outcome=0
        money=0
        self.balance=0

#定义相关函数
def Start():
    month=entry1.get()
    if month=="":
        messagebox.showinfo(title="欢迎使用本程序",message="请输入您记账的月份！")
        return
    else:
        messagebox.showinfo(title="欢迎使用本程序",message="您已设定月份，快来记账吧！")
    a1.setList(month,money)

def Clear():
    a1.clear()
    messagebox.showinfo(title="数据已清除",message="数据已清空，快来记账吧！")
    
def About():
    messagebox.showinfo(title="关于本程序",message="本程序仅为实验设计，仍存在许多不足，感谢您的使用！")

def Calculate():
    money=0
    month=entry1.get()
    global i
    if i =="":
        i=0
    else:
        i=float(entry2.get())
    global o
    if o =="":
        o=0
    else:
        o=float(entry3.get())
    a1.calculate(month,money)
    
window=Tk()
window.geometry("350x150")
window.title("模拟记账")

#GUI布局
lbl=Label(window,text="使用本程序前，请先输入您记账的月份，谢谢合作",width=50)
lbl.grid()

frm1=Frame(window)
frm1.grid()

entry1 = Entry(frm1,width=15)
entry1.grid(row=1,column=1)
entry2 = Entry(frm1,width=15)
entry2.grid(row=2,column=1)
entry3 = Entry(frm1,width=15)
entry3.grid(row=3,column=1)

lbl1=Label(frm1,text="请输入记账月份：",width=15)
lbl1.grid(row=1,column=0)
lbl2=Label(frm1,text="请输入本月收入：",width=15)
lbl2.grid(row=2,column=0)
lbl3=Label(frm1,text="请输入本月支出：",width=15)
lbl3.grid(row=3,column=0)
lbl4=Label(frm1,text="月",width=5)
lbl4.grid(row=1,column=2)
lbl5=Label(frm1,text="元",width=5)
lbl5.grid(row=2,column=2)
lbl6=Label(frm1,text="元",width=5)
lbl6.grid(row=3,column=2)

btn1 = Button(window,width=10,text="计算结余", command=Calculate) 
btn1.grid()

#设计菜单栏
menubar=Menu(window)
filemenu=Menu(menubar)
filemenu.add_command(label="开始记账",command=Start)
filemenu.add_separator()
filemenu.add_command(label="清除数据",command=Clear)
filemenu.add_separator()
filemenu.add_command(label="退出程序",command=window.destroy)
menubar.add_cascade(label="开始",menu=filemenu)
helpmenu=Menu(menubar)
helpmenu.add_command(label="关于",command=About)
menubar.add_cascade(label="帮助",menu=helpmenu)
window.config(menu=menubar)

a1=moneyList()
window.mainloop( )
