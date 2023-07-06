print("start code")

try:
    
    a=int(input("enter value = "))
    b=int(input("enter value = "))
    c=a/b
    print("divition = ",c)

    l=[1,2,3,4,5]
    index=int(input("enter index value = "))
    print(l[index])
    
##except ZeroDivisionError as e:
##    print("exception zero division error")
##except ValueError as e:
##    print("exception value error")
##except IndexError as e:
##    print("exception Index error")
except Exception as e:
    print("exception caught = ",e)
finally:
    print("finally called")
print("end code")

