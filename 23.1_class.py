class Student():

    def __init__(self, fname ,lname):
        self.fname = fname
        self.lname = lname

    def info(self, std, age, address, **kwords):
        self.age = age
        self.std  = std
        self.address = address
        self.course = kwords
        
         
        

    


sohai = Student("Sohail", "Danyal")
hamza  = Student("Hamza", "Mehran")
# student.name = "sohail"

#print(sohai.name)
sohai.info("Master", "45", "Germany", "IOT", "AIC", "CC")
print(f"Student name is {sohai.fname} {sohai.lname} his age is {sohai.age}. He studies in {sohai.std} and live {sohai.address}. He takes course of {sohai.course}")
hamza.info("ACCA", "56", "England")
print(f"Student name is {hamza.fname} {hamza.lname} his age is {hamza.age}. He studies in {hamza.std} and live {hamza.address}. He takes course of {hamza.course}")
#print(hamza.name)
#print(sohai.std)