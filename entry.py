from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your name")  # Default text im form


def onSubmit():
    hello = "Hello " + e.get()
    entryLabel = Label(root, text=hello)
    entryLabel.pack()


submitButton = Button(root, text="Submit", command=onSubmit)
submitButton.pack()

root.mainloop()
