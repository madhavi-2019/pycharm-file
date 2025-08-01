from tkinter import *
wm=Tk()
wm.title("calculater")
wm.geometry("300x300")
e=Entry(wm,width=50,borderwidth=5)
e.place(x=0,y=0)
#Button
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b1=Button(wm,text="1",width=5,command=lambda :click(1))
b2=Button(wm,text="2",width=5,command=lambda :click(2))
b3=Button(wm,text="3",width=5,command=lambda :click(3))
b4=Button(wm,text="4",width=5,command=lambda :click(4))
b5=Button(wm,text="5",width=5,command=lambda :click(5))
b6=Button(wm,text="6",width=5,command=lambda :click(6))
b7=Button(wm,text="7",width=5,command=lambda :click(7))
b8=Button(wm,text="8",width=5,command=lambda :click(8))
b9=Button(wm,text="9",width=5,command=lambda :click(9))
bx=Button(wm,text="0",width=5,command=lambda :click(0))
bc=Button(wm,text="clear",width=5,command=lambda :click(clear))

# Operators:
def add():
    n1=e.get()
    global math
    math ="addition"
    global i
    i=int(n1)
    e.delete(0,END)
bp=Button(wm,text="+",width=5,command=add)
def sub():
    n1=e.get()
    global math
    math ="subtraction"
    global i
    i=int(n1)
    e.delete(0,END)



bk=Button(wm,text="-",width=5,command=sub)
def mult():
    n1=e.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    e.delete(0,END)
bm=Button(wm,text="*",width=5,command=mult)
def div():
    n1=e.get()
    global math
    math="division"
    global i
    i=int(n1)
    e.delete(0,END)
bj=Button(wm,text="/",width=5,command=div)
def equal():
    n2=e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0,i+int(n2))
    elif math =="subtraction":
        e.insert(0, i - int(n2))
    elif math =="multiplication":
        e.insert(0,i*int(n2))
    elif math =="division":
        e.insert(0,i/int(n2))

bn=Button(wm,text="=",width=5,command=equal)


def clear():
    e.delete(0, END)

bc=Button(wm,text="clear",width=5,command=clear)
b1.place(x=10,y=40)
b2.place(x=50,y=40)
b3.place(x=90,y=40)
b4.place(x=10,y=80)
b5.place(x=50,y=80)
b6.place(x=90,y=80)
b7.place(x=10,y=120)
b8.place(x=50,y=120)
b9.place(x=90,y=120)
bx.place(x=10,y=170)
bp.place(x=50,y=170)
bk.place(x=90,y=170)
bm.place(x=10,y=210)
bj.place(x=50,y=210)
bn.place(x=90,y=210)
bc.place(x=10,y=260)
wm.mainloop()
