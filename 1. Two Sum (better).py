from collections import defaultdict


def twoSum(nums, target):
    nun_map = defaultdict(int)

    for index, num in enumerate(nums):
        other = target - num
        if other in nun_map:
            return [nun_map[other], index]

        nun_map[num] = index

    return [-1, -1]

nums =[2,7,11,15]
target = 17

print(twoSum(nums, target))