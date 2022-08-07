math = int(input("Enter the marks :"))
physics = int(input("Enter the marks :"))
chemistry = int(input("Enter the marks :"))
name = "sohail"
obt_marks = math + physics + chemistry
percentage = obt_marks/300*100
print("Percentage : ", percentage)


# we can also give str in the condition
if name == "sohail":
    print("sohail is present")
else:
    print("sohail is not present")

if percentage >= 90:
    print("You have gotten A+")
elif percentage >= 80:
    print("You have gotten A")
elif percentage >= 70:
    print("You have gotten B")
else:
    print("You have failed the course")
