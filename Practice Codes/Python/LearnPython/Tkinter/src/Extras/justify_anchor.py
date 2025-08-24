import tkinter as tk

if __name__=='__main__':
    root = tk.Tk()

    # Create a label with a large width and height
    label = tk.Label(root, text="Hello, Tkinter!", bg="lightgrey", width=20, height=10, anchor='nw')
    label.pack()

    # Create a label with multiple lines of text and justify set to center
    label = tk.Label(root, text="Hello, Tkinter!\nThis is a test of the justify attribute.\nThe lines should be centered.", bg="lightgrey", justify='center')
    label.pack()

    # Create a label with anchor and justify attributes
    label = tk.Label(root, text="Hello, Tkinter!\nThis is a test of the justify attribute.\nThe lines should be centered.", bg="lightgrey", width=20, height=10, anchor='s', justify='center')
    label.pack()

    root.mainloop()