# Write a Python program to count occurrences of a substring in a string.

a=(input("enter value = "))
b=(input("enter value = "))
m=0;
for i in range(0,len(a)):
    n=i;
    end=i+len(b)
    m=m+a.count(b,n,end)
print(m)
    
