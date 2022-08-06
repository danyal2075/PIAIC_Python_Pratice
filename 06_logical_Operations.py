                                                # Logical Operator


x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))

# Returns True if both statements are true
if x > 5 and x < 10:
    print("X is between 5 and 10")

#Returns True if one of the statements is true
elif x == 4 or y < 5:
    print("X is equal to 4 or y is less than 5")

#Reverse the result, returns False if the result is true
elif not(x == 3 or y < 5):
    print("X is not equal to 4 or y is  not less than 5")