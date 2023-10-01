#Infinite Loop

# while True:
#     print("I am Jim")

#It will keep printing forever

#Use of break

# while True:
#     n = int(input("Enter a number:"))
#     if n>0:
#         print("positive")
#     elif n<0:
#         print("Negative")
#     else:
#         break;
#

#another break example:

# count =0
#
# while count <10:
#     print(count)
#     count = count +1
#     if count > 5:
#         break


# continue examples
# count = 0
#
# while count < 10:
#     n = int(input("enter a number"))
#
#     if n%3 ==0:
#         print(n, "will not be counted")
#         continue
#
#     print(n)
#     count += 1

# #it will not print the numbers divisible by 3 as it will not excute
#  print when the numbers divisible by 3 appears.
# so continue will take me back to lopp instead of the next Line


# Pass - when we want to do nothing
#if number is divisible by 3 I will do nothing

count = 0
while count < 10:

    n = int(input("enter a number"))

    if n%3 ==0:
       pass
    else:
        print(n)
        count += 1

# we could've done this without using pass by changing the condition
#
#  if n%3 !=0:
#      print(n)

