from tkinter import *

root = Tk()
root.geometry('500x500')

btn1 = Button(root, text="north (click me)", bd=5, background="red", command=root.destroy)
btn2 = Button(root, text="east (click me)", bd=5, background="green", command=root.destroy)
btn3 = Button(root, text="south (click me)", bd=5, background="cyan", command=root.destroy)
btn4 = Button(root, text="west (click me)", bd=5, background="yellow", command=root.destroy)

btn1.pack(side="top")
btn2.pack(side="right")
btn3.pack(side="bottom")
btn4.pack(side="left")

root.mainloop()