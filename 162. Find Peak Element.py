"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

    1 <= nums.length <= 1000
    -231 <= nums[i] <= 231 - 1
    nums[i] != nums[i + 1] for all valid i.

 
Follow up: Could you implement a solution with logarithmic complexity?

solution #1: linear search O(n)
	search thru nums  
	compare left right
solution # 2: bin search kinda

"""

def findPeak(nums):
	if (len(nums) == 1):
		return 0

	l = 0
	r = len(nums)-1

	while(l < r):
		mid = (l+r) // 2
		if (nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
			return mid
		if (nums[mid - 1] > nums[mid + 1]):
			r = mid - 1
		else: 
			l = mid + 1

# def findPeak(nums):
#   if (len(nums) == 1):
#     return 0

#   current = nums[0]
#   after = nums[1]
#   if (current > after):
#     return 0
#   else:
#     for i in range(1,len(nums) - 1):
#       before = nums[i - 1]
#       current = nums[i]
#       after = nums[i+1]
#       if (current > before and current > after):
#         return i
#     before = nums[-2]
#     current = nums[-1]
#     if (current > before):
#       return len(nums) - 1


print(findPeak([1,2,3,1]))
print(findPeak([1,2,1,3,5,6,4]))