class student:
    def __init__(self):
        print("constructor called .....")
        
s1 = student()

class Student:
    def __init__(self):
        print("Constructor")

print("Start")

s1 = Student()

print("Middle")

s2 = Student()

print("End")

'''
output :    start 
            constructor
            middle 
            constructor
            end
'''
