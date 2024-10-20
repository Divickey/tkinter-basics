from tkinter import *

#create output window

root = Tk()

#output window size
root.geometry('500x500')

#create a button - widget
btn = Button(root,text = "click me", bd=5, background="cyan", command=root.destroy)

#set the position of button on the top of the window.
#tryside = bottom, right, left, top
btn.pack(side="bottom")

root.mainloop()