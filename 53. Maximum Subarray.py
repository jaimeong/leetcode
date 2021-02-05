# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

def maxSub(nums):
    if len(nums) == 1:
        return nums[0]
    
    temp = curr_max = nums[0]

    for i in range(1, len(nums)):
        temp = max(nums[i], nums[i]+temp)
        curr_max = max(temp, curr_max)
    
    return curr_max


print(maxSub([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSub([1]))
print(maxSub([-1]))