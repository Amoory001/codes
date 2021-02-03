#tkinter
from tkinter import *               # we import every submodule in tkinter library
root = Tk()                         #initialize a blank window
root.geometry('300x300')           #change the dimension of our window
l=Label(root,text="Hello World")

                                #adding a label widget
l.pack()
                        #to pack what ever instruction to the window
root.mainloop()                 #to make it visible to the user keeps it in the loop

