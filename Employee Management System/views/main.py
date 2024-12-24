from customtkinter import *
from PIL import Image

root = CTk()
root.geometry('930x478')
root.resizable(0, 0)
root.title('login form')
image = CTkImage(Image.open('cover.jpg'), size=(930, 478))
imageLb = CTkLabel(root, image=image, text='')
imageLb.place(x=0, y=0)

headerLb = CTkLabel(root, text='Employee Management System', bg_color='#151E2D', font=('Brush Script Std', 20, 'bold'),
                    text_color='#000000')
headerLb.place(x=20, y=30)

usernameEntry = CTkEntry(root, placeholder_text='Enter User Name', text_color='#000000', width=200, height=30,
                         font=('Arial', 14, 'bold'))
usernameEntry.place(x=20, y=70)

passwordEntry = CTkEntry(root, placeholder_text='Enter Password', text_color='#000000', width=200, height=30,
                         font=('Arial', 14, 'bold'))
passwordEntry.place(x=20, y=110)

loginBtn = CTkButton(root, text="✔ Login", height=5, width=100, font=('Arial', 20, 'bold'))
loginBtn.place(x=60, y=150)
root.mainloop()