import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from creator import CSVDataCreator
from csv_viewer import CSVDataLoader
import matplotlib.pyplot as plt


class CSVEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV DataFrame Editor")
        self.style = Style(theme="darkly")  # Apply dark theme

        self.creator = CSVDataCreator()
        self.file_path = None

        self.build_gui()

    def build_gui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill='both')

        self.create_tab = ttk.Frame(self.notebook)
        self.load_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.create_tab, text='Create CSV')
        self.notebook.add(self.load_tab, text='Load CSV')

        self.build_create_tab()
        self.build_load_tab()

    def build_create_tab(self):
        ttk.Label(self.create_tab, text="Column Names (comma separated):").pack(pady=5)
        self.columns_entry = ttk.Entry(self.create_tab, width=50)
        self.columns_entry.pack()

        ttk.Label(self.create_tab, text="Row Data (one row per line, comma-separated values):").pack(pady=5)
        self.data_text = tk.Text(self.create_tab, height=10, width=60, bg="#1e1e1e", fg="white", insertbackground="white")
        self.data_text.pack()

        ttk.Button(self.create_tab, text="Create DataFrame", command=self.create_dataframe).pack(pady=5)
        ttk.Button(self.create_tab, text="Save to CSV", command=self.save_csv).pack(pady=2)
        ttk.Button(self.create_tab, text="Export to Excel", command=self.save_excel).pack(pady=2)
        ttk.Button(self.create_tab, text="Update Cell", command=self.update_cell_popup).pack(pady=2)
        ttk.Button(self.create_tab, text="Insert Row", command=self.insert_row_popup).pack(pady=2)
        ttk.Button(self.create_tab, text="Insert Column", command=self.insert_col_popup).pack(pady=2)
        ttk.Button(self.create_tab, text="Delete Row", command=self.delete_row_popup).pack(pady=2)
        ttk.Button(self.create_tab, text="Delete Column", command=self.delete_col_popup).pack(pady=2)
        ttk.Button(self.create_tab, text="Show Dashboard", command=self.show_dashboard).pack(pady=10)


        self.create_output = tk.Text(self.create_tab, height=10, width=80, bg="#1e1e1e", fg="white", insertbackground="white")
        self.create_output.pack(pady=5)

    def build_load_tab(self):
        ttk.Button(self.load_tab, text="Load CSV File", command=self.load_csv).pack(pady=5)
        self.load_output = tk.Text(self.load_tab, height=15, width=80, bg="#1e1e1e", fg="white", insertbackground="white")
        self.load_output.pack()
        ttk.Button(self.load_tab, text="Show Description", command=self.show_description).pack(pady=5)
        ttk.Button(self.load_tab, text="Show Info", command=self.show_info).pack(pady=5)

    def create_dataframe(self):
        columns = [col.strip() for col in self.columns_entry.get().split(',')]
        raw_rows = self.data_text.get("1.0", tk.END).strip().split('\n')
        row_data = [row.split(',') for row in raw_rows if row]

        df = self.creator.create_dataframe(columns, row_data)
        self.display_dataframe(df)

    def save_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path and self.creator.save_to_csv(file_path):
            messagebox.showinfo("Saved", f"CSV saved at {file_path}")

    def save_excel(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if file_path and self.creator.save_to_excel(file_path):
            messagebox.showinfo("Saved", f"Excel saved at {file_path}")

    def update_cell_popup(self):
        self.simple_popup("Update Cell", ["Row Index", "Column Name", "New Value"], self.apply_update)

    def delete_row_popup(self):
        self.simple_popup("Delete Row", ["Row Index"], self.apply_row_delete)

    def delete_col_popup(self):
        self.simple_popup("Delete Column", ["Column Name"], self.apply_col_delete)

    def simple_popup(self, title, fields, callback):
        top = tk.Toplevel(self.root)
        top.title(title)
        entries = []

        for i, field in enumerate(fields):
            ttk.Label(top, text=field).grid(row=i, column=0, padx=5, pady=5)
            entry = ttk.Entry(top)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries.append(entry)

        ttk.Button(top, text="Submit", command=lambda: callback(entries, top)).grid(row=len(fields), columnspan=2, pady=10)

    def apply_update(self, entries, top):
        try:
            row = int(entries[0].get())
            col = entries[1].get()
            val = entries[2].get()
            updated = self.creator.update_value(row, col, val)
            if updated:
                self.display_dataframe(self.creator.get_dataframe())
                top.destroy()
            else:
                messagebox.showerror("Error", "Invalid row/column.")
        except ValueError:
            messagebox.showerror("Error", "Row index must be an integer.")

    def insert_row_popup(self):
        top = tk.Toplevel(self.root)
        top.title("Insert Row")

        columns = self.creator.get_dataframe().columns.tolist()
        entries = {}

        for i, col in enumerate(columns):
            ttk.Label(top, text=col).grid(row=i, column=0, padx=5, pady=5)
            ent = ttk.Entry(top)
            ent.grid(row=i, column=1, padx=5, pady=5)
            entries[col] = ent

        ttk.Button(top, text="Submit", command=lambda: self.apply_insert_row(entries, top)).grid(
            row=len(columns), columnspan=2, pady=10)

    def apply_insert_row(self, entries, top):
        new_data = {col: entry.get() for col, entry in entries.items()}
        self.creator.df.loc[len(self.creator.df) + 1] = new_data
        self.display_dataframe(self.creator.df)
        top.destroy()


    def insert_col_popup(self):
        top = tk.Toplevel(self.root)
        top.title("Insert Column")

        ttk.Label(top, text="New Column Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(top)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(top, text="Default Value:").grid(row=1, column=0, padx=5, pady=5)
        value_entry = ttk.Entry(top)
        value_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(top, text="Submit", command=lambda: self.apply_insert_column(
            name_entry.get(), value_entry.get(), top)).grid(row=2, columnspan=2, pady=10)

    def apply_insert_column(self, col_name, default_value, top):
        self.creator.df[col_name] = default_value
        self.display_dataframe(self.creator.df)
        top.destroy()


    def apply_row_delete(self, entries, top):
        try:
            row = int(entries[0].get())
            confirm = messagebox.askyesno("Confirm", f"Delete row {row}?")
            if confirm and self.creator.delete_row(row):
                self.display_dataframe(self.creator.get_dataframe())
                top.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid row index.")

    def apply_col_delete(self, entries, top):
        col = entries[0].get()
        confirm = messagebox.askyesno("Confirm", f"Delete column '{col}'?")
        if confirm and self.creator.delete_column(col):
            self.display_dataframe(self.creator.get_dataframe())
            top.destroy()

    def display_dataframe(self, df):
        self.create_output.delete("1.0", tk.END)
        self.create_output.insert(tk.END, str(df))

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.loader = CSVDataLoader(file_path)
            df = self.loader.get_data()
            self.load_output.delete("1.0", tk.END)
            self.load_output.insert(tk.END, str(df))

    def show_description(self):
        if hasattr(self, 'loader'):
            self.load_output.delete("1.0", tk.END)
            self.load_output.insert(tk.END, self.loader.get_description())

    def show_info(self):
        if hasattr(self, 'loader'):
            self.load_output.delete("1.0", tk.END)
            self.load_output.insert(tk.END, self.loader.get_info())

    def show_dashboard(self):
        df = self.creator.get_dataframe()

        if df.empty:
            messagebox.showerror("Error", "No data to plot.")
            return

        numeric_cols = df.select_dtypes(include='number').columns.tolist()
        if not numeric_cols:
            messagebox.showinfo("No Plots", "No numeric columns to plot.")
            return

        for col in numeric_cols:
            plt.figure(figsize=(6, 4))
            df[col].plot(kind='bar', title=f"{col} - Bar Chart")
            plt.xlabel("Index")
            plt.ylabel(col)
            plt.tight_layout()

        plt.show()



if __name__ == '__main__':
    root = tk.Tk()
    style = Style(theme="darkly")  # Can change to "superhero", "cyborg", etc.
    app = CSVEditorApp(root)
    root.mainloop()
