# we take input values from the user but the problem is input value is always a str so that cannot be add. 
# In this case we use typecating. means we change the data type of the variable.
#if we donnot change the data type then the two variables will be concetenate. 
#




num1 = input("Enter the first value :")
num2 = input("Enter the second value :")
result = int(num1) + float(num2)
print(result)