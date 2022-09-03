import random

org_list = []
# How to find min

for i in range(100):
    l =  random.randint(10,100)
    org_list.append(l)
print("Orginal List" , org_list)
_min = org_list[0]
print("min",_min)
print("We are printing via i")
for i in org_list:
    print(i)
    if _min < i:
        continue
    print("Here is the min value")
    _min = i
print("_min",_min)
print("Maximum : ", min(org_list))


