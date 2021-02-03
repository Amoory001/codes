#tkinter with closing button
from tkinter import *              # we import every submodule in tkinter library
root = Tk()                        #initialize a blank window
root.geometry('300x300')           #change the dimension of our window
l=Label(root,text="Hello World")   #
b=Button(root,text="close window",command=root.destroy)
l.pack()                           #to pack what ever instruction to the window
b.pack()
#root.mainloop()
