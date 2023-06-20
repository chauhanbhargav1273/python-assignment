#Write a Python function to reverses a string if its length is a multiple of 4.

n=(input("enter string = "))
if len(n) % 4 == 0:
        print(n[::-1])
else:
        print(n)
        
