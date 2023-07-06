class A:
    def show(self):
        print("show from A")
class B(A):
    def show(self):
        super().show()
        print("show from B")

class C(A):
    def show(self):
        super().show()
        print("show from C")
        
class D(B,C):
    def show(self):
        super().show()
        print("show from D")

d1=D()
d1.show()
        
