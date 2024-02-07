def sum0(L):
    summation = 0
    for i in L:
        if i%10 == 0:
            summation +=i

    return summation



l = [1,34,20,453,6543,67,10]
print(sum0(l))




