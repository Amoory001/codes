import string
from random import randint 
#have a txt file with name dati already

#reading our file

f=open("dati.txt",'r')
print(f.read)


w=open("dati.txt",'a')
print(w.read)

#lets update our file
w.write("updated file")
w.close()


#check your txt file
#you will notice addition of "updated file"


#creating a new file
c=open("py.txt",'w')

#lets put some numbers in it
a= ""

for i in range(5):
    a= a + str(randint(1,100))+ "\n"
    i=i+1
    
    
print(a)
#now lets put the numbers generated to our new file
c.write(a)
#remember to close your writing file 'w'
c.close()

