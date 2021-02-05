
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# Time Complexity: O(n); single for loop to iterate thru nums; set/dict look up time is O(1)
# Space Complexity: O(n); 1:1 relationship between space allocated and inputs

## Hint: What information do you need to keep track of?
## Hint: What data structure allows you to keep track of two pieces of data at the same time?

def singleNum(nums):
    A = set()
    B = set()

    for each in nums:
        if each not in A:
            A.add(each)
        else:
            B.add(each)

    return (A-B).pop()

print(singleNum([2,2,1]))
print(singleNum([4,1,2,1,2]))
print(singleNum([1]))

# def singleNum(nums):
#     seen = []
#     if len(nums) > 2:
#         for each in nums:
#             if each in seen:
#                 seen.remove(each)
#             else:
#                 seen.append(each)
    
#         return seen[0]
#     else:
#         return nums[0]



# print(singleNum([2,2,1]))
# print(singleNum([4,1,2,1,2]))
# print(singleNum([1]))

# def singleNumOne(nums):
#     seen = {}
#     for each in nums:
#         if each not in seen:
#             seen[each] = 1
#         else:
#             seen[each] += 1

#     for each in seen:
#         if seen[each] == 1:
#             return each


# print(singleNumOne([2,2,1]))
# print(singleNumOne([4,1,2,1,2]))
# print(singleNumOne([1]))

