# 1.	Implement a Student class with __init__ and __str__ methods that displays the student’s name and grade.

class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        
    def __str__(self):
        return (f"student Name : {self.name} ,grade : {self.grade}")
        
obj = student("indrayani", "A+")
print(obj)