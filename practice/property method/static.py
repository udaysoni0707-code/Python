'''
@staticmethod ek aisa method hota hai jo class ke
andar logically belong karta hai, lekin use na 
object ki details chahiye hoti hain (self), na 
class ki details (cls).
'''
class Student:
    school = "ABC School"
    
    def introduce(self):
        return f"Student of {self.school}"
    
    @classmethod
    def