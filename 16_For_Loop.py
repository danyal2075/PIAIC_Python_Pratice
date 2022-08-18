# https://www.w3schools.com/python/python_for_loops.asp
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)


fruits  = ["banana", "mango", "apple", "cheery"]

for i in fruits:
    print("Fruits : ",i)


# Looping via string
#x = "banana"
print("")
print("**************************************")
print("1")
for x in "banana":
    print(x)

# The break statement 
print("")
print("**************************************")
print("2")
for i in fruits:
    print(i)
    if i == "apple":
        break
print("The loop is break")
print("")
for i in fruits:
    if i == "apple":
        break

    print(i)


# Continue Statement
print("")
print("**************************************")
print("3")
for i in fruits:
    if i == "apple":
        continue
    print(i)

# Range Function
print("")
print("**************************************")
print("4")
for i in range(6):
    print("Code inside this loop will run six times")
print("")
for i in range(2,6):
    print("The starting value is 2")

print("")
for i in range(0,30,3):
    print(i)

#Else in far loop
# Else will not be exucated if the loop is break
print("")
print("**************************************")
print("5")
for i in range(6):
    print(i)
else:
    print("Finally finished")
print("")


for i in range(6):
    if i == 4: break
    print(i)
else:
    print("Finally Finished")

# nested loop
print("")
print("**************************************")
print("6")
adj = ["red", "big", "tasty"]
fruit = ["apple", "banana", "cherry"]

for i in adj:
    for x in fruit:
        print(i,x)

# pass statement
print("")
print("**************************************")
print("7")
for x in range(4):
    pass


   