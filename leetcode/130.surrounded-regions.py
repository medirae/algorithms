# Category: algorithms
# Level: Medium
# Percent: 45.822372%



# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
# 
# 
# 	Connect: A cell is connected to adjacent cells horizontally or vertically.
# 	Region: To form a region connect every 'O' cell.
# 	Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.
# 
# 
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
# 
#  
# Example 1:
# 
# 
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# 
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 
# Explanation:
# 
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
# 
# 
# Example 2:
# 
# 
# Input: board = [["X"]]
# 
# Output: [["X"]]
# 
# 
#  
# Constraints:
# 
# 
# 	m == board.length
# 	n == board[i].length
# 	1 <= m, n <= 200
# 	board[i][j] is 'X' or 'O'.
# 
 

# CODE-START
class Solution:
    def solve(self, b: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(b), len(b[0])
        
        def mark(i, j):
            if 0 <= i < n and 0 <= j < m and b[i][j] == 'O':
                b[i][j] = '.'
                mark(i + 1, j)
                mark(i - 1, j)
                mark(i, j + 1)
                mark(i, j - 1)
        
        for i in range(n):
            if b[i][0] == 'O':
                mark(i, 0)
            
            if b[i][m - 1] == 'O':
                mark(i, m - 1)
        
        for j in range(m):
            if b[0][j] == 'O':
                mark(0, j)
            
            if b[n - 1][j] == 'O':
                mark(n - 1, j)
        
        t = {79: 88, 46: 79}
        for i in range(n):
            for j in range(m):
                if b[i][j] == 'O':
                    b[i][j] = 'X'
                elif b[i][j] == '.':
                    b[i][j] = 'O'
        
# CODE-END
