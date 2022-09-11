from winreg import ExpandEnvironmentStrings


expirement = {

    6062020 : {
        "employeeID":1,
        "name":"sohail danyal",
        "fathername":"Qamar Zaman",
        "Job":"Pick",
    },

    15062022 :{
        "employeeID":2,
        "name":"sohail danyal",
        "fathername":"Qamar Zaman",
        "Job":"Pick",
    },

    30072022 :{
        "employeeID":3,
        "name":"sohail danyal",
        "fathername":"Qamar Zaman",
        "Job":"Pick",
    }
}
#exp_key = int(expirement.keys())
#print(type(exp_key()))
info = None
exp_date = int(input("Enter the date of the expriment : " ))
for i in expirement:
    if i  == exp_date:
        information = i
        info =expirement[information]
        break
            

print(info)