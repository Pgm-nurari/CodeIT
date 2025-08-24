""" Explore the entry widget """
from tkinter import *

def show(textbox : Entry, parent: Frame) -> None:
    labl=Label(parent,text=textbox.get())
    labl.grid(row=1,column=0)

def show_password(pwrdtext : Entry, btn3:Button) -> None:
    if pwrdtext.cget('show')=='*':
        pwrdtext.config(show='')
        btn3.config(text='Hide Password')
    else:
        pwrdtext.config(show='*')
        btn3.config(text='Show Password')

if __name__=='__main__':
    app = Tk()
    app.title('Entry Widget')
    app.geometry('400x300')
    app.config(bg='sky blue')
    
    # FRAME 1
    frame1 = LabelFrame(master = app,text='Showing the text in ENTRY')
    text1 = Entry(frame1,bd=-1,width=30,relief='solid',border=1)
    btn1 = Button(frame1,text='Click here!')

    text1.insert(0,'Enter something here')
    text1.insert(END, 'End of the Entry')
    btn1.config(command=lambda : show(text1,frame1),relief='flat',bg='sky blue',fg='dark blue')

    frame1.pack(fill='x',expand=True)
    text1.grid(row=0,column=0,padx=10,pady=5)
    btn1.grid(row=0,column=1,padx=10,pady=5)

    # FRAME 2
    frame2 = LabelFrame(master = app,text='Hide/Show Password',bg='magenta',height=300,width=300)
    pwrdLabel = Label(master = frame2,text="Password: ")
    pwrdtext = Entry(master = frame2,width=10,show='*')
    btn3 = Button(master = frame2,text='Show Password')

    btn3.config(command = lambda:show_password(pwrdtext,btn3))

    frame2.pack(fill='both')
    pwrdLabel.grid(row=0, column=0, padx=5,pady=5)
    pwrdtext.grid(row=0, column=1, padx=5,pady=5)
    btn3.grid(row=0, column=2, padx=5,pady=5)

    # FRAME 3
    frame3 = LabelFrame(master = app, text='Clear the ENTRY')
    text2 = Entry(frame3,width=20)
    btn2 = Button(frame3,text='Clear Entry')

    text2.insert(0,'Press the button to clear this text in Entry!')
    btn2.config(command=lambda:text2.delete(0,END))

    frame3.pack(fill='x',expand=True)
    text2.grid(row=0,column=0,padx=10,ipadx=10)
    btn2.grid(row=0,column=1,padx=10)

    app.mainloop()