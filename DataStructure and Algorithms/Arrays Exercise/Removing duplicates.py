# def removeDuplicates(n_list):
#     L2 = []
#     for i in n_list:
#         if i not in L2:
#             L2.append(i)
#     return L2
#
# L1 = [1, 2, 2, 3, 4, 4, 5]
# print(removeDuplicates(L1))


# better time complexity solve

def removeDuplicates(n_list):
    unique_elements = set()
    result = []

    for item in n_list:
        if item not in unique_elements:
            unique_elements.add(item)
            result.append(item)

    return result

L1 = [1, 2, 2, 3, 4, 4, 5]
print(removeDuplicates(L1))
