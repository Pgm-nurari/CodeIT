 #* Working with images in tkinter! 
import tkinter
from PIL import Image,ImageTk

if __name__=='__main__':
    app=tkinter.Tk()
    app.title('Images')
    app.iconbitmap('Assets/imgLogo.ico') #? This is the app icon on the title bar

    my_img = ImageTk.PhotoImage(Image.open('Assets/img1.jpg'))
    imgLabel = tkinter.Label(app,image=my_img)
    imgLabel.pack()

    app.mainloop()