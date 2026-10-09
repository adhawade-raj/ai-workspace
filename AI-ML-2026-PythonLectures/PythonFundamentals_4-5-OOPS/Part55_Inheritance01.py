class Employee :

    start_time = 9
    end_time = 5

class Teacher(Employee) :
    def __init__(self, subject) :
    
        self.subject = subject

    def get_details(self) :
        return f" Subject: {self.subject}" 


t1 = Teacher("Maths")

print("-----Accessing the details of Teacher class using inheritance of teacher and employee class -----")
print(t1.get_details(), t1.start_time, t1.end_time)       