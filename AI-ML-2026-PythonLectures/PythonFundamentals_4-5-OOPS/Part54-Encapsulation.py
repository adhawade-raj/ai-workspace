
class BankAccount:

    def __init__(self,name, balance, pin):
        self.name=name #public
        self._balance=balance #protected
        self.__pin=pin #private


    def get_pin(self):
            return self.__pin #getter method to access the value of private variable

    def set_pin(self, new_pin):
        self.__pin=new_pin #setter method to change the value of private variable

print("Encapsulation in Python")

acc1= BankAccount("John", 1000, 1234)
print(acc1.name) #public
print(acc1._balance) #protected
print(acc1.get_pin()) #private

print("-----Changing the value of private variable using setter method-----")
acc1.set_pin(4321) #changing the value of private variable using setter method
print(acc1.get_pin()) #private



print("-----Accessing private this way will not print the value of pin-----")
print(acc1.__pin) #private