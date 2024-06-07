def linear_search(L,x):
    #S.C = O(1)
    #T.C - O(n)
    for i in range(len(L)):
        if L[i] == x:
            return i

    return -1






L=[1,2,3,4,5,563,1431,2435,7347,14,21]
print(linear_search(L,23))
