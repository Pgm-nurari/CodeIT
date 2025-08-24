import os
from tkinter import *
from tkinter import filedialog

class App:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x450')
        self.root.title('.txtReader')
        self.text_to_display = StringVar()

        self.layout()

        self.root.mainloop()

    def get_data(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            try:
                with open(file_path,'r',encoding='utf-8') as file_header:
                    self.text_to_display = file_header.read()
                self.displayer.insert(END,self.text_to_display)
                self.displayer.grid(row=1,column=0,columnspan=5,padx=10,pady=10,sticky='news')
            except:
                raise Exception
    
    def layout(self):
        self.root.config(bg='light gray')

        self.file_button = Button(self.root,text='Select File',command=self.get_data)
        self.file_button.config(relief = FLAT, padx=10)

        self.displayer = Text(self.root,height=25,width=50,wrap='word')

        self.scrollbar = Scrollbar(self.root,command=self.displayer.yview)

        self.file_button.grid(row=0,column=2,padx=10,pady=10)
        # self.displayer.grid(row=1,column=0,columnspan=5,padx=10,pady=10,sticky='news)
        
if __name__=='__main__':
    window = App()