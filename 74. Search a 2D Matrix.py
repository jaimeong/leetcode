"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

# Time Complexity: O(log m) + O(log n)
# First O(log m) is due to first outer loop  
# Second O(log n) is due to inner loop
# Space Complexity: O(1)
def search(matrix, target):
	left = 0
	right = len(matrix)
	mid = (left+right) // 2

	# print(left, mid, right)
	
	while left < right:
		if target < matrix[mid][0]:
			left =  0
			right = mid
			mid = (left+right) // 2
		elif target > matrix[mid][-1]:
			left = mid 
			right = len(matrix) 
			mid = (left+right) // 2
		else: 
			row = mid
			left = 0
			right = len(matrix[mid])-1
			mid = (left+right) // 2
			while(left < right):
				# print(left, mid, right)
				if target == matrix[row][mid] or target == matrix[row][right] or target == matrix[row][left]: 
					return True
				elif left == mid:
					return False
				elif target > mid: 
					left = mid
					right = len(matrix[mid])-1
					mid = (left+right) // 2
				elif target < mid:  
					left = 0
					right = mid
					mid = (left+right) // 2
	else:
		return False
	



print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60], [61,62,63,64,65], [66,67,68,69,70]], 64))

print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 4))
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 0))


print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60], [61,62,63,64,65], [66,67,68,69,70]], 64))
print(search([[1,3,5,7],[10,11,16,20],[23,30,34,60], [61,62,63,64,65]], 64))