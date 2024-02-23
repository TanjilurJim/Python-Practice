import bisect


def insertion_sort(l):
    sorted_list = []
    for i in l:
        bisect.insort(sorted_list,i)

    return sorted_list







 

l = [2,4,6,8,10,1,3,5,7,9]
print(insertion_sort(l))
