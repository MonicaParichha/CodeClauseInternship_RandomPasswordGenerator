import random
import string
from tkinter import *

def pwd_generate():
    pwd_length = int(enter_pwdLength.get())
    pwd_ch = string.ascii_letters + string.digits + string.punctuation

    if pwd_length < 8:
        result.config(text="Password length must be at least 8")
    else:
        password = ''.join(random.choice(pwd_ch) for i in range(pwd_length))
        result.config(text=password)


root = Tk()
root.title("Random Password Generator")
root.geometry("300x100")
root.config(bg="#fff")

pwdLength = Label(root, text="Enter Desired password length:")
pwdLength.config(fg="#000")
pwdLength.pack()

enter_pwdLength = Entry(root)
enter_pwdLength.config(fg="#000")
enter_pwdLength.pack()

button_generate = Button(root, text="Generate Password", command=pwd_generate)
button_generate.config(fg="#fff", bg="#000")
button_generate.pack()

result = Label(root, text="")
result.config(fg="#000")
result.pack()

root.mainloop()
