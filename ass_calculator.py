from multiprocessing.connection import answer_challenge
from tkinter import Y


x = int(input("Enter the 1st value : "))
oper = input("Enter the operator : ")
y = int(input("Enter the 2nd value : "))

if oper == "+":
    answer = x + y  
    print(f"Answer : {answer}")

if oper == "-":
    answer = x - y  
    print(f"Answer : {answer}")

if oper == "*":
    answer = x * y  
    print(f"Answer : {answer}")

if oper == "/":
    answer = x / y  
    print(f"Answer : {answer}")