#the reverse of a number == original i.e 1221 is same reverse
#need to check if a number is same reverse or not

n=int(input("please enter a number:"))
m =n
rev = 0
while n>0:
    r = n%10
    n= n//10
    rev = rev*10+r

if rev == m:
    print(m,"is palindrome")
else:
    print(m,"is not a palindrome")
print(rev)