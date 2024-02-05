# to find some of adjacent numbers
# def add(x, y):
#     return x + y

# def diff(*li):
#     total_sum = 0
#     for i in range(len(li) - 1):
#         total_sum += add(li[i], li[i + 1])
#     return total_sum

# l = []
# for i in range(2):
#     n1 = int(input(f"Please enter {i}th number: "))
#     l.append(n1)

# result = diff(*l)
# print("Result:", result)


def diff(x,y):
    difference = abs(x-y)
    if abs(x-y) <=5:
        return difference
    else:
        return False

n1 = float(input("1st number: "))
n2 = float(input('2nd number: '))    
print(diff(n1,n2))

