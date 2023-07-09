#Write a Python program to read an entire text file.

file=open("demo.txt","w")
file.write("hello")
file=open("demo.txt","r")
print(file.read())
file.close()

