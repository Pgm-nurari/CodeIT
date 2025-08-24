from tkinter import *
from tkinter import messagebox as msg

def get_button(parent,buttonName:str,method):
    btn = Button(parent,text=buttonName,command=method)
    btn.config(bg='#ff7f7f',fg='white',relief='flat')
    btn.pack(ipadx=30,pady=5)

def ShowInfo(title:str,text:str):
    msg.showinfo(title,text)

def ShowWarning(title:str,text:str):
    msg.showwarning(title,text)

def ShowError(title : str, text : str):
    msg.showerror(title,text)

def AskQuestion(title : str, text : str):
    user_response = msg.askquestion(title,text) 
    print(user_response,type(user_response))
    #* Returns [yes/no] in strings

def OkCancel(title : str, text : str):
    user_response = msg.askokcancel(title,text) 
    print(user_response,type(user_response))
    #* Returns [True/False] in strings

def YesNoBox(title : str, text : str):
    user_response = msg.askyesno(title,text) 
    print(user_response,type(user_response))
    #* Returns [True/False] in strings

def RetryBox(title : str, text : str):
    user_response = msg.askretrycancel(title,text)          
    print(user_response,type(user_response))
    #* Returns [True/False] in strings

""" 
#?  To get the values of the key pressed in the messageboxes, simply pass the statement 'messagebox.askokcancel(title,text)' into a variable!
"""

if __name__=='__main__':
    root=Tk()
    root.title('Messagebox')
    root.geometry('368x278')
    root.resizable(False,False)
    root.config(padx=10,pady=10,bg='red')

    mainframe=Frame(root,bg='yellow')
    mainframe.pack(fill='both',expand=True)

    get_button(mainframe,"Info Box",lambda: ShowInfo("Messageboxes : information","Do you know this message box is used for showing information!"))

    get_button(mainframe,"Warning Box",lambda: ShowWarning("Messagebox : warning box","Do not press that button again!"))

    get_button(mainframe,"Error Box",lambda: ShowError("Messagebox : Error","You have pressed the wrong Button"))

    get_button(mainframe,"Questioning Box",lambda: AskQuestion("Messagebox : question", "Are you sure?"))

    get_button(mainframe,"Ok/Cancel Box",lambda: OkCancel("Messagebox : ok-cancel", "Want to continue?"))

    get_button(mainframe,"Yes/No Box",lambda: YesNoBox("Messagebox : yes-no", "Find the value?"))
    
    get_button(mainframe,"Retry/Cancel Box",lambda: RetryBox("Messagebox : retry-cancel", "Try again?"))

    root.mainloop()