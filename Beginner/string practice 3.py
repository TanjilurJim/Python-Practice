#take a string as an input and print which letter is there how many times

str= input("please enter a line: ")
s = str.split()
print(s)

for i in str:
    print(i, str.count(i))