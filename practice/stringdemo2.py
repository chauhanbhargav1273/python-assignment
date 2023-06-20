    s=input("enter String = ")

upper=0
lower=0
char=0
digit=0
space=0

for i in s:
    if i.isupper():
       upper+=1
    elif i.islower():
        lower+=1
    if i.isalpha():
        char+=1
    elif i.isnumeric():
        digit+=1
    elif i.isspace():
        space+=1

print("total upper = ",upper)
print("total lower = ",lower)
print("total char = ",char)
print("total digit = ",digit)
print("total space = ",space)
