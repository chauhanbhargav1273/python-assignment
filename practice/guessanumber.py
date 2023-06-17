import random

num=random.randint(1,20)

while True:
    guess=int(input("enter guess a number between 1 to 20 = "))
    if guess==num:
        print("you guess correct number")
        break
    elif guess>num:
        print("you guess a greater number")
    elif guess<num:
        print("you guess a smaller number")
