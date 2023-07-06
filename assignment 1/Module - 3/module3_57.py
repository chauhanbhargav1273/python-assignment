#Write a Python program to read a random line from a file.

import random
print(random.choice(open("text.txt","r").readline().split()))
