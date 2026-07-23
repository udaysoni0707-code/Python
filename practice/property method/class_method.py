class Student:
    
    school = "ABC School"
    
    def __init__(self,name):
        self.name = name 
        
    def show(self):
        print(f"The name is :- {self.name}")
        
    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school
        
s1 = Student("Uday")
s2 = Student("Rahul")

print(Student.school)
# ABC School

Student.change_school("XYZ School")

print(Student.school)
# XYZ School

print(s1.school)
# XYZ School

print(s2.school)
# XYZ School

# question 2 

class Employee:
    company = "Google"
    
    def __init__(self,name , salary):
        self.__name = name 
        self.__salary = salary
        
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        
e1 = Employee("Uday", 50000)
e2 = Employee("Rahul", 60000)

print(e1.company) # Google

Employee.change_company("Microsoft")

print(e1.company) # Microsoft
print(e2.company) # Microsoft
print(Employee.company) # Microsoft

# question 3 
class Bank:
    bank_name = "SBI"
    
    def __init__(self,name, balance):
        self.__name = name 
        self.__balance = balance
        
    @classmethod
    def change_bank(cls,new_bank):
        cls.bank_name = new_bank
        
b1 = Bank("Uday", 10000000)
b2 = Bank("Rahul", 20000000)

print(f"The name of bank :- {b1.bank_name}")
# SBI

Bank.change_bank("HDFC")

print(f"After the changing name of bank :- {b1.bank_name}")
# HDFC

print(f"After the changing name of bank :- {b2.bank_name}")
# HDFC

# question 4

class Mobile:
    brand = "Samsung"
    
    def __init__(self,model,price):
        self.model = model
        self.price = price
        
    @classmethod
    def change_brand(cls,new_brand):
        cls.brand = new_brand
        
m1 = Mobile("S23", 70000)
m2 = Mobile("A56", 35000)

print(m1.brand)

Mobile.change_brand("Apple")
print(m1.brand)
print(m2.brand)
print(Mobile.brand)

# question 5
class Car:
    total_cars = 0 
    def __init__(self,brand):
        self.brand = brand
        Car.total_cars+=1
    
    @classmethod
    def show_total_cars(cls):
        print(f"Total Cars = {cls.total_cars}")        
c1 = Car("BMW")
print(c1.brand)
c2 = Car("Audi")
print(c2.brand)
c3 = Car("Toyota")
print(c3.brand)

Car.show_total_cars()

# question 6
class Employee:
    company = "Google"
    employee_count = 0
    
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
        Employee.employee_count+=1
        
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        
    @classmethod
    def show_details(cls):
        print(Employee.company)
        print(Employee.employee_count)
        
e1 = Employee("Uday", 50000)
e2 = Employee("Rahul", 60000)
e3 = Employee("Aman", 70000)

Employee.change_company("Microsoft")

Employee.show_details()

# question 6
class Book:
    library = "Central Library"
    
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    @classmethod
    def change_library(cls,new_library):
        Book.library = new_library
        
    @classmethod
    def show_library(cls):
        print(cls.library)
        
b1 = Book("Python", "Guido")
b2 = Book("Java", "James")

Book.show_library()
Book.change_library("City Library")
Book.show_library()
print(b1.library)
print(b2.library)

b1.library = "My Library"

print(b1.library)
print(b2.library)
print(Book.library)

# question 7 
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

    @classmethod
    def anonymous(cls):
        return cls("Anonymous", 0)
    
    @classmethod
    def demo(cls):
        return cls("Uday",21)
    
user1 = User("Asha", 25)
user2 = User.from_dict({"name": "Ravi", "age": 30})
user3 = User.anonymous()
user4 = User.demo()

print(user1.name, user1.age)
print(user2.name, user2.age)
print(user3.name, user3.age)
print(user4.name, user4.age)