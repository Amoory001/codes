#from the library /module random we import submodule randint to generate random interger

from random import randint

from guizero import*

def open_file():
    with open(file_name.value,"r") as f:
         return f.read()

app = App()
sav_box=Box(app,border=1,width="fill")
Text(sav_box,text='Enter file name : ')
open_b=PushButton(sav_box, command=open_file, text="open file")
file_name = TextBox(sav_box,align='right',width='fill')

app.display()


#we use 'w' for writing a file and 'r' for reading a file
#very important to include the format of the file i.e '.txt'

f = open("dati.txt", 'w')

#create a varible to store the string
#initialize the string

dati = ''

#Nested loop (loop inside a loop)

for riga in range(10):

    #second loop to compile a single line
    for elemento in range(1):

        #adding the random intergers to our variable dati
        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
    
    #we add a line terminator to wrap up the 1st line
    dati = dati + "\n"

# we could have created a list of lines without the loops:
# lines = [
# ... 'first line of file \ n',
# ... 'second line of file \ n',
# ... 'third line of file \ n',
# ...]

print(dati)

# we write the strings to the file
f.write(dati)

# we close our file for no further modification
f.close()
