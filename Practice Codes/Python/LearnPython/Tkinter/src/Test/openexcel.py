import tkinter as tk
from tkinter import filedialog, scrolledtext
import pandas as pd

def open_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        # Read the Excel file
        df = pd.read_excel(file_path)
        # Clear the text widget
        text_widget.delete(1.0, tk.END)
        # Insert DataFrame content into the text widget
        text_widget.insert(tk.END, df.to_string())

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Open Excel File')
    root.geometry('600x400')

    open_button = tk.Button(root, text="Open Excel File", command=open_excel_file)
    open_button.pack(pady=10)

    text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    text_widget.pack(expand=True, fill='both', padx=10, pady=10)

    root.mainloop()
