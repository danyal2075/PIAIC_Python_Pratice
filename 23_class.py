class Patient():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.ward = None

    def admission(self,wardname):
        self.ward = wardname
    
human = Patient("sohail", 28)
print(f"My name is {human.name} and my age is {human.age}. He is admitted in ward :{human.ward} ") 
human.admission("Gestro")
print(f"Human {human.name} is now admiited in ward : {human.ward}" )

# change the value of the attribute

human.ward  = "Kidney"
print(f"Human {human.name} is now admiited in ward : {human.ward}" )
human.admission("Brain")
print(f"Human {human.name} is now admiited in ward : {human.ward}" ) 