# # question 1 
# class Student :
    
#     def __init__(self,naam):
#         self.__name = naam
        
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self,value):
#         naam = value
#         self.__name = naam
        
# s1 = Student("uday")
# print(s1.name)

# # question 2 ..
# class Employee:
#     def __init__(self,salary):
#         self.__sal = salary
    
#     @property
#     def salary(self):
#         return self.__sal
    
#     @salary.setter
#     def salary(self,value):
#         if value <= 0 :
#             print("Invalid Salaery..")
#         else:
#             self.__sal = value
#             print("Salary update...")
        
# e1 = Employee(10000)
# e1.salary = -90
# print(e1.salary)

# # question 3
# class Student:
#     def __init__(self,age=0):
#         self.__age_student = age
        
#     @property
#     def age (self):
#         return self.__age_student
    
#     @age.setter
#     def age (self,value):
#         if value < 18 :
#             print(f"Invalid age : {value}")
#         else:
#             self.__age_student = value
#             print(f"The age is valid : {value}")

# s1 = Student(18)
# s1.age = 19

# # question 4 

# class Rectangle:
    
#     def __init__(self,l=0,b=0):
#         self.__length = l
#         self.__breadth = b
        
#     @property
#     def length(self):
#         return self.__length
    
#     @length.setter
#     def length(self,value):
#         if value < 0:
#             print("invalid length")
#         else:
#             self.__length = value
#             print(value)
            
#     @property
#     def breadth(self):
#         return self.__breadth
    
#     @breadth.setter
#     def breadth(self,value):
#         if value < 0:
#             print("invalid")
#         else:
#             self.__breadth = value
#             print(value)
            
# r1 = Rectangle(10,5)

# r1.length = -2
# r1.breadth = 8

# print(r1.length)
# print(r1.breadth)

# # question 5 
# class Rectangle:
    
#     def __init__(self,l,b):
#         self.__length = l
#         self.__breadth = b
        
#     @property
#     def length(self):
#         return self.__length
    
#     @length.setter
#     def length(self,value):
#         if value < 0:
#             print("invalid length")
#         else:
#             self.__length = value
#             print(value)
            
#     @property
#     def breadth(self):
#         return self.__breadth
    
#     @breadth.setter
#     def breadth(self,value):
#         if value < 0:
#             print("invalid")
#         else:
#             self.__breadth = value
#             print(value)
            
#     @property
#     def area (self):
#         aera = self.__length*self.__breadth
#         return aera

# length = int(input("Enter Length: "))
# breadth = int(input("Enter Breadth: "))
# r1 = Rectangle(length,breadth)

# r1.length = 12
# r1.breadth = 12 
# print(r1.area)

# question 6

class Circle:
    
    def __init__(self,r=0):
        self.__radius = r
        
    @property
    def radius (self):
        return self.__radius
    
    @radius.setter
    def radius(self,value):
        if value <=0:
            print("Invalid Radius..")
        else:
            self.__radius = value
            print(f"The radius is valid :- {value}")
    
    @property        
    def area(self):
        a = (3.14 * self.__radius*self.__radius)
        return a
    
    @property
    def cirumference(self):
        c = (2*3.14*self.__radius)
        return c
    

c1 = Circle(5)

print(f"The area of circle is :- {c1.area}")
print(f"The cirumference of circle is :- {c1.cirumference}")

c1.radius = 10 

print(f"The area of circle is :- {c1.area}")
print(f"The cirumference of circle is :- {c1.cirumference}")
