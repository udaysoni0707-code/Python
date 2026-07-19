class Student:

    def __init__(self, name):
        self.name = name

    def change(self):
        self.name = "Aman"

    def display(self):
        print(self.name) 

s1 = Student("Uday")

s1.display()
s1.change()
s1.display()