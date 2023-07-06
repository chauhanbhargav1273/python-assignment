class bank:
    def openaccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=amount
        else:
            self
