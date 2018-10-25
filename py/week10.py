from tkinter import *
w=Tk()
str=StringVar()
str.set( "Hello..." )
l=Label(w,textvariable=str)
l.pack()
def fun():
    str.set("Good bye...")
b=Button(w,text="Command",command=fun)
b.pack()
