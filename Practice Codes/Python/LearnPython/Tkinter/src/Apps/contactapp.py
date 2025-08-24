from tkinter import *
import os

class ContactApp:

    def __init__(self):
        self.root = Tk()
        
        self.initials()
        self.layout()

        self.root.mainloop()

    def initials(self):
        self.root.title('Contact App')
        self.root.iconbitmap(os.path.join(os.getcwd(),'Assets','imgLoco.ico'))
        self.root.geometry('700x400')
        self.root.minsize(width=700,height=400)

        # Get Menu Bar...
        """ menubar = Menu(self.root)

        filemenu = Menu(menubar,tearoff = 0, type = 'tearoff') 
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open File')
        filemenu.add_command(label='Open Folder')
        filemenu.add_command(label='Save File')
        filemenu.add_separator()
        filemenu.add_command(label='Exit',command=self.root.quit)
        menubar.add_cascade(label='File',menu=filemenu)


        self.root.config(menu=menubar) """

    def layout(self):
        mainframe = Frame(self.root)
        mainframe.pack(fill='both',expand=True)

        frame1 = Frame(mainframe)
        frame1.config(width=200,height=400,bg='sky blue')
        frame1.grid(row=0,column=0,sticky='nsw',padx=(5,10),pady=(0,5))

        frame2 = Frame(mainframe)
        frame2.config(width=500,height=400,bg='green')
        frame2.grid(row=0,column=1,sticky='nsew',padx=(0,5),pady=(0,5),columnspan=2)

        mainframe.grid_rowconfigure(0,weight=1)
        mainframe.grid_columnconfigure(1,weight=2)

def main():
    app = ContactApp()

if __name__=='__main__':
    main()