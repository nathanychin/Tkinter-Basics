from tkinter import *

root = Tk()

# Creating widget
myLabel1 = Label(root, text="Label 1")
myLabel2 = Label(root, text="Label 2")

# Moving to screen
# myLabel1.pack()
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
