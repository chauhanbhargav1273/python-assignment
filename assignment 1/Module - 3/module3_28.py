#Write a Python program to remove an empty tuple(s) from a list of tuples.


l1= [(), (),('.') ,('a', 'b'), ('a', 'b', 'c'), ('d')]
l1=[t for t in l1 if t]
print(l1)

