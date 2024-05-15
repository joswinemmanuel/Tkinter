from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    
    if email=='joswin@gmail.com' and password=='123':
        messagebox.showinfo('Completed', 'Login Successful')
    else:
        messagebox.showinfo('Error', 'Login Failed')

root = Tk()
root.title("Login Form")
root.iconbitmap('login_icon.ico')
# root.minsize(800, 400)
# root.maxsize(1000, 800)
root.geometry("350x500")
root.configure(background='#478eff')

img = Image.open('flipkart_logo.png')
resized_img = img.resize((70, 70))
img = ImageTk.PhotoImage(resized_img)

img_lable = Label(root, image=img)
img_lable.pack(pady=(10, 10))

title_lable = Label(root, text='Flipkart', fg='white', bg='#478eff')
title_lable.pack()
title_lable.config(font=('verdana', 24))

email_lable = Label(root, text='Enter Email : ', fg='white', bg='#478eff')
email_lable.pack(pady=(20, 5))
email_lable.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=4, pady=(1, 15))

password_lable = Label(root, text='Enter Password : ', fg='white', bg='#478eff')
password_lable.pack(pady=(20, 5))
password_lable.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=4, pady=(1, 15))

login_btn = Button(root, text='Login Here', bg='white', fg='#080078', width=10, height=1, command=handle_login)
login_btn.pack(pady=(20, 20))
login_btn.config(font=('verdana', 9))

root.mainloop()