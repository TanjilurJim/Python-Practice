def binary_search(L,x):
    left,right = 0, len(L)-1

    while left <= right:
        mid = (left + right)//2

        if L[mid] == x :
            return mid

        if L[mid] < x:
            left = mid +1
        else:
            right = mid -1
    return -1


L = []
for i in range(1,51):
    L.append(i)
print(L)

print(binary_search(L,20))