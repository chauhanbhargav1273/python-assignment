n=int(input("enter value = "))
if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print("not prime number")
            break
    else:
        print("prime number")
else:
    print("not prime number")
