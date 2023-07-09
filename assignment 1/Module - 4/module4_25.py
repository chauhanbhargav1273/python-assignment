#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class demo:
    def radius(self,rediu):
        r=rediu
    def area(self,r):
        a=3.14*r*r
        print("area of circle : ",a)
    def pari(self,r):
        b=2*3.14*r
        print("parimeter if circle : ",b)

c1=demo()
n=int(input("enter rediues of number : "))
c1.area(n)
c1.pari(n)


