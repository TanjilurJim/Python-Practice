def bubble_sort(L):
    #T.C = O(n)
    n=len(L)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if L[j] > L[j+1]:
                tmp = L[j]
                L[j],L[j+1] = L[j+1],tmp
                swapped = True

        if not swapped:
            break






if __name__ =="__main__":
    L=[6,1,4,9,2]
    print("before sort:", L)
    bubble_sort(L)
    print("After sort:", L)


