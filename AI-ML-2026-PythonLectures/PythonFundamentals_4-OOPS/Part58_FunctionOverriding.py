class Employee:
    def get_designation(self):
        print("designation of employee is: Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation of employee is: Teacher")

t1 = Teacher()
print("-----getting values from teacher class as we overridden the method in teacher class-----")
t1.get_designation()

print("-----Duck Typing-----")
def print_designation(emp):
    emp.get_designation()

e1 = Employee()
print_designation(e1)
print_designation(t1)
