#5,7,9,11,13.......
#we have to print n terms
#for example here the series has 5 terms. what would be 8th term ?

a = int(input("Enter the initial Term: "))

d = int(input("The common difference between terms: "))

n = int(input("Enter the term(th) you want to print"))

for i in range(a,a+n*d,d):
    print(i)

