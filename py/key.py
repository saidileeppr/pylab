from tkinter import *

root = Tk()

def key(event):
    print("press"+repr(event.char))
def keyr(event):
    print("keyrel")
def keypr(event):
    print("keypres")


def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Shift Up>", keyr)
frame.bind("<KeyPress>", keypr)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
