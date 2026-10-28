class Employee:
    def __init__(self):
        self.start_time = 9
        self.end_time = 5


class AdmiinStaff(Employee):
    def __init__(self, role):
        super().__init__()
        self.role = role


class AccountingStaff(AdmiinStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

print("-----Accessing the details of AccountingStaff class using multi-level inheritance of AccountingStaff, AdmiinStaff and Employee class -----")
acc1 = AccountingStaff(50000, "Accountant")           
print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)