# https://www.w3schools.com/python/python_tuples.asp
# Tuples are used to store multiple items in a single variable
# Tuple items are ordered, unchangeable, and allow duplicate values.
# 

# We use tuples for constant value like pi, speed of light etc sometimes we need constant value then we use tuples.


city = ('karachi', 'city of lights')
diff_data_type = ("multan0", 1, 2, False)
print("Tuple with different data type : ", diff_data_type)
print("City : ",city)

# Tuples constructor and just one item in the tuple 
print("")
print("**************************************")
print("1")
capital =  tuple(("Islamabad0", "capital of pakistan"))
t_oneitem = ('peshawar',)
print("Tuple Constructor : ", capital)
print("Tuple With one item : ", t_oneitem)

# To check the length
print("")
print("**************************************")
print("2")
print("Length of tuple : ",len(capital))
print("ID of the tuple : ", id(capital))

