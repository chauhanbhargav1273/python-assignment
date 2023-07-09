#Write python program that user to enter only odd numbers, else will raise an exception.

n=int(input("enter value : "))
if n%2!=0:
    print(n,"is odd number")
else:
    print(n,"is invalid number")
