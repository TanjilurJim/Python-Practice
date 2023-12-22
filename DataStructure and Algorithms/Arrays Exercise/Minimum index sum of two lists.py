# # Given 2 lists, with food preferences. index = 0 is most preferred.
# # Therefore, from the 2 lists find items which have minimum index
# # example: List1 = [pizza, hotdog, nuggets], l2 = [hotdog,nuggets, pizza]
# # output: hotdog
#
# def minSumofTwoLists(list1, list2):
#     index_map = {}
#
#     for index,item in enumerate(list1):
#         if item in index_map:
#             index_map[item] += index
#         else:
#             index_map[item] = index
#
#     for index,item in enumerate(list2):
#         if item in index_map:
#             index_map[item] += index
#         else:
#             index_map[item] = index
#
#     min_item = min(index_map, key=index_map.get)
#
#     return min_item
#
#
# # Example usage
# list1 = ["pizza", "hotdog", "nuggets"]
# list2 = ["hotdog", "nuggets", "pizza"]
# print(minSumofTwoLists(list1, list2))  # Output: hotdog

def minSumofTwoLists(list1, list2):
    index_map = {}

    for index, item in enumerate(list1):
        if item in index_map:
            index_map[item] += index
        else:
            index_map[item] = index

    for index, item in enumerate(list2):
        if item in index_map:
            index_map[item] += index
        else:
            index_map[item] = index

    min_item = min(index_map, key=index_map.get)

    return min_item

# Function to process the input string into a list
def process_input(input_str):
    # Assuming the input format is 'item1, item2, item3'
    return [item.strip() for item in input_str.split(',')]

# Example usage with user input
input_list1 = input("Enter the first list of items, separated by commas: ")
input_list2 = input("Enter the second list of items, separated by commas: ")

list1 = process_input(input_list1)
list2 = process_input(input_list2)

print(minSumofTwoLists(list1, list2))
