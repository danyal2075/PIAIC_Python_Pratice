# This is how orginasation stores their data.

employee = [
    {
        "employeeID":1,
        "name":"sohail danyal",
        "fathername":"Qamar Zaman",
        "Job":"Pick",
    },
    {
        "employeeID":2,
        "name":"sohail danyal",
        "fathername":"Qamar Zaman",
        "Job":"Pick",
    },
    {
        "employeeID":3,
        "name":"sohail danyal",
        "fathername":"Qamar Zaman",
        "Job":"Pick",
    }



]
id = int(input("Input your id number : "))
details = None
for i in employee:
    #   print(i)
    if i["employeeID"] == id:
        details = i
        break
#for j, k in details.items():
#    print(j,"  :  ",k)

print(details)

