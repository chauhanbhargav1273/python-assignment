#Write a Python program that will return true if the two given integer
#values are equal or their sum or difference is 5.


a=int(input("enter value = "))
b=int(input("enter value = "))

if a == b or (a-b) == 5 or (a+b) == 5:
    print("true")
else:
    print("false")
    

