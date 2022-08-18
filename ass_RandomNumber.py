import random
lis = []
li = []

for i in range(100):
    x = random.randint(10,100)
    if x >= 50:
        continue
    lis.append(x)

print("This is going to print less than 50")
print("Length : ",len(lis))
print("The list is : ",lis)
print("")
print("")



for i in range(100):
    y = random.randint(10,100)
    if y < 50:
        continue
    li.append(y)

print("This is going to print higher than 50")
print("Length : ",len(li))
print("The list is : ", li)