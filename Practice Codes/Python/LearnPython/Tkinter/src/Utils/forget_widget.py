import tkinter as tk

def hide_button():
    button.pack_forget()

def show_button():
    button.pack()

root = tk.Tk()

button = tk.Button(root, text="Click me!")
button.pack()

hide_button_button = tk.Button(root, text="Hide Button", command=hide_button)
hide_button_button.pack()

show_button_button = tk.Button(root, text="Show Button", command=show_button)
show_button_button.pack()

root.mainloop()
