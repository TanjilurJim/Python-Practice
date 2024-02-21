import bisect

l = [10,20,20,30,40,50,60,70,80,90]

bisect.insort(l,25)
print(l)

bisect.insort(l,90)
print(l)
print(id(l[11]))
print(id(l[10]))


print(bisect.bisect(l,35))
print(bisect.bisect_right(l,20))
  