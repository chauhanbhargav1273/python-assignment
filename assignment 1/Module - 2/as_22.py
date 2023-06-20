n=input("enter string = ")

if len(n)<2:
    n=""
    print(n)
else:
    print(n[:2]+n[-2:])
    
