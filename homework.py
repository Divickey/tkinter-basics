from tkinter import *

root = Tk()
root.title("replit")
root.geometry('450x300')
root.config(background="black")

ptemplate = Label(root, text="pick template").place (x=25, y=60)
nproject = Label(root, text="pick template").place (x=25, y=90)
crepl = Button(root, text="create repl", bd=5).place(x=40, y=130)
pentry = Entry(root, width=30).place(x=110, y=60)
nentry = Entry(root, width=30).place(x=110,y=90)
root.mainloop()