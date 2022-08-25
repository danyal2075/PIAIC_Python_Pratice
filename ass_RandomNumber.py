
import random
import statistics
org_list = []
lis = []
li = []
x = None


for i in range(100):
    x = random.randint(10,100)
    org_list.append(x)
    #print("Orginal List" , org_list)
    if x >= 50:
        continue
    lis.append(x)
    

print("The actual list is: ",org_list)
print("The size of actual list is: ",len(org_list))
print("The min value is : ", min(org_list))
print("The max value is : ", max(org_list))
summ = sum(org_list)
print("The sum of the list : ", summ)
length = len(org_list)
avg = summ / length
print("The avg is : ", avg)
print("The sorted List : ", sorted(org_list))
print("The median of the list : ", statistics.median(org_list))

print("")
print("")



print("This is going to print less than 50")
print("Length : ",len(lis))
print("The list is : ",lis)
print("Sum is : ",sum(lis))
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
print("Sum is : ",sum(li))

# Intersection

_intersection  = set(org_list).intersection(set(li))
print(f"These are the common values : {_intersection} \nThe length is : {len(set(org_list).intersection(set(li)))}")



