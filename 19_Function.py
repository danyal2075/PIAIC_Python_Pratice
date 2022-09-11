def space(method):
    print("")
    print("*" * 20, method)


def addition(num1, num2):
    print(num1 + num2)
addition(10,30)

def repeat_a_string(content, times):
    print(content * times)
repeat_a_string("*",20 )

def repeat_a_string():
    content = "*"
    times = 20
    print(content * times)
repeat_a_string() 


# Giving default value to the varaible.
# if we donot give any value to the variable it will take the default value given in the argument
space(1)
def repeated_a_string(content, times = 30):
    print(content * times)
repeated_a_string("@", 20)
repeated_a_string("@")