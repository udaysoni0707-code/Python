#BankAcc : Accno, AccName, Balance , deposit(), withdraw(), accinfo(), getbal()

class BankAcc:
    counts=0
    
    def __init__(self,accno=0,accname="",balance=0):
        self.__accountno=accno
        self.__accountname=accname
        self.__accountbalance=balance
        BankAcc.counts+=1
        self.__srno=BankAcc.counts
        
    def __str__(self):
        return f"Registration No : {self.__srno}\nAccount No : {self.__accountno}\nAccount Name : {self.__accountname}\nBalance : {self.__accountbalance}"    
    @property
    def deposit(self):
        return self.__accountbalance
    
    @deposit.setter
    def deposit(self, value):
        if value > 0:
            self.__accountbalance += value
        else:
            print("Invalid Deposit Amount")
        
    @property
    def withdraw(self):
        return self.__accountbalance
    
    @withdraw.setter
    def withdraw(self,value):
        if value <= self.__accountbalance:
            self.__accountbalance -= value
        else:
            print("insufficient balance")
    
    @property
    def accinfo(self):
        return (self.__accountno,
                self.__accountbalance,
                self.__accountname)
        
    @accinfo.setter
    def accinfo(self, value):
        accno, accname, balance = value
        self.__accountno = accno
        self.__accountname = accname
        self.__accountbalance = balance
        
    @property
    def getbal(self):
        return self.__accountbalance
    
