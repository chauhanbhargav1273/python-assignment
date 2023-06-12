for i in range(9):
    for j in range(9-i):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print(i+1,end=" ")
    print()
