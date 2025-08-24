from tkinter import *
from tkinter import filedialog

def select_files():
    global common_path
    file_list:list = filedialog.askopenfilenames()
    common_path = '/'.join(str(file_list[0]).split('/')[0:-1:1])
    for i in file_list:
        l=str(i).split('/')
        lists.insert('end',l[-1])
    delete_item_button.config(state = 'active')
    display_file_address.config(state = 'active')

def delete_item():
    lists.delete('anchor')

def display_address():
    global common_path
    file_name = str(lists.get('anchor'))
    address = '/'.join([common_path,file_name])
    address_label.config(text=address)

if __name__=='__main__':
    print("This is a list box program")
    common_path=''

    app=Tk()
    app.title('List Box Window')
    app.resizable(True,True)
    app.minsize(width=252,height=135)
    app.config(bg='light gray',padx=50,pady=10)
   
    lists = Listbox(app)
    Scroller = Scrollbar(app,orient='vertical',command=lists.yview)
    lists.config(activestyle='underline',cursor='hand2',width=40,yscrollcommand=Scroller.set)
    lists.pack(padx=10,pady=10,ipady=10)

    address_label = Label(app,text='select a file name from the list!')
    address_label.pack(pady=10)

    choose_file_button = Button(app,text='Chose files',command=select_files)
    delete_item_button = Button(app,text='Delete Selected',command=delete_item,state='disabled')
    display_file_address = Button(app,text='show address',command = display_address,state='disabled')

    choose_file_button.pack(pady=10)
    delete_item_button.pack(pady=10)
    display_file_address.pack(pady=10)

    print(common_path)
    app.mainloop()