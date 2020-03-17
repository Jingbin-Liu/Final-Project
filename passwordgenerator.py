from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mBox
import random
def get_yn():
    global v
    p=v.get()
    return p
def msgBox_uncompletewrong():
    mBox.showerror('Error','Please enter the required password length!')
def msgBox_longwrong():
    mBox.showerror('Error','The total password length cannot be less than the sum of other parts!')
def msgBox_unvalidwrong():
    mBox.showerror('Error','Please enter an integer!')
def _msgBox():
    mBox.showinfo('Statement', 'This is the final project of the python class\nfor winter 2020. Coded by Liu Jingbin at UCSB')
def msg():
    win1=Tk()
    i='''***INTRODUCTION***
    You can use this program to randomly generate a password, 
    enter the total length of the password, the number of symbols,
    the number of numbers, whether you need capital letters or not,
    and then randomly generate the password.
    '''
    l2=Label(win1,text=i,anchor="nw",font=("Gabriola",20),fg="black")
    l2.grid(row=0,column=0,columnspan=2,rowspan=2)
    win1.mainloop()
def msgBox_succpc(p):
    pa=""
    for i in range (len(p)):
        pa=pa+p[i]
    mBox.showinfo('Congratulations', f'Your Password is   {pa}  Please remember it.If you are not satisfied, you can create a new one')
    pass
def passend(pa):
    msgBox_succpc(pa)
    pass
def creat(l,s,n,c):
    numb=[0]*n
    for i in range(n):
        nint=random.randint(0,9)
        ns=str(nint)
        numb[i]=ns
    symb=random.sample('!@#$%^&*()-+=[]}{/,.><',s)
    le=l-s-n
    wholepass=numb+symb
    if c==0:
        if le!=0:
            let=random.sample('abcdefghijklmnopqrstuvwxyz',le)
            wholepass=wholepass+let
    else:
        cln=random.randint(1,le)
        clnle=random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ',cln)
        slen=le-cln
        wholepass=wholepass+clnle
        if slen!=0:
            let=random.sample('abcdefghijklmnopqrstuvwxyz',slen)
            wholepass=wholepass+let
    random.shuffle(wholepass)
    passend(wholepass)
    pass
def generate(event):
    global lon,sym,num,cap
    global long_en,symb_en,num_en
    lon=long_en.get()
    sym=symb_en.get()
    num=num_en.get()
    cap=get_yn()
    if lon=="":
        msgBox_uncompletewrong()
    else:
        try:
            lon=int(lon)
            sym=int(sym)
            num=int(num)
            cap=int(cap)
            if lon<sym+num+cap:
                msgBox_longwrong()
            else:
                creat(lon,sym,num,cap)
        except:
            msgBox_unvalidwrong()
    pass
def show():
    win=Tk()
    photo1 = PhotoImage(file="C:\\Users\\刘景宾\\Desktop\\final\\1.png")
    photo2 = PhotoImage(file="C:\\Users\\刘景宾\\Desktop\\final\\2.png")
    win.title("PASSWORD GENERATOR")
    lf1=LabelFrame(win)
    lf1.grid(row=0,column=0,columnspan=6)
    lb1=Label(lf1,text="PASSWORD GENERATOR",font=("黑体",40),fg="white",compound=CENTER,image=photo1)
    lb1.grid(row=0,column=0,columnspan=6)
    lf2=LabelFrame(win,borderwidth=3)
    lf2.grid(row=1,rowspan=4,column=0,columnspan=6)
    lb2=Label(lf2,image=photo2)
    lb2.grid(row=1,rowspan=7,column=0,columnspan=6)
    lb3=Label(lf2,text="How long",font=("宋体",15),fg="black",bg="aliceblue")
    lb3.grid(row=2,column=1)
    lb4=Label(lf2,text="How many symbols",font=("宋体",15),fg="black",bg="aliceblue")
    lb4.grid(row=3,column=1)
    lb5=Label(lf2,text="How many numbers",font=("宋体",15),fg="black",bg="aliceblue")
    lb5.grid(row=4,column=1)
    lb7=Label(lf2,text="Do you need capital letter",font=("宋体",15),fg="black",bg="aliceblue")
    lb7.grid(row=6,column=1)
    global v
    v=IntVar()
    v.set(0)
    global long_en,symb_en,num_en
    long_en=ttk.Entry(lf2,width=20)
    long_en.grid(row=2,column=2)
    symb_en=ttk.Entry(lf2,width=20)
    symb_en.grid(row=3,column=2)
    num_en=ttk.Entry(lf2,width=20)
    num_en.grid(row=4,column=2)
    cap_check= Radiobutton(lf2, text="YES",bg="aliceblue",variable=v, value=1,command=get_yn)
    cap_check.grid(row=6,column=2,sticky=W)
    cap_check= Radiobutton(lf2, text="NO",bg="aliceblue",variable=v, value=0,command=get_yn)
    cap_check.grid(row=6,column=2,sticky=E)
    ttk.Style().configure("TButton",padding=6,relief="flat",background="cyan",foreground='aqua')
    genebt=ttk.Button(lf2,text="GENERATE")
    genebt.grid(row=7,column=1,sticky=E)
    me=Menu(win)
    meson=Menu(me)
    meson.add_command(label="Statement",command=_msgBox)
    meson.add_command(label="Introduction",command=msg)
    me.add_cascade(label="About",menu=meson)
    win["menu"]=me
    genebt.bind("<Button-1>",generate)
    win.mainloop()
    pass      
show()