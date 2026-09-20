# Category: algorithms
# Level: Medium
# Percent: 56.72134%



# Given an integer n, return the least number of perfect square numbers that sum to n.
# 
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
# 
#  
# Example 1:
# 
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# 
# 
# Example 2:
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= n <= 10⁴
# 
 

# CODE-START
class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def lps(x):
            return isqrt(x) ** 2

        if lps(n) == n:
            return 1

        for x in range(isqrt(n), 0, -1):
            if (d := n - x ** 2) == lps(d):
                return 2

        for x in range(isqrt(n), 0, -1):
            for y in range(isqrt(n - x ** 2), 0, -1):
                if (d := n - (x ** 2 + y ** 2)) == lps(d):
                    return 3

        return 4
# CODE-END
