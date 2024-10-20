from tkinter import *

#output screen
root = Tk()
root.title("login")
root.geometry('450x300')
root.config(background="black")

#widgets
username = Label(root, text="username").place(x=40,y=60)
password = Label(root, text="password").place(x=40,y=90)
login = Button(root, text="login", bd=5).place(x=40,y=130)
uentry = Entry(root, width=30).place(x=110,y=60)
pentry = Entry(root, show='*', width=30).place(x=110,y=90)

root.mainloop()