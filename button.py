from tkinter import *

root = Tk()


def on_click():
    myLabel = Label(root, text="Button has been clicked")
    myLabel.pack()


myButton = Button(root, text="Click me", command=onClick)
# state=DISABLED disables button - use padx and pady to change dimensions

myButton.pack()


root.mainloop()
