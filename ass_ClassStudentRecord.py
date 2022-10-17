from mimetypes import init


class Student():
    def __init__(self,name,father_name,courses):
        self.name = name
        self.father_name = father_name
        self.courses = courses

        
    


student = Student("Sohail", "Qamar", "Artificial Intelligence" )
print(f"Your name is {student.name}. Your father name is {student.father_name} and registered course is {student.courses}")
