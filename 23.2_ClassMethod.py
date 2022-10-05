# Class Method is used when class variables we want to change.

class Employee():
    increment_salaries  = 1.5 
    no_employees = 2
    def __init__(self, fname, lname ):
        self.fname = fname
        self.lname = lname
        
    def info_employee(self, salary, age, address):
        self.salary = salary
        self.age = age
        self.address = address
        
    def increase(self):
        self.salary = self.salary * self.increment_salaries
    @classmethod
    def increment_salary(cls, amount, emp):
        cls.increment_salaries = amount
        cls.no_employees = emp



sohail = Employee("Sohail", "Danyal")
hamza =  Employee("Hamza", "Mehran")
sohail.info_employee( 250, 28, "Germany")
hamza.info_employee("25k", 22, "England")
Employee.increment_salary(2, 5)
sohail.increase()




print(f"Student name is {sohail.fname} {sohail.lname} his age is {sohail.age}. He live {sohail.address} and his salary is {sohail.salary}. {sohail.no_employees}")
print(f"Student name is {hamza.fname} {hamza.lname} his age is {hamza.age}. He live {hamza.address}.")