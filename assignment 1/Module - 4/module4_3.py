#Write a Python program to append text to a file and display the text.


file=open("demo.txt","w")
file.write("hello\n")
file=open("demo.txt","a")
file.write("hello\n")
file=open("demo.txt","a")
file.write("welcome\n")
file=open("demo.txt","a")
file.write("python\n")
file=open("demo.txt","a")
file.write("bhargav\n")
file=open("demo.txt","r")
print(file.read())
file.close()
