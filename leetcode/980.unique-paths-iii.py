# Category: algorithms
# Level: Hard
# Percent: 82.911476%



# You are given an m x n integer array grid where grid[i][j] could be:
# 
# 
# 	1 representing the starting square. There is exactly one starting square.
# 	2 representing the ending square. There is exactly one ending square.
# 	0 representing empty squares we can walk over.
# 	-1 representing obstacles that we cannot walk over.
# 
# 
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
# 
#  
# Example 1:
# 
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# 
# 
# Example 2:
# 
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# 
# 
# Example 3:
# 
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
# 
# 
#  
# Constraints:
# 
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 20
# 	1 <= m * n <= 20
# 	-1 <= grid[i][j] <= 2
# 	There is exactly one starting cell and one ending cell.
# 
 

# CODE-START
class Solution:
    def uniquePathsIII(self, mx: list[list[int]]) -> int:
        n, m = len(mx), len(mx[0])
        si = sj = ei = ej = -1
        k = 0
        for i in range(n):
            k += mx[i].count(0)
            if si != -1 and ei != -1:
                continue

            for j in range(m):
                if mx[i][j] == 1:
                    si, sj = i, j
                elif mx[i][j] == 2:
                    ei, ej = i, j

        def dfs(i, j, k):
            if (i, j) == (ei, ej):
                return int(k == 0)
            
            c = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    0 <= (x := i + dx) < n and
                    0 <= (y := j + dy) < m and
                    mx[x][y] == 0
                ):
                    mx[x][y] = -1
                    c += dfs(x, y, k - 1)
                    mx[x][y] = 0
            
            return c
        
        mx[si][sj] = -1
        mx[ei][ej] = 0
        return dfs(si, sj, k + 1)
# CODE-END
