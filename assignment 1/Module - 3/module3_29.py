#Write a Python program to unzip a list of tuples into individual lists. 

z1=[('Manjeet', 4), ('Nikhil', 1), ('Shambhavi', 3), ('Astha', 2)]

a=[[name for name,roll in z1],[roll for name,roll in z1]]
print(a)
