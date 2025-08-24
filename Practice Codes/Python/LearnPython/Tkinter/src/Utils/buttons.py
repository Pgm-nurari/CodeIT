from tkinter import *

if __name__=='__main__':
    app=Tk()
    app.geometry('300x200')
    app.resizable(False,False)

    btn1 = Button(app,text='Click here')
    btn1.pack()
    btn3 = Button(app,text='Hello',command=lambda:show_text(btn3))
    
    def change_color(button : Button):
        button.config(bg="light gray",fg="black",text="color changed")
        btn3.pack()
    def show_text(button: Button):
        btxt = Label(app,text = btn3.cget('text')).pack()


    btn2 = Button(app,text='Color change!',command=lambda : change_color(btn2),padx=30)
    btn2.pack()

    exit_button = Button(app,text="Exit!",command=app.quit).pack()

    app.mainloop()
    pass