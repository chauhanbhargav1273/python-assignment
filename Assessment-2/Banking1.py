import mysql.connector

def create_conn():
   return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_1"
       )
class bank:
   
   def register(self,ano,fname,lname,balance,email,password):
        self.ano=ano
        self.fname=fname
        self.lname=lname
        self.email=email
        self.password=password
        self.balance=balance
        conn=create_conn()
        cursor=conn.cursor()
        cursor.execute(f"insert into costmer(ano,fname,lname,balance,email,password) values('{self.ano}','{self.fname}','{self.lname}','{self.balance}','{self.email}','{self.password}');")
        conn.commit()
        conn.close()
        print("*"*60)
        print("Data Inserted Sucessfully")

   def login(self,email,password):
      
      conn=create_conn()
      cursor=conn.cursor()
      cursor.execute(f"select email,password from costmer where email='{email}' and password='{password}';")
      
      r=cursor.fetchall()
      conn.close()
      if len(r)<1:
         print("user not found")
      else:
         
         print("logined successfully")

   def update(self,ano,fname,lname,balance,password,email):
      conn=create_conn()
      cursor=conn.cursor()
      cursor.execute(f"update costmer set fname='{fname}',lname='{lname}',balance='{balance}',email='{email}',password='{password}' where ano='{ano}';")
      r=cursor.fetchall()
      conn.commit()
      conn.close()
      if len(r)<0:
         print("account number not found")
      else: 
         print("Update Sucessfully")

   def view_all(self):      
      conn=create_conn()
      cursor=conn.cursor()
      cursor.execute(f"select * from costmer")
      rows=cursor.fetchall()
      #print(rows)
      cn=1
      for i in rows:
         count=0
         print("***************Detail Of Banker",cn,"******************")
         print("Account Number : ",i[count])
         count+=1
         print("First Name : ",i[count])
         count+=1
         print("Last Name : ",i[count])
         count+=1
         print("Balance : ",i[count])
         count+=1
         print("Email : ",i[count])
         count+=1
         print("Password : ",i[count])
         count+=1
         cn+=1
      conn.close()

   def delete(self,ano):
      conn=create_conn()
      cursor=conn.cursor()
      cursor.execute(f"delete from costmer where ano='{ano}';")
      conn.commit()
      conn.close()
      print("Deleted successfully")

   def withdraw(self,ano):
      self.ano=ano
      
      conn=create_conn()
      cursor=conn.cursor()
      cursor.execute(f"update costmer set balance='{self.balance}' where ano='{self.ano}';")
      conn.commit()
      conn.close()
      print("withdraw sucessfully")


   def deposit(self):
      print()

   def view_balance(self,ano):
      self.ano=ano
      
      conn=create_conn()
      cursor=conn.cursor()
      cursor.execute(f"select balance from costmer where ano='{self.ano}';")
      rows=cursor.fetchall()
      for i in rows:
         count=0
         print("***************Detail Of costmer""******************")
         count+1
         print("Balance : ",i[count])
      conn.close()
      
b1=bank()
   
while True:
    print("*"*60)
    print("WALCOME TO BANKING APPLICATION")
    print("*"*60)
    print("1. Banker")
    print("2. Customer")
    print("3. Exit")
    print("*"*60)
    choice=int(input("Enter Your Choice : "))
    print("*"*60)
    if choice==1:
        print("Banker")
        print("*"*60)
        print("1. Register")
        print("2. Login")
        print("3. Update all Customers")
        print("4. View all Customers")
        print("5. Delete all Customers")
        
        print("*"*60)
        choice=int(input("Enter Your roles : "))
        print("*"*60)
        if choice==1:
            print("Register")
            print("*"*60)
            ano=int(input("enter account number : "))
            fname=input("enter first name : ")
            lname=input("enter last name : ")
            balance=int(input("enter check balance : "))
            email=input("enter Email id : ")
            password=input("enter password : ")
            b1.register(ano,fname,lname,balance,email,password)
        elif choice==2:
            print("Login")
            print("*"*60)
            email=input("Enter Email : ")
            password=input("enter your password : ")
            b1.login(email,password)
        elif choice==3:
            print("Update all Customers")
            print("*"*60)
            ano=int(input("enter account number : "))
            fname=input("enter first name : ")
            lname=input("enter last name : ")
            balance=int(input("enter check balance : "))
            email=input("enter Email id : ")
            password=input("enter password : ")
            b1.update(ano,fname,lname,balance,email,password)
        elif choice==4:
            print("View all Customers")
            print("*"*60)
            b1.view_all()
        elif choice==5:
            print("Delete all Customers")
            print("*"*60)
            ano=int(input("enter account number : "))
            b1.delete(ano)
    elif choice==2:
        print("Customer")
        print("*"*60)
        print("1. Register")
        print("2. Login")
        print("3. Withdraw Amount")
        print("4. Deposit Amount")
        print("5. View Balance")

        print("*"*60)
        choice=int(input("Enter Your Choice : "))
        print("*"*60)
        if choice==1:
            print("Register")
            print("*"*60)
            ano=int(input("enter account number : "))
            fname=input("enter first name : ")
            lname=input("enter last name : ")
            balance=int(input("enter check balance : "))
            email=input("enter Email id : ")
            password=input("enter password : ")
            b1.register(ano,fname,lname,balance,email,password)
        elif choice==2:
            print("Login")
            email=input("Enter Email : ")
            password=input("enter your password : ")
            print("*"*60)
            b1.login(email,password)
            print("*"*60)
        elif choice==3:
            print("Withdraw Amount")
            ano=int(input("Enter Account Number : "))
            amount=int(input("Enter Withdraw Ammount: "))
            
            b1.withdraw(amount,,ano,balance)
            print("*"*60)
        elif choice==4:
            print("Deposit Amount")
            print("*"*60)
        elif choice==5:
            print("View Balance")
            print("*"*60)
            ano=int(input("enter Account Number : "))
            b1.view_balance(ano)
    else:
        print("Thank you")
        break

