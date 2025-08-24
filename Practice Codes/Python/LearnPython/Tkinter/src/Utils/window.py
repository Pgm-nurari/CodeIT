from tkinter import *

def print_window_dimensions():
    width = app.winfo_width()
    height = app.winfo_height()
    print(f"Current dimensions: {width}x{height}")

def print_requested_dimensions():
    req_width = app.winfo_reqwidth()
    req_height = app.winfo_reqheight()
    print(f"Requested dimensions: {req_width}x{req_height}")

def print_dimensions(root):
    # Create a button to print the current window dimensions
    button1 = Button(app, text="Print Current Dimensions", command=print_window_dimensions)
    button1.pack(pady=10)
    
    # Create a button to print the requested window dimensions
    button2 = Button(app, text="Print Requested Dimensions", command=print_requested_dimensions)
    button2.pack(pady=10)



if __name__=='__main__':
    app=Tk()
    app.title('Window')
    app.geometry('252x135')
    app.resizable(True,True)
    app.minsize(width=252,height=135)
    # app.maxsize(width=400,height=200)
    # app.iconbitmap('Assets/imgLogo.ico') #? This is the app icon on the title bar

    print_dimensions(app)

    exit_btn = Button(app,text='click to exit the program!',command=app.quit)
    exit_btn.config(fg='white',bg='#ff7f7f',relief = 'flat')
    exit_btn.pack()

    app.mainloop()