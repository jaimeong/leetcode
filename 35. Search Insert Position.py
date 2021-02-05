# Given a sorted array of distinct integers and a target value, return the index if the
# target is found. If not, return the index where it would be if it were inserted in order.

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 7
# Output: 4

"""
part 1: find target if target 
for val, each in enumerate(nums):
	if target found, return val 

part 2: find where target would be inserted



best_index = largest num until target
for val, each in enumerate(nums):
	if target found, return val 
	if each > best and each < target: 
		best = each 
return best + 1
"""

def find(nums, target):
	best_idx = 0

	if len(nums) == 0:
		return -1 
	elif len(nums) == 1:
		return nums[0] == target

	for idx, val in enumerate(nums):
		if val == target:
			return idx  
		elif val > nums[best_idx] and val < target:
			best_idx = idx 

	return best_idx + 1




print(find([1,3,5,6], 5))
print(find([1,3,5,6], 7))