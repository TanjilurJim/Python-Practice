import heapq

H = []
heapq.heappush(H, 20)
heapq.heappush(H, 40)

print(H)

heapq.heappush(H,10)

print(H)

heapq.heappush(H,50)
print(H)
heapq.heappop(H)
print(H)

L = [50,30,20,1,234]
heapq.heapify(L)
print(L)

two_largest =heapq.nlargest(2,L)
print(two_largest)