#Write a Python program to copy the contents of a file to another file.

file=open("demo.txt","r")
file1=open("myfile.txt","a")

for i in file:
    file1.write(i+"\n")
file.close()
file1.close()
