"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
      [1],
     [1,1],
    [1,2,1],
   [1,3,3,1],
  [1,4,6,4,1]
 [1,5,10,10,5,1]
]

"""

def pascal(num_rows):
	ans = [[1], [1,1]]
	for i in range(2, num_rows+1):
		temp = [1]
		for j in range(len(ans[i-1])-1):
			temp.append(ans[i-1][j] + ans[i-1][j+1])

		temp.append(1)
		ans.append(temp)

	return ans
		
# def generate(self, numRows: int):
#     output = []
#     for i in range(numRows):
#         row = []
#         for j in range(i+1):
#             if j == 0 or j == i:
#                 row.append(1)
#             else:
#                 row.append(output[i-1][j-1] + output[i-1][j])
            
#         output.append(row)
        
#     return output

print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(5))
print(pascal(7))