#Write a Python program to count the number of characters (character 
#frequency) in a string

a=(input("enter string = "))
b = {}

for i in a:
	if i in b:
		b[i] += 1
	else:
		b[i] = 1

print(b)
