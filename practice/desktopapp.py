from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
   return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_1"
       )

def insert_data():
    if e_ename.get()=="" or e_dept.get()=="" or e_salary.get()=="":
        msg.showinfo("insert status","all Fields are Mandatory")
    else:
         conn=create_conn()
         cursor=conn.cursor()
         query="insert into emp(ename,dept,salary)values(%s,%s,%s)"
         args=(e_ename.get(),e_dept.get(),e_salary.get())
         cursor.execute(query,args)
         conn.commit()
         conn.close()
         e_ename.delete(0,"end")
         e_dept.delete(0,"end")
         e_salary.delete(0,"end")
         msg.showinfo("Insert Status ","Insert data sucessfully")

def search_data():
   e_ename.delete(0,"end")
   e_dept.delete(0,"end")
   e_salary.delete(0,"end")
   if e_id.get()=="":
      msg.showinfo("Search Status","id is mandatory for search")
   else:
      conn=create_conn()
      cursor=conn.cursor()
      query="select * from emp where id=%s"
      args=(e_id.get(),)
      cursor.execute(query,args)
      row=cursor.fetchall()
      if row:
         for i in row:
             e_ename.insert(0,i[1])
             e_dept.insert(0,i[2])
             e_salary.insert(0,i[3])
      else:
         msg.showinfo("Search Status","ID Not Found")
      conn.close()

def update_data():
   if e_ename.get()=="" or e_dept.get()=="" or e_salary.get()=="" or e_id.get()=="":
      msg.showinfo("Update Status","All fields are Mandatory")
   else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update emp set ename=%s,dept=%s,salary=%s where id=%s"
        args=(e_ename.get(),e_dept.get(),e_salary.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close() 
        e_ename.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        e_id.delete(0,"end")
        msg.showinfo("Update Status","Data Updated Sucessfully")

def delete_data():
   if e_id.get()=="":
      msg.showinfo("Delete Status","Id is Mendatory")
   else:
      conn=create_conn()
      cursor=conn.cursor()
      query="delete from emp where id=%s"
      args=(e_id.get(),)
      cursor.execute(query,args)
      conn.commit()
      conn.close()

      e_id.delete(0,"end")
      e_ename.delete(0,"end")
      e_dept.delete(0,"end")
      e_salary.delete(0,"end")
      msg.showinfo("Delete Status","Data Delete Sucessfully")
      
      
         
root=Tk()

root.geometry("400x450")
root.title("My DEsktop Application")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Algerian",15))
l_id.place(x=50,y=50)

l_ename=Label(root,text="ENAME",font=("Algerian",15))
l_ename.place(x=50,y=100)

l_dept=Label(root,text="DEPT",font=("Algerian",15))
l_dept.place(x=50,y=150)

l_salary=Label(root,text="SALARY",font=("Algerian",15))
l_salary.place(x=50,y=200)

e_id=Entry(root)
e_id.place(x=170,y=50)

e_ename=Entry(root)
e_ename.place(x=170,y=100)

e_dept=Entry(root)
e_dept.place(x=170,y=150)

e_salary=Entry(root)
e_salary.place(x=170,y=200)

insert=Button(root,text="INSERT",font=("Algrian",15),bg="black",fg="white",command=insert_data)
insert.place(x=70,y=280)

search=Button(root,text="SEARCH",font=("Algrian",15),bg="black",fg="white",command=search_data)
search.place(x=200,y=280)

update=Button(root,text="UPDATE",font=("Algrian",15),bg="black",fg="white",command=update_data)
update.place(x=70,y=350)

delete=Button(root,text="DELETE",font=("Algrian",15),bg="black",fg="white",command=delete_data)
delete.place(x=200,y=350)

root.mainloop()
