from tkinter import *
from PIL import ImageTk, Image
import os

def next_image():
    global counter
    img_label.config(image=img_array[counter % len(img_array)])
    counter = counter + 1

counter = 1
root = Tk()

root.title('Wallpaper Viewer')
root.geometry('1050x700')
root.configure(background='black')

files = os.listdir('wallpapers')
img_array = []
for file in files:
    img = Image.open(os.path.join('wallpapers', file))
    resized_img = img.resize((1000, 600))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root, image=img_array[0])
img_label.pack(pady=(20, 10))

next_btn = Button(root, text='Next Image', bg='white', fg='black', width=25, height=1, command=next_image)
next_btn.pack(pady=(10, 10))
next_btn.config(font=('verdana', 15))

root.mainloop()