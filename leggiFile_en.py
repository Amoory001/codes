#importing of modules

import string
import numpy as np
import matplotlib.pyplot as plt
from random import randint

from guizero import*

def open_file():
    with open(file_name.value,"r") as f:
         return f

def closing():
    return app.destroy()

app = App()
sav_box=Box(app,border=1,width="fill")
Text(sav_box,text='Enter file name : ')
open_b=PushButton(sav_box, command=open_file, text="open file")
file_name = TextBox(sav_box,align='right',width='fill')
open_b1=PushButton(app,text="click me", command=closing)
app.display()



#we use 'r' to read the file we created
#remember to display the name of the file exactly with the extention(.txt)

#f = open("dati.txt", 'r')

#we use the command readlines to read lines on a file
# lets read our fist line in dati file
#print(f.readline())


# lets read all the lines in a loop
#lets initialize some empty lists

coordX = []
coordY = []

# passing a loop inside the file

for line in f:
    valori = str(f.readline())  # line to string conversion
    Nval = len(valori)          # determine the length (number of characters)
    valori = valori.strip('\n') #eliminate the end of line sign
    valori = valori.split(',')  # separate the string into two by a comma
    valori = list(valori)       # covert to List format
    print(valori,Nval)
    coordX.append(int(valori[0])) # adds a single item to the existing list of coordX
    coordY.append(int(valori[1])) # adds a single item to an existing list of coordY

f.close()  # we close the file

print ("X: ",coordX)
print ("Y: ",coordY)

# sorting the lists
coordX.sort()
coordY.sort()

print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)

# lets prints the data type of our coodinates
print(type(coordX))
print(type(coordY))

# now can be used as characters

plt.plot(coordX,coordY)
plt.ylabel('some numbers')
plt.show()
