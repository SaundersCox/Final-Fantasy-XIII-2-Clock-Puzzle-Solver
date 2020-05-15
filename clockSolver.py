# Final Fantasy XIII-2 Clock Puzzle Solver
# Enter values starting from the 12 o'clock position going clockwise
# When done, enter value 0 to calculate.
# Solutions will print out

# [EXAMPLE]
# Enter numbers starting from 12 o'clock position.
# Enter '0' to solve
# 1
# 2
# 4
# 6
# 6
# 3
# 1
# 4
# 2
# 3
# 3
# 5
# 0
# [2, 6, 5, 8, 10, 7, 3, 9, 0, 1, 11, 4]
# [8, 6, 5, 2, 10, 7, 3, 9, 0, 1, 11, 4]

import copy

# ID, value, references, marked
ID = 0
VAL = 1
REF = 2
MARK = 3

def solve(nums):
    build_refs(nums)
    # print(nums)
    traverse(nums)
    return 1

def build_refs(nums):
    sz = len(nums)
    for i in range(0,sz):
        val = nums[i][VAL]
        nums[i][REF].add(nums[(i-val)%sz][ID])
        nums[i][REF].add(nums[(i+val)%sz][ID])

def traverse(nums):
    # Test each root
    for i in range(0, len(nums)):
        nums_copy = copy.deepcopy(nums)
        # We want to traverse through the references until all nodes are marked
        path = mark_and_sweep(nums_copy, nums_copy[i], [])
        
        

def mark_and_sweep(nums, item, path):
    path_copy = copy.deepcopy(path)
    if len(path) == len(nums):
        print(path)
    if (item[MARK]):
        marks = [item[MARK] for item in nums]
        return
    item[MARK] = True
    path_copy.append(item[ID])
    for sub_item in item[REF]:
        # print(sub_item)
        if (sub_item == -1):
            return
        n = sub_item
        # sub_item = -1
        nums_copy = copy.deepcopy(nums)
        mark_and_sweep(nums_copy, nums_copy[sub_item], path_copy)
    return path_copy

nums = []
n = -1
i = 0
print('Enter numbers starting from 12 o\'clock position.')
print('Enter \'0\' to solve')
while (n != 0):
    n = input()
    if (n>0):
        nums.append([i, n, set(), False]) # ID, value, references, marked
        i = i + 1

(solve(nums))