#Write a Python program to count the occurrences of each word in a 
#given sentence
a = (input("enter string = "))

b = a.split()
c={}
for i in b:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1
print(c)


