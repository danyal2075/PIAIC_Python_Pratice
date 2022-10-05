class Employee():
    increment_salaries  = 1.5 
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
    def increment_salary(cls, amount):
        cls.increment_salaries = amount
    @classmethod
    def class_method_as_constructor(cls, _str):
        fname, lname = _str.split("-")
        return cls(fname, lname)

class Programmer(Employee):
    def __init__(self, fname, lname, exp, prolang):
        super().__init__(fname, lname)
        self.exp = exp
        self.prolang = prolang
    

sohail = Programmer("sohail", "danyal", "5 yrs", "Python")
print(sohail.fname, sohail.prolang)