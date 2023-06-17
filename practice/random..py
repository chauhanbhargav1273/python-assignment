import random

#l=[1,2,3,"hello","tops",3.4,6.1]

#print(random.randint(1,20))
#print(random.choice(l))

l=[]
lucky=[]

for i in range(1,101):
    l.append (i)
print(l)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
