class Rect:
    counts=0 # class attribute it increased on creation of every object
    #count is common for all objects its last value retain in multiple function
    #call it is like a global variable
    
    def __init__(self,l=1,b=1): # here l and b are local variable
        self.__length=l
        self.__breadth=b
        Rect.counts+=1
        self.__srno=Rect.counts

    def __str__(self):
        return f"Dimension of Rect{self.__srno} is {self.__length}x{self.__breadth}"

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self,value):
        self.__length=value

    @property
    def breadth(self):
        return self.__breadth

    @breadth.setter
    def breadth(self,value):
        self.__breadth=value

    def area(self):
        return self.__length*self.__breadth
    
    #length=property(get_length,set_length)
    #breadth=property(get_breadth, set_breadth)


#BankAcc : Accno, AccName, Balance , deposit(), withdraw(), accinfo(), getbal()
# Distance : feet, inch, AddDistance() used to add 2 distance objects
# Box : length, breadth, height , area(), vol()

    
    
