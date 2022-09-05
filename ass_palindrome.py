
number = "civic"
j = -1
flag= 0
for i in number:
    print("i: ",i)
    if i == number[j]:
        j = j-1
    else: 
        flag = 1
        break
if flag == 1:
    print("This is not plindrom")
else :
    print("This is plindrom")


