# This program is writtten to store the data of the students. 
student_name = []
student_info = [
    {
      "name":"",
      "age":"",
      "gender":"",
      "course":{
        
      },  
    },
    {
      "name":"",
      "age":"",
      "gender":"",
      "course":{
        


      },  
    },
    {
      "name":"",
      "age":"",
      "gender":"",
      "course":{
        

      },  
    },
    {
      "name":"",
      "age":"",
      "gender":"",
      "course":{
        

      },  
    },
]
for i in range(4):
    print(i)
    name  = input("Enter your name : ").title()
    age  = input("Enter your age : ").title()
    gender  = input("Enter your gender : ").title()
    
    
    student_name.append(name)
    student_info[i]["name"] = name
    student_info[i]["age"] = age
    student_info[i]["gender"] = gender
    print("Please select your course in one of the following")
    print(f"\n 1) AI \n 2) IOT \n 3) Metaverse")
    for cou in range(1,4):  
        course  = input("Enter your course : ").upper()
        if course == "Q":
            break
        student_info[i]["course"][f" Subject_{cou}"] = course
print(student_name)
print("-" * 10)
for j in student_info:
    
    for k,v in j.items():
        print(f"{k} : {v}")
    print("-" * 10)   