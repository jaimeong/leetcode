# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

## Hint: What data structure can keep track of two data at the same time?
## Hint: How do you count occurences?

### Hint: What is the element in the middle of the sorted list? How do you know?

def majorityElement1(nums):
    nums = sorted(nums)
    return nums[len(nums)//2]

print(majorityElement1([2,2,1,1,1,2,2]))

def majorityElement2(nums):
    seen = {}
    for each in nums:
        if each not in seen:
            seen[each] = 1
        else:
            seen[each] += 1

    max_key = nums[0]
    for each in seen:
        if seen[each] > seen[max_key]:
            max_key = each 
    

    return max_key 

print(majorityElement1([2,2,1,1,1,2,2]))