# Distance : feet, inch, 
# AddDistance() used 
# to add 2 distance objects


class distance:
    
    def __init__(self,feet,inch):
        self.__dis_feet = feet
        self.__dis_inch = inch
        
    def __str__(self):
        return f"the distance in feet : {self.__dis_feet}\ndistance in inch : {self.__dis_inch}"
    
    @property
    def AddDistance(self):
        return (self.__dis_feet,
                self.__dis_inch )
        
    @AddDistance.setter
    def AddDistance(self,value):
        feet, inch = value
        self.__dis_feet += feet
        self.__dis_inch += inch
    
    @property
    def final_result(self):
        return (self.__dis_feet,
                self.__dis_inch)
        
# object Creation 
d1 = distance(100,200)

# print object 
print(d1)  

# Add distance 
d1.AddDistance = (100,50)
print(d1.final_result)