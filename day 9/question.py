class Rect:
    counts=0 # class attribute
    def __init__(self, l=0, b=0):
        self.l=l # instance attribute
        self.b=b
        Rect.counts+=1
        self.srno=Rect.counts 

    def area(self):
        return self.l*self.b
    
    def display(self):
        print(f"Dimension of Rect{self.srno} {self.l}x{self.b}")

r1=Rect()
r2=Rect(6,2)

r1.l=int(input("Enter length of Rect1: "))
r1.b=int(input("Enter breadth of Rect1: "))

r1.display()    
r2.display()



# BankAcc - AccNo, AccName, AccBal
# deposit(self, amnt), withdraw(self, amnt), accinfo(self)

# Box  - l, b, h , vol()

class bankAcc:
    def __init__(self,acc_name,acc_bal):
        self.acc_name = acc_name
        self.acc_bal = 