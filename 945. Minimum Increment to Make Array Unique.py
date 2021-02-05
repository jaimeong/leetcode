"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:


Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.

observations:
- increment only
- case 1: increase 1ish number
- case 2: increase the other numbers
- case 1 vs case 2
- increaes numbers to numbers not s

- linear search to find duplicates
- once duplicate found increase to next unseen number 
- dictionary to keep track of seen nums 
"""

def minIncrements(nums):
  # find dupes 
	if len(nums) <= 1:
		return 0
	elif len(nums) == 2 and nums[0] != nums[1]:
		return 0

	find_dupes = {} 
	dupes = []
	moves = 0

	for key, each in enumerate(nums):
		if each not in find_dupes:
			find_dupes[each] = 1
		else:
			find_dupes[each] += 1
			dupes.append(each)

	for i in range(min(dupes), max(nums)*3):
		if dupes and i not in find_dupes :
			moves += i - dupes.pop()
	

	return moves



			






print(minIncrements([]))
print(minIncrements([1,2,2]))
print(minIncrements([3,2,1,2,1,7]))
print(minIncrements([]))
print(minIncrements([3])) 
