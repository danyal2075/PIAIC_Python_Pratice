# https://www.w3schools.com/python/python_lists.asp

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.


                                                                    #List Items 
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

                                                                    #Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list

                                                                    #Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

                                                                    #Allow Duplicates
#Since lists are indexed, lists can have items with the same value

                                                                    #List Items - Data Types
# List items can be of any data type:
# A list can contain different data types:


temp = [12, 15, 14, 65, 45, 60]
clas = list((10, 78, 65, 35, 65)) # Creating list via list constructor
x = [12, 12, 12, 12] # We can add same value in the list. Duplicate
y = [12, "apple", 45, 85, "Banana", True] # Item list can be different data type
print("**************************************")
print("1")
print("temp : ",temp)
print("clas : ",clas)
print("x : ",x)
print("y : ",y)
print("")

# To access a specific value
print("**************************************")
print("2")
print("Access the 3 index : ", temp[2])
print("Access the last index : ", temp[-1])
print("")

# To check the length of list
print("**************************************")
print("3")
print("Length of the temp :", len(temp))
print("Length of the clas :", len(clas))
print("Length of the x :", len(x))
print("Length of the y :", len(y))
print("") 

# To check the data type
print("**************************************")
print("4")
print("To check the data type : ",type(clas))
print("")

# To replace the value of the index
print("**************************************")
print("5")
temp[4] = "Apple"
temp[5] = 100
print("temp : ",temp)
print("")

# To add new value to the list
print("**************************************")
print("6")
print("Class : ",clas)
z = 100
clas.append(15)
clas.append(z)
print("clas : ",clas)
print("Length of the clas :", len(clas))
print("")

# To combine two list.
print("**************************************")
print("7")
combined_list = clas + temp
print("Combined temp and clas : ", combined_list) 
print("")
#combined_lis = clas.append[12, 15, 14, 65, 45, 60] # see the result it gives different.
#combined_lst = clas.extend[12, 15, 14, 65, 45, 60] # i put the temp value in the braces.
print("")

# to have one list in another
print("**************************************")
print("8")
mat = [12, 13, 14,[15, 16, 17], 18, 19]
print("List mat : ", mat)
print("The inner list : ", mat[3]) 
print("Acces the index 1 of the inner matrix : ", mat[3][1]) 
print("")


# To insert value to the list
print("**************************************")
print("9")
eng = [1, 2, 3, 4, 5]
print("List eng : ", eng)
eng.insert(2,100)
print("List eng : ", eng)
print("")

# To find the index of the item.
print("**************************************")
print("10")
print("List eng : ", eng)
print("The index of 4 is :", eng.index(4))
print("")

#  to remove the items and rmeove index
print("**************************************")
print("11")
print("List eng : ", eng) 
eng.remove(5)
print("List updated eng : ", eng) 
eng.pop(1)
print("List updated eng : ", eng)
print("")

#Reverse the List
print("**************************************")
print("12")
maths = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print("math : ", maths)
maths.reverse()
print("Reversed maths : ", maths) 
print("")