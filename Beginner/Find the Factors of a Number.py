#will only print the numbers completely divisible by 12

factor = []

n= int(input("please enter the number: "))

for i in range( 1,n+1):
    if n%i == 0:
        factor.append(i)

print(factor)
