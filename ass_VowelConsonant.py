#statemnt = "This is sohail danyal"
statemnt = input("Enter your statement")
v_count = 0
c_count = 0
#vowel = ["a","e","i","o","u"]
#print(vowel)
for i in statemnt:
    #print(i)
    if i == "a":
        v_count += 1
        #print("This is a")
    elif i == "o":
        v_count += 1
        #print("This is o")
    elif i == "i":
        v_count += 1
        #print("This is i")
    elif i == "e":
        v_count += 1
    elif i == "u":
        v_count += 1
    else:
        c_count += 1 
print("Vowels : ", v_count)
print("Consonant : ", c_count)
print(len(statemnt))