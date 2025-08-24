import tkinter as tk

def create_layout(root):
    # Create main frames
    top_frame = tk.Frame(root, bg='lightgrey', borderwidth=2, relief="solid")
    bottom_frame = tk.Frame(root, bg='white', borderwidth=2, relief="solid")
    
    top_frame.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
    bottom_frame.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
    
    # Configure grid layout for root window
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=3)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Top Frame: 3 equally spaced widgets with colors
    top_left = tk.Label(top_frame, text="Top Left", bg='red', borderwidth=2, relief="solid")
    top_middle = tk.Label(top_frame, text="Top Middle", bg='green', borderwidth=2, relief="solid")
    top_right = tk.Label(top_frame, text="Top Right", bg='blue', borderwidth=2, relief="solid")
    
    top_left.pack(side='left', fill='both', expand=True, padx=10, pady=10)
    top_middle.pack(side='left', fill='both', expand=True, padx=10, pady=10)
    top_right.pack(side='left', fill='both', expand=True, padx=10, pady=10)

    # Bottom Frame: left and right sections
    left_frame = tk.Frame(bottom_frame, bg='lightblue', borderwidth=2, relief="solid")
    right_frame = tk.Frame(bottom_frame, bg='lightgreen', borderwidth=2, relief="solid")
    
    left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
    right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)
    
    # Left Frame: 3x2 grid of widgets with colors
    for i in range(3):
        for j in range(2):
            label = tk.Label(left_frame, text=f"Item {i*2 + j + 1}", bg='yellow', borderwidth=2, relief="solid")
            label.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
    
    # Configure grid layout for left frame
    for i in range(3):
        left_frame.grid_rowconfigure(i, weight=1)
    for j in range(2):
        left_frame.grid_columnconfigure(j, weight=1)
    
    # Right Frame: complex layout with packed widgets with colors
    inner_frame1 = tk.Frame(right_frame, bg='orange', borderwidth=2, relief="solid")
    inner_frame2 = tk.Frame(right_frame, bg='purple', borderwidth=2, relief="solid")
    
    inner_frame1.pack(side='left', fill='both', expand=True, padx=5, pady=5)
    inner_frame2.pack(side='left', fill='both', expand=True, padx=5, pady=5)
    
    # Adding widgets to inner frames with colors
    inner_label1 = tk.Label(inner_frame1, text="Inner 1", bg='pink', borderwidth=2, relief="solid")
    inner_label2 = tk.Label(inner_frame1, text="Inner 2", bg='cyan', borderwidth=2, relief="solid")
    
    inner_label1.pack(side='top', fill='both', expand=True, padx=5, pady=5)
    inner_label2.pack(side='bottom', fill='both', expand=True, padx=5, pady=5)
    
    inner_label3 = tk.Label(inner_frame2, text="Inner 3", bg='lightcoral', borderwidth=2, relief="solid")
    inner_label4 = tk.Label(inner_frame2, text="Inner 4", bg='lightseagreen', borderwidth=2, relief="solid")
    inner_label5 = tk.Label(inner_frame2, text="Inner 5", bg='lightgoldenrodyellow', borderwidth=2, relief="solid")
    
    inner_label3.pack(side='top', fill='both', expand=True, padx=5, pady=5)
    inner_label4.pack(side='top', fill='both', expand=True, padx=5, pady=5)
    inner_label5.pack(side='bottom', fill='both', expand=True, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x500')
    create_layout(root)
    root.mainloop()
