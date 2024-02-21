from collections import deque
L= [1,2,3,4,5]
q = deque(L)

print(q)

(q.append(6))
print(q)

q.appendleft(4)
print(q)
print(q.pop())
print(q.popleft())
q.extend([10,20,30,40,50])
print(q)
q.rotate(2)
print(q)