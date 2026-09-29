class Student :
    colleg_name = "ABC College"  # class attribute
    PI=3.14  # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age    # instance attribute
        self.PI = 3.14      # instance attribute

student1 = Student("John", 20)

print("---------Student name & age are from instance attributes :-----------")
print(f"Name: {student1.name}, Age: {student1.age}")

print("---------Student college name is from class attributes :-----------")
print(f"College: {Student.colleg_name}")


print("---------Instance value will be preferred over class if attribute is same-----------")
print(f"PI: {student1.PI}")