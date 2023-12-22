def overLapping(l1, l2):
    l3 = []

    for i in range(len(l1)):
        if l1[i] in l2:
            l3.append(l1[i])  # Append the element, not the index

    return l3

li_1 = [1, 2, 3, 4, 50, 60]
li_2 = [4, 7, 5, 8, 13, 2, 90, 50]

print(overLapping(li_1, li_2))
