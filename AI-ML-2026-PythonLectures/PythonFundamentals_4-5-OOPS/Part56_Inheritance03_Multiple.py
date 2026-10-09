class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TeachingAssistant(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa) 
        self.name = name  

t1 = TeachingAssistant(50000, 3.8, "John")
print("-----Accessing the details of TeachingAssistant class using multiple inheritance of Teacher and Student class -----")
print(t1.name, t1.salary, t1.gpa)             