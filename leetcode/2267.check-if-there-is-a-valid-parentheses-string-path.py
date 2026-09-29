# Category: algorithms
# Level: Hard
# Percent: 40.479298%



# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
# 
# 
# 	It is ().
# 	It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# 	It can be written as (A), where A is a valid parentheses string.
# 
# 
# You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:
# 
# 
# 	The path starts from the upper left cell (0, 0).
# 	The path ends at the bottom-right cell (m - 1, n - 1).
# 	The path only ever moves down or right.
# 	The resulting parentheses string formed by the path is valid.
# 
# 
# Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.
# 
#  
# Example 1:
# 
# Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
# Output: true
# Explanation: The above diagram shows two possible paths that form valid parentheses strings.
# The first path shown results in the valid parentheses string "()(())".
# The second path shown results in the valid parentheses string "((()))".
# Note that there may be other valid parentheses string paths.
# 
# 
# Example 2:
# 
# Input: grid = [[")",")"],["(","("]]
# Output: false
# Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
# 
# 
#  
# Constraints:
# 
# 
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 100
# 	grid[i][j] is either '(' or ')'.
# 
 

# CODE-START
class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        if grid[n - 1][m - 1] == '(' or (m + n - 1) & 1:
            return False

        @cache
        def bt(i=0, j=0, st=0):
            if grid[i][j] == '(':
                if (n - i) + (m - j) - 1 < st:
                    return False

                st += 1

            elif st == 1 and (i, j) == (n - 1, m - 1):
                return True

            elif st == 0:
                return False

            else:
                st -= 1

            if i + 1 < n and bt(i + 1, j, st):
                return True

            if j + 1 < m and bt(i, j + 1, st):
                return True

            return False

        return bt()
# CODE-END
