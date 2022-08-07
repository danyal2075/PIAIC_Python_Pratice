# nestedif is used to make the logical operation (and) in sample way 


x = int(input("enter the value : "))
y = int(input("enter the value : "))
z = int(input("enter the value : "))
w = int(input("enter the value : "))




# these both will have same result.
# if x < 5 and y < 10:
if x < 5:
    if y < 10:
        print("this is a great idea")
    else:
        print("This is not a good idea")
else:
        print("This is not a good idea")