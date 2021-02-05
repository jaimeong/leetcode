"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

def numIslands(grid):
	count = 0

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '1':
					search(grid,i, j, 1)
					count += 1
	
	return count      

def search(grid, i, j, land):
	if i >= len(grid) or j >= len(grid[0]) or i < 0  or j < 0 or grid[i][j] != '1':
		return

	grid[i][j] = "-1"

	search(grid, i + 1, j , land)
	search(grid, i -1, j, land)
	search(grid, i, j+1, land)
	search(grid, i , j-1, land)

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
