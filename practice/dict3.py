d1={"a":1,"b":2,"c":3,"d":4}
d2={"a":5,"c":10,"d":15,"e":20}
d3={}

for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
        for j in d2:
            if j not in d3:
                d3[j]=d2[j]
print(d3)
