from tkinter import *

root = Tk()


def onClick():
    myLabel = Label(root, text="Button has been clicked")
    myLabel.pack()


myButton = Button(root, text="Click me", command=onClick)
# state=DISABLED disables button - use padx and pady to change dimensions

myButton.pack()


root.mainloop()
