

nums = [10, 20, 13, 14, 15, 13, 17, 10, 20, 13]

def find_first_duplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)
    return None  # Return None if no duplicates are found

print(find_first_duplicate(nums))





