""" 
There are 2 frame widgets: i) Frame and ii) LabelFrame
"""
from tkinter import *

if __name__=='__main__':
    app = Tk()
    app.config(bg="sky blue",padx=100,pady=100)
    
    frame = Frame(app,bg="orange",padx=10,pady=10,border=1,borderwidth=10)
    frame.grid(row=0,column=0)
    
    for _ in range(10):
        text = Label(frame,text="This is a frame widget!",anchor='nw')
        text.pack(fill="both")

    Lframe = LabelFrame(app,text="This is a Labeled Frame!",bg="yellow",padx=10,pady=10,bd=1,borderwidth=5)
    Lframe.grid(row=1,column=0)

    for i in range(10):
        text = Label(Lframe,text="This is a labeled frame widget!",anchor='nw')
        text.grid(row=i,column=0)

    app.rowconfigure(0,weight=1)
    app.columnconfigure(0,weight=1)
    app.rowconfigure(1,weight=1)
    

    app.mainloop()