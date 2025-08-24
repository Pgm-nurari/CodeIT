import tkinter as tk

def create_layout(root):
    # Create a top frame
    top_frame = tk.Frame(root, bg='lightgrey', borderwidth=2, relief="solid")
    top_frame.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Top Frame: 3 equally spaced widgets with padding only on specific sides
    top_left = tk.Label(top_frame, text="Top Left", bg='red', borderwidth=2, relief="solid")
    top_middle = tk.Label(top_frame, text="Top Middle", bg='green', borderwidth=2, relief="solid")
    top_right = tk.Label(top_frame, text="Top Right", bg='blue', borderwidth=2, relief="solid")
    
    # Apply external padding and internal padding
    top_left.pack(side='left', fill='both', expand=True, padx=(0, 10), pady=10, ipadx=20, ipady=10)   # padding on right side only
    top_middle.pack(side='left', fill='both', expand=True, padx=(10, 10), pady=10, ipadx=20, ipady=10) # padding on both sides
    top_right.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=10, ipadx=20, ipady=10)  # padding on left side only

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x500')
    create_layout(root)
    root.mainloop()
