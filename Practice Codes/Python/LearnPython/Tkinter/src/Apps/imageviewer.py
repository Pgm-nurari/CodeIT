import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class ImageViewer:

    def __init__(self, root: Tk):
        self.app = root
        self.image_list = []
        # self.image_size_list=[]
        self.position = 0

        self.set_application()
        self.add_images()
        self.set_layout()

    def set_application(self):
        self.app.geometry('1000x700')
        self.app.resizable(False,False)
        self.app.title('Image Viewer')
        self.app.config(padx=20,pady=20)
        try:
            self.app.iconbitmap('Assets/imgLogo.ico')
        except:
            pass

    def set_layout(self):
        self.image_frame = LabelFrame(self.app,text="Images",padx=10,pady=10)
        self.button_frame = LabelFrame(self.app,text="Buttons",pady=10)

        self.image_frame.grid(row=0, column=0, sticky="nsew")
        self.button_frame.grid(row=1, column=0, sticky="ew")

        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

        self.imageLabel = Label(self.image_frame, image=self.image_list[self.position])
        self.imageLabel.pack(expand=True)

        self.back_button = Button(self.button_frame, text=" <-- ", command=self.go_back)
        self.exit_button = Button(self.button_frame, text="Exit App", command=self.app.destroy)
        self.next_button = Button(self.button_frame, text=" --> ", command=self.go_next)
        self.status_bar = Label(self.button_frame,text=f'Image {self.position+1} of {len(self.image_list)}')

        self.back_button.config(background="#1D8348",foreground="#FDFEFE",disabledforeground="#E74C3C",justify="right",relief="flat",state="disabled",padx=10)
        self.next_button.config(background="#1D8348",foreground="#FDFEFE",disabledforeground="#E74C3C",justify="left",relief="flat",state="normal",padx=10)
        self.exit_button.config(background="#F1948A",foreground="#17202A",activebackground="#D0DFF7",disabledforeground="#E74C3C",justify="center",relief="flat",state="normal",padx=20)
        self.status_bar.config(border=1,relief='sunken',justify='right',anchor='e')

        self.back_button.grid(row=0, column=0, padx=10, pady=10)
        self.exit_button.grid(row=0, column=1, padx=10, pady=10)
        self.next_button.grid(row=0, column=2, padx=10, pady=10)
        self.status_bar.grid(row=0, column=3, padx=5,pady=10,sticky='ew')
        
        self.button_frame.columnconfigure(3,weight=1)


    def add_images(self):
        asset_images = os.listdir(os.path.join(os.getcwd(), 'Assets'))
        for i in asset_images:
            if ('.png' in i) or ('.jpg' in i):
                image = self.resize_image(Image.open(f'Assets/{i}'))
                self.image_list.append(ImageTk.PhotoImage(image))

    def resize_image(self, image):
        original_width, original_height = image.size
        ratio = min(1000 / original_width, 800 / original_height)
        new_size = (int(original_width * ratio), int(original_height * ratio))
        return image.resize(new_size, Image.LANCZOS)

    def go_back(self):
        if self.position > 0:
            self.position -= 1
            self.imageLabel.config(image=self.image_list[self.position])
            self.next_button.config(state='normal')
        if self.position == 0:
            self.back_button.config(state='disabled')
        self.status_bar.config(text=f'Image {self.position+1} of {len(self.image_list)}')

    def go_next(self):
        if self.position < len(self.image_list) - 1:
            self.position += 1
            self.imageLabel.config(image=self.image_list[self.position])
            self.back_button.config(state='normal')
        if self.position == len(self.image_list) - 1:
            self.next_button.config(state='disabled')
        self.status_bar.config(text=f'Image {self.position+1} of {len(self.image_list)}')

if __name__ == '__main__':
    root = ImageViewer(Tk())
    root.app.mainloop()