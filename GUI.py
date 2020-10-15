#GUI using python is beginner friendly and helps you to understand how it works !
#Here we will be explaining how we could actually implement it using few lines of code!
#Lets automate something using tkinter



from tkinter import *

def click():
    l2 = Label(root, text = "Hello "+ e.get())
    l2.pack()

root = Tk()
e = Entry(root,width =60)
e.pack()
b1 = Button(root, text = "Enter your name",command = click)
b1.pack()
root.mainloop
