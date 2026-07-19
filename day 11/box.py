# Box : length, breadth, height , 
# area(), vol()

class box:
    
    def __init__(self,l=1,b=1,h=1):
        self.__length=l
        self.__breadth=b
        self.__height=h
        
    def __str__(self):
        return f"The length of box is : {self.__length}\nbreadth of box : {self.__breadth}\nhieght of box : {self.__height}"
    
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
        self.__breadth = value
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        self.__height=value
        
    def area(self):
        return 2*(self.__length+self.__breadth+self.__height)
    
    def volume(self):
        return f"The volume is : {self.__length*self.__breadth*self.__height}"

# object creation  
b1 = box(10,20,30)

# print object 
print(b1)

b1.length = 20
b1.breadth = 10
b1.height = 5

print(f"the area is :- {b1.area()}")
print(f"The volume of box :- {b1.volume()}")
