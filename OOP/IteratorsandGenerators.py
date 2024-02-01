l = [1,2,3,4,5,6]

itr = iter(l)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

#Generator

def Days():
    L = ['sun', 'mon', 'tuesday ', 'wed', 'thursday', 'friday'
         ,'saturday']
    i = 0

    while True:
        x = L[i]
        i = (i+1)%7
        yield x

d = Days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

