#0,1,1,2,3,5,8,13,21,34

#we have to generate this series


n = int(input("the number of terms"))

a = 0

b =1

series = []
for i in range(n):
    series.append(a)
    c = a+b
    a=b
    b=c

print(series)


