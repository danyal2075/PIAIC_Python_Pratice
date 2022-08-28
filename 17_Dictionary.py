# https://www.w3schools.com/python/python_dictionaries.asp
# Dictionaries are used to store data values in key:value pairs
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries cannot have two items with the same key:






# Creating and Printing Dictionary
print("************** 1")
info =  {
        "frist_name":"sohail".title(),
        "last_name":"danyal".title(),
        "father_name":"qamar zaman".title(),
        "age":28,
        "dob":"02 jan 1994",
        5 : "We can pass digits as a key"

}
  
print("Record : ", info)
print("frist_name",info["frist_name"]) 


# updating and adding new element
print("")
print("*************** 2")
info["Natinality"] = "Pakistani"
info["frist_name"] = "Hamza Mehran"
print("Record : ", info)

# Deleting
print("")
print("**************3")
del info[5]
print("Record : ", info)


# how to get the values of the dic
print("")
print("*************** 3")
for i in info:
    print("Record", info[i])

print("***************")
for i in info.values():
    print("Record", i)
print("Record", info.values())
print("***************")
for i in info.keys():
    print("Record", i)
print("Record", info.keys())
print("***************")
for i in info.items():          # this convert dictionary into the tuple
    print("Record", i)
print("Record", info.items())
