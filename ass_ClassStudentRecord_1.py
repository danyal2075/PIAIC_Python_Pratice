class Student():
    counter = 0
    def __init__(self):
        self.name = input("Enter your Name : ")
        self.course = input("Enter Your Course : ")
        Student.counter += 1
    def result(self):
        print(f"Name : {self.name} and Course : {self.course}")


st1 = Student()
st3 = Student()
st2 = Student()

st1.result()
st2.result()
st3.result()
print("Number of Student :", Student.counter)
