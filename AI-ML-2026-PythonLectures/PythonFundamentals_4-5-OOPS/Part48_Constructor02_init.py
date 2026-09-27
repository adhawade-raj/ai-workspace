class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

emp1 = Employee("Alice", 30)
emp2 = Employee("Bob", 25)
emp3 = Employee("Charlie", 35)

print("Employee names & ages are:")
print(f"Name: {emp1.get_name()}, Age: {emp1.get_age()}")