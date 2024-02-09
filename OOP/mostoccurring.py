
# to count how many times each word appears
# def counts(l):
#     result = []
#     for i in l:
#         cnt = l.count(i)
#         if (i,cnt) not in result:
#             result.append((i,cnt))
#
#
#
#     return result
#


#to count how many times each element appears

def counts(l):
    # Join the list into a single string and replace spaces
    str = ''.join(l).replace(' ', '')
    result = []
    for i in str:
        cnt = str.count(i)
        if (i,cnt) not in result:
            result.append((i,cnt))
    return result

 
L = []
input1 = int(input("Please enter how many elements you want in a list?:"))

for i in range(input1):
    n = input("Please give an input: ")
    L.append(n)

print(counts(L))
