# Category: algorithms
# Level: Medium
# Percent: 58.964054%



# You are given an m x n grid where each cell can have one of three values:
# 
# 
# 	0 representing an empty cell,
# 	1 representing a fresh orange, or
# 	2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# 
#  
# Example 1:
# 
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# Example 2:
# 
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# 
# 
# Example 3:
# 
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
# 
# 
#  
# Constraints:
# 
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 10
# 	grid[i][j] is 0, 1, or 2.
# 
 

# CODE-START
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fruit = 0
        for i, j in product(range(n), range(m)):
            if grid[i][j] != 0:
                fruit += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        if (rotten := len(q)) == fruit:
            return 0
        elif rotten == 0:
            return -1

        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for ix, jy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i + ix, j + jy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        grid[x][y] = 2
                        rotten += 1
                        q.append((x, y))
                        if rotten == fruit:
                            return minutes + 1

        return -1
        
# CODE-END
