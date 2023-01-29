class user:
    def __init__(self,name,age,gender):
        self.nam=name
        self.ag=age
        self.gend=gender
    def show_details(self):
        print("details: ")
        print(self.nam,self.ag,self.gend)

class bank(user):
    def __init__(self,nae,age,gender):
        super().__init__(nae,age,gender)
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("balance update ", self.balance)
    def withdraw(self,amount):
        self.amount=amount
        self.balance = self.balance - self.amount
        print("balance update ", self.balance)

    def view_details(self):
        self.show_details()
        print(self.balance)






d=bank("Anu",12,"male")
d.deposit(12)
d.deposit(23)
d.withdraw(3)
d.withdraw(4)
d.view_details()








