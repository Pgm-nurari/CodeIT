import tkinter as tk

def update_status_bar(root, statusbar):
    #? Get the current dimensions of the window
    width = root.winfo_width()
    height = root.winfo_height()
    statusbar.config(text=f"Window size: {width}x{height}")
    #! Schedule this function to run again after 100 milliseconds
    root.after(100, update_status_bar, root, statusbar)

def create_status_bar(root):
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    
    frame1.grid(row=0, column=0, sticky='nsew')
    frame2.grid(row=1, column=0, sticky='ew')
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=0)
    root.grid_columnconfigure(0, weight=1)
    
    menubar = tk.Label(frame1, background='sky blue', border=1, relief='flat', width=30, height=25)
    menubar.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    
    content = tk.Label(frame1, background="green", border=1, relief='flat', width=45, height=25)
    content.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
    
    frame1.grid_rowconfigure(0, weight=1)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)
    
    statusbar = tk.Label(frame2, text="This is a status bar!", anchor='w', bd=1, relief='sunken')
    statusbar.grid(row=0, column=0, sticky='ew')
    
    frame2.grid_columnconfigure(0, weight=1)
    update_status_bar(root, statusbar)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x500')
    root.minsize(width=197,height=33)
    create_status_bar(root)
    root.mainloop()

