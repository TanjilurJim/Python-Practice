import heapq

def Kthlargest(l, k):
    sorted_list = []
    for i in l:
        heapq.heappush(sorted_list,-i)

    for i in range(k-1):
        heapq.heappop(sorted_list)


    return -heapq.heappop(sorted_list)







l = [11,13,41,21,345,6871,1]

print(Kthlargest(l,1))


