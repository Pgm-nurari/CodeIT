import os
from tkinter import *
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
        self.app.geometry('1200x700')
        # self.app.resizable(False,False)
        self.app.title('Image Viewer 2.0')
        self.app.config(padx=10,pady=10)
        try:
            self.app.iconbitmap('Assets/imgLogo.ico')
        except:
            pass

    def set_layout(self):
        # Creating Maniframes for image and selection
        self.image_frame = Frame(self.app)
        self.radio_frame = Frame(self.app)
        
        self.image_frame.config(height=680,border=1,borderwidth=5,bg='yellow')
        self.image_frame.grid(row=0,column=0,sticky='news',padx=(0,10))
        
        self.radio_frame.config(width=200,height=680,border=1,borderwidth=5,bg='green')
        self.radio_frame.grid(row=0,column=1,)
        
        self.app.grid_rowconfigure(0,weight=1)
        self.app.grid_columnconfigure(0,weight=1)
        self.app.grid_columnconfigure(0,weight=1)

    def add_images(self):
        asset_images = os.listdir(os.path.join(os.getcwd(), 'Assets'))
        for i in asset_images:
            if ('.png' in i) or ('.jpg' in i):
                image = self.resize_image(Image.open(f'Assets/{i}'))
                self.image_list.append(ImageTk.PhotoImage(image))

    def resize_image(self, image): #! Used by add_image() function.
        original_width, original_height = image.size
        ratio = min(1000 / original_width, 800 / original_height)
        new_size = (int(original_width * ratio), int(original_height * ratio))
        return image.resize(new_size, Image.LANCZOS)
    
if __name__=='__main__':
    root = ImageViewer(Tk())
    root.app.mainloop()