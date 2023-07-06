import random

data=open("file.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")

data.close()

data=open("file.txt","r")
prime=open("prime.txt","w")
notprime=open("norprime.txt","w")
l=data.read().split(",")[:-1]
print(l)
if 

file.close()
prime.close()
notprime.close()
