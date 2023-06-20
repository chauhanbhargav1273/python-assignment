l=[]
st=1000
end=3001

for i in range(st,end):
    if i%5!=0 and i%7==0:
        l.append(i)
print(l)
