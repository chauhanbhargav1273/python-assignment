d={}
def add_fruit(fname,qty,price):
    if fname in d:
        print("fruit name is avalable")
    else:
        d[fname]={
            "qty":qty,
            "price":price
        }
       
def view_fruit():
    
        print(d)
       
       
def update_fruit(fname,qty,price):
    if fname in d:
        d[fname]={
            "qty":qty,
            "price":price,
        }
    else:
        print("enter valid fruit name")
        

def save_all_fruit(fname,qty,price):
    file=open("fruit.txt","w")
    file.write("Fruit Name : "+fname+"\nQuantity : "+str(qty)+"\nPrice : "+str(price))
    print(d)
    file.close()
    file=open("fruit.txt","r")
    a=file.read()
    print(a)
    file.close()
    
    
    
   

while True:
    print("*"*60)
    print("WALCOME TO FRUIT MARKET")
    print("*"*60)
    print("1. Manager")
    print("2. Customer")
    print("3. Exit")
    print("*"*60)
    choice=int(input("Enter Your Choice : "))
    print("*"*60)
    if choice==1:
        print("Fruit Market Manager")
        print("*"*60)
        print("1. Add Fruit Stock")
        print("2. View Fruit Stock")
        print("3. Update Fruit Stock")
        print("*"*60)
        choice=int(input("Enter Your roles : "))
        print("*"*60)
    
        if choice==1:
            print("Add Fruit Stock")
            print("*"*60)
            fname=input("enter fruit name : ")
            qty=int(input("enter fruit qulity : "))
            price=int(input("enter fruit price : "))
            add_fruit(fname,qty,price)
            save_all_fruit(fname,qty,price)
            yn=input("Do You Wont To Perform More Opration (Y/N) : ")
            if yn=='y':
                choice==1
            else:
                continue
        elif choice==2:
            print("View Fruit Stock")
            print("*"*60)
            view_fruit()
        elif choice==3:
            fname=input("enter fruit name : ")
            qty=int(input("enter fruit qulity : "))
            price=int(input("enter fruit price : "))
            update_fruit(fname,qty,price)
                
    elif choice==2:
        print("costomer")
    
    else:
        print("Thank you")
        break


