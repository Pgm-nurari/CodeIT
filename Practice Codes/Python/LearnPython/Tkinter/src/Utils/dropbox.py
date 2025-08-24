from tkinter import *

def display_option_selected(selection):
    displayer.config(text=selection)

if __name__ == '__main__':
    root = Tk()
    root.geometry('252x135')
    root.title('Drop Boxes')

    states_list = [
        'Kerala',
        'Tamil Nadu',
        'Uttar Pradesh'
    ]
    
    Option_selected = StringVar()
    Option_selected.set(states_list[0])
    displayer = Label(root, text='Select an option', padx=10)

    dropbox = OptionMenu(root, Option_selected, *states_list, command=lambda x: display_option_selected(Option_selected.get()))
    # By default the OptionMenu passes the selected option in the command section. Hence lambda needs 'x' as its positional argument.
    dropbox.pack(anchor=CENTER, fill='x', expand=True)

    displayer.pack(anchor=CENTER, fill='x', expand=True)
    
    root.mainloop()
