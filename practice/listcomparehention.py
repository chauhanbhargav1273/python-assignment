#newlist=[expression(element)for element in oldlist if codition]

data=[i for i in range(1,10) if i%2==0]
print(data)

# matrix

matrix=[[j for j in range(3)]for i in range(3)]
print(matrix)

#lambda argument : expression

max=lambda a,b :a if(a>b) else b

print(max(90,2))


# map(fun,iter)

def addition(n):
    return n+n

##l=[]
##
##for i in range(5):
##    num=int(input("enter value = "))
##    data=addition(num)
##    l.append(data)
##print(l)

numbers=(12,23,34,45,56)
result=map(addition, numbers)
print(list(result))
    
#set are represented by{}(values enclosed in curly braces)

s={10,1.1,"tops","python",True,10}

print(s)

#Zip fuction

a=["geeks","for","GEEKS"]
b=[2175,3456,7866]

c={a:b for a,b in zip(a,b)}
print(c)
