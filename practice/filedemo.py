file=open("tops.txt","w")
file.write("this is file write")
#file.close()
print("file written successfully")


file=open("tops.txt","r")
print(file.read())
file.close()


file=open("tops.txt","a")
file.write("\nnow this file is appended")
file.close()
print("file appended successfully")

file=open("tops.txt","r")
print(file.read())
file.close()

file=open("tops.txt","w+")
file.write("this is w+ file")
print("current position = ",file.tell())
file.seek(5)
print(file.read())
file.close()
print("w+ mode working")


