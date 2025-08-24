import tkinter as tk
from tkinter import font

def heading(parent,text:str):
    label1 = tk.Label(parent,text=text,justify='left',font=font.Font(underline=True,size=10))
    label1.pack(anchor='nw')

def print_value(parent,variable):
   display_value = tk.Label(parent,text=variable,justify='left')
   display_value.pack(anchor='w')

def display_button(parent,temp_variable):
    btn = tk.Button(parent,text="Display",command=lambda: print_value(parent,temp_variable.get()))
    btn.config(relief='flat',border=1,borderwidth=2,background='#ff7f7f',foreground='white')
    btn.pack(anchor='w',expand=True,fill='x')

def radio_without_loop(parent):
    temp=tk.IntVar()
    temp.set(0)
    tk.Radiobutton(parent,text='Option 1',variable=temp,value=1).pack(anchor='w')
    tk.Radiobutton(parent,text='Option 2',variable=temp,value=2).pack(anchor='w')
    tk.Radiobutton(parent,text='Option 3',variable=temp,value=3).pack(anchor='w')
    tk.Radiobutton(parent,text='Option 4',variable=temp,value=4).pack(anchor='w')
    tk.Radiobutton(parent,text='Option 5',variable=temp,value=5).pack(anchor='w')
    display_button(parent,temp)

def radio_with_loop(parent):
    radio_list=[
        ('Option 1',"One"),
        ('Option 2',"Two"),
        ('Option 3',"Three"),
        ('Option 4',"Four"),
        ('Option 5',"Five")
    ]
    temp_string=tk.StringVar()
    temp_string.set("Select an Option!")
    for rDisplay,rValue in radio_list:
        tk.Radiobutton(parent,text=rDisplay,variable=temp_string,value=rValue).pack(anchor='w')
    display_button(parent,temp_string)

if __name__=='__main__':
    app = tk.Tk()
    app.title('Radio Buttons')
    app.resizable(False, False)
    app.config(padx=10,pady=10)
    
    frame1 = tk.LabelFrame(app,text="Radio Button 1",padx=10,pady=10,width=150,height=200)
    frame2 = tk.LabelFrame(app,text="Radio Button 2",padx=10,pady=10,width=150,height=200)

    frame1.grid(row=0,column=0)
    frame2.grid(row=0,column=1)

    heading(frame1,text="Radio Buttom without For Loop")
    heading(frame2,"Radio Buttom using For Loop")

    radio_without_loop(frame1)
    radio_with_loop(frame2)

    app.mainloop()