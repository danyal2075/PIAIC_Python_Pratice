# https://www.w3schools.com/python/python_strings_slicing.asp


# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# the end index is -1

math = [11, 22, 33, 44, 55, 66, 77, 88, 99]


#Slicing
print("********************************")
print("1")
print("Slicing Part : ", math[2:6])
eng = math[2:6]
print("List : ",math)
print(eng)
print("")

# Slice From the Start
print("********************************")
print("2")
print("List : ",math)
print("Slicing from the start : ", math[:6])
print("")

# Slice to the End
print("********************************")
print("3")
print("List : ",math)
print("Slicing to the end : ", math[6:])
print("")

# Negative Indexing
print("********************************")
print("4")
print("List : ",math)
print("Negative Slicing : ", math[-5:-1])
print("")

# Step Slicing
print("********************************")
print("5")
print("List : ",math)
print("Step Slicing : ", math[1:6:2])
print("Step Slicing : ", math[::2])
print("Reverse Step Slicing : ", math[:-1:2])
print("")