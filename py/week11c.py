from tkinter import *
from tkinter import filedialog
import sys
str=None
def NewFile():
    print("New File!")
def OpenFile():
    global str
    name = filedialog.askopenfilename()
    print(name)
    f=open(name,"r")
    str=f.read()
    f.close()
def Save():
    f=open("xyz.txt","w")
    f.write(str)
    f.close()
def About():
    print("This is a simple example of a menu")
    
w = Tk()
menu = Menu(w)
w.config(menu=menu)
fm = Menu(menu)
menu.add_cascade(label="File", menu=fm)
fm.add_command(label="New", command=NewFile)
fm.add_command(label="Open...", command=OpenFile)
fm.add_command(label="Save", command=Save)
fm.add_separator()
fm.add_command(label="Exit", command=w.destroy)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
