import random
x = int(input("Enter your number : "))

y = random.randint(1,10)

if x == y :
    print("You have won!")
else:
    print("You lose!")

print(f"The random value is : {y}")