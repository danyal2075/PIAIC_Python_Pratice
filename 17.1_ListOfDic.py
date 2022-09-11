# we can store data of an organisation

all_student = {
    {
        "Name":"Sohail",
        "age":"28",
        "Residence":"Germany",
        "Edu":"master",
        "nationality":"Pakistani"

    }
    ,
    {
        "Name":"Danyal",
        "age":"27",
        "Residence":"Germany",
        "Edu":["Master of MT","B.Sc in Electrical Engineering", "F.Sc Science ", "PIAIC Artificial Intelligence"]

    }
    ,
    {
        "Name":"Hamza",
        "age":"22",
        "Residence":"England",
        "Edu":"ACCA",
        "Hobbies":("Cricket", "Football", "Mobile Games", "Reading Books")


    }


}
print(all_student)


# Printing just one key in a specific dic
print("")
print("**************** 1")
print("Dic 0 key 1 :",all_student[0]["Name"])

# Adding new Dic

all_student.append({
    "Name":"Qamar",
    "Age":"58",
    "Residence":"Pakistan",
    "Educaion":"B.Com"

})

# Printing one dic
print('') 
print("**************** 2")
print("Sohail Data :",all_student[0])
print("Danyal Data :",all_student[1])

print("Hamza Data :",all_student[2])
print("Hamza Data :",all_student[3])

# Printing Dic via for loop
print('') 
print("**************** 3")

for i in all_student:
    print(i)

print("*" * 10)
for i in all_student:
    for k, v in i.items():
        print(f"Keys : {k},  Value : {v}")

    print("-" * 10)


print("*" * 10) 
for i in all_student:
    for k, v in i.items():
        print(k ,":",v)

    print("-" * 10)


# Methods
print('') 
print("**************** 4")
print(len(all_student ))

# to get info from dic in dic
print('') 
print("**************** 5")
print(all_student[3]["Hobbies"])