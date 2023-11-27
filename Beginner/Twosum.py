def twoSums(nums,target):
    map = {}

    for i, v in enumerate(nums):
        complement = target - v
        if complement in map:
            return [map[complement],i]


        map[v] = i



num = [1,3,5,4]
target = 8

print(twoSums(num,target))



