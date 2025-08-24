from tkinter import *

def printLabel(parent,var):
    temp_frame=Frame(parent)
    temp_frame.grid(row=1,column=0,columnspan=2)
    checklabel = Label(temp_frame,text=var.get(),bg='yellow',fg='black')
    checklabel.pack()
if __name__=='__main__':
    root = Tk()
    root.geometry('800x120')
    root.title('Checkboxes')
    root.config(bg='light gray',padx=10,pady=10)

    mainframe1 = Frame(root)
    mainframe1.config(relief='groove',padx=10,pady=10)
    mainframe2 = Frame(root)
    mainframe2.config(relief='groove',padx=10,pady=10)
    mainframe3 = Frame(root)
    mainframe3.config(relief='groove',padx=10,pady=10)
    
    var1 = IntVar() # To get/set values from/into the widgets.
    # Checkboxes return 0 or 1 based on their state.
    var1.set(0)
    c = Checkbutton(mainframe1,text="Wanna click this!",variable=var1,command=lambda:printLabel(mainframe1,var1))
    c.config(pady=10,bd=2,borderwidth=5,font=('Arial',12))
    c.grid(row=0,column=0)

    # Setting the variable to either on or off state. Checkboxes must return 'off' or 'on' based on their state. Put offvalue and onvalue as the arguments
    
    var2 = StringVar()
    c2 = Checkbutton(mainframe2,text="Wanna click this!",variable=var2,offvalue='off',onvalue='on')
    c2.config(pady=10,bd=2,borderwidth=5,font=('Arial',12))
    btn = Button(mainframe2,text='click me nigga',command=lambda:printLabel(mainframe2,var2))
    c2.grid(row=0,column=0)
    btn.grid(row=0,column=1)

    # By default 'variable' will be in null state, ie the value in var2='', thus the label may print empty string so set it to 'off' before using it.
    var3 = StringVar()
    var3.set('off')
    c3 = Checkbutton(mainframe3,text="Wanna click this!",variable=var3,offvalue='off',onvalue='on')
    c3.config(pady=10,bd=2,borderwidth=5,font=('Arial',12))
    btn = Button(mainframe3,text='click me nigga',command=lambda:printLabel(mainframe3,var3))
    c3.grid(row=0,column=0)
    btn.grid(row=0,column=1)

    mainframe1.grid(row=0,column=0,padx=10,pady=10,sticky='news') 
    mainframe2.grid(row=0,column=1,padx=10,pady=10,sticky='news')
    mainframe3.grid(row=0,column=2,padx=10,pady=10,sticky='news')

    root.mainloop()