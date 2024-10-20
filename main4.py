from tkinter import *

root = Tk()
root.geometry('500x500')

s = Spinbox(root, from_=0, to=10e+1000)
s.pack()

root.mainloop()