


def add(num1 , num2 ):
    return num1 + num2
    

def subtract(num1 , num2):
    return num1 - num2
    

def calculator(n1 , n2, op):
    if op == "+":
        print(add(n1 , n2))
    elif op == "-":
        print(subtract(n1 , n2))
    else:
        print("Wrong Operator")

calculator(2,5,"-")
