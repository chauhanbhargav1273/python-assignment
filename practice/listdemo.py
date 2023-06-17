l=[1,2,3,1.1,22.2,"tops",True,10,20,"python",False,101,202,"java","automation"]
print(l)
l.append(100)
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
l1.append(200)
print(l1)
print(l)
l2=l
print(l2)
l2.append(300)
print(l2)
print(l)
print(l.count(1))
l3=[101,202,303]
l.extend(l3)
print(l)
print(l.index(10))
l.insert(5,1000)
print(l)
l.pop()
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)

for i in l:
    print(i)
print(100 in l)

    



