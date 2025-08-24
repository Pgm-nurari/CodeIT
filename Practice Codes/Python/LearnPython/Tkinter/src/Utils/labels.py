""" Labels in tkinter module """
import tkinter as tk

if __name__=='__main__':
    root = tk.Tk()
    root.title('Labels')
    root.geometry('300x200')
    root.minsize()
    f1=tk.Frame(root).grid()

    l1 = tk.Label(f1,text='This is label 1\n...').grid(row=0,column=0)
    #l1.pack()
    word = input("Enter something: ")
    l2 = tk.Label(f1,text = word)
    l2.configure(bg="light blue",fg="dark blue",padx=30,pady=5,relief="sunken")
    l2.grid(row=1,column=0)
    l3 = tk.Label(f1,text = word)
    l3.configure(bg="light blue",fg="dark blue",padx=30,pady=5,relief="flat")
    l3.grid(row=2,column=0)
    l4 = tk.Label(f1,text = word)
    l4.configure(bg="light blue",fg="dark blue",padx=30,pady=5,relief="groove")
    l4.grid(row=3,column=0)
    l5 = tk.Label(f1,text = word)
    l5.configure(bg="light blue",fg="dark blue",padx=30,pady=5,relief="raised")
    l5.grid(row=4,column=0)    
    print(root.minsize())  
    root.mainloop()