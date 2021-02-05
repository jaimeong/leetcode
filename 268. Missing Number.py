# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?



def missingNo(nums):
    return sum(i for i in range(len(nums)+1)) - sum(nums)






print(missingNo([3,0,1]))
print(missingNo([9,6,4,2,3,5,7,0,1]))
print(missingNo([0,1]))