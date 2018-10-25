from tkinter import *
w=Tk()
f=Frame(width=300,height=400)
f.pack()
f.propagate(0)
mpos=StringVar()
def MPr(event):
      mpos.set( "Pressed at " + str( event.x ) + ", " + str( event.y ))
def MRel(event):
      mpos.set( "Released at" + str( event.x ) + ", " + str( event.y ))
def MEnt(event):
      mpos.set( "Mouse in window" )

def Mexit( event ):
      mpos.set( "Mouse outside window" )

def MDrag(event ):
      mpos.set( "Dragged at " + str( event.x ) + ", " + str( event.y ))
mpos.set("Mouse outside window")
l=Label(f,textvariable=mpos)
l.pack()
f.bind( "<Button-1>",MPr)
f.bind( "<ButtonRelease-1>",MRel)   
f.bind( "<Enter>", MEnt)
f.bind( "<Leave>", Mexit )
f.bind( "<B1-Motion>",MDrag )
mainloop()

