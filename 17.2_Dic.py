# we can store a dic or list or tuple by one id


employee  = {
            "Name":"Sohail",
            "FatherName":"Qamar",
            "Education":["Mater of Media Technology", "B.Sc in Electrical Engineering ", "F.Sc Science Pre Engineering"],
            "Age":"28",
            "Hobbies":("Cricket", "Football", "Mobile Games", "Reading Books")


}

print(employee)
for i,l in employee.items():
    print(i,":",l)
print("_" * 10)
for edu in employee["Education"]:
    print(edu)


print("_" * 10)
for dic in  employee["Hobbies"]:
    print(dic)