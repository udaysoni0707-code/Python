#Assignments: class , side1, 
# side2, side3, side4, 
# function : perimeter()

class assignment:
    
    def __init__(self,a,b,c,d):
        self.__sideA=a
        self.__sideB=b
        self.__sideC=c
        self.__sideD=d
        
    def __str__(self):
        return f"Perimeter of class is :- {self.__sideA}+{self.__sideB}+{self.__sideC}+{self.__sideD}"
    
    @property
    def sideA(self):
        return self.__sideA
    
    @sideA.setter
    def sideA(self,value):
        self.__sideA = value
        
    @property
    def sideB(self):
        return self.__sideB
        
    @sideB.setter
    def sideB(self,value):
        self.__sideB = value
        
    @property
    def sideC(self):
        return self.__sideC
    
    @sideC.setter
    def sideC(self,value):
        self.__sideC = value
        
    @property
    def sideD(self):
        return self.__sideD
    
    @sideD.setter
    def sideD(self,value):
        self.__sideD = value
        
    
    def perimeter(self):
        return (self.__sideA+self.__sideB+self.__sideC+self.__sideD)
        

# object creation
a1 = assignment(12,13,14,15)

# print object 
print(a1)

# set side A 
a1.sideA = 10

# set side B
a1.sideB = 20

# set side C
a1.sideC = 10

# set side D 
a1.sideD = 20 

# perimeter of class
print(f"The perimeter is :- {a1.perimeter()}")