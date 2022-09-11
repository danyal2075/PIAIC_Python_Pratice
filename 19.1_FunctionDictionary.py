def dictionary(**numbers):
    print(numbers)  # This gives the value in the dic
    sum = 0
    for i in numbers.values():
        sum += i
        #sum += sum
    print(sum)

#dictionary(n1 = 10, n2 = 20, n3 = 20)

def tuple(*numbers):
    print(numbers)  # This gives the value in the tuple
    sum = 0
    for i in numbers:
        sum += i
        #sum += sum
    print(sum)

dictionary(n1 = 10, n2 = 20, n3 = 20)
tuple(20,10,30)