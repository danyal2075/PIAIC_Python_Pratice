def dictionary(**numbers):
    #print(numbers)  # This gives the value in the dic
    sum = 0
    for i in numbers.values():
        sum += i
        #sum += sum
    return numbers , sum


val_retrun =  dictionary(n1 = 10, n2 = 20, n3 = 20)
print(val_retrun)