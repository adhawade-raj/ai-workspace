print("==========Student class with constructor=====================")
class Student :
    def __init__(self):
        print("This is the constructor of Student class")

stu1 = Student()  
stu2 = Student() 
stu3 = Student()       

print("==========Employee class with constructor=====================")
class Employee :
    def __init__(self, name, age):
        self.name = name
        self.age = age

emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 25)
emp3 = Employee("Charlie", 35)

print("Employee names & ages are:")
print(emp1.name, emp1.age)
print(emp2.name, emp2.age)
print(emp3.name, emp3.age)

  