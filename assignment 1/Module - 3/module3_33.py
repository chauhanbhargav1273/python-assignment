#Write a Python script to concatenate following dictionaries to create a new one.

d1={1:"vishal"}
d2={2:"bhargav"}
d3={}

for i in (d1,d2): d3.update(i)

print(d3)
