# Category: algorithms
# Level: Hard
# Percent: 52.207726%



# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# 
# The test cases are generated so that the answer fits on a 32-bit signed integer.
# 
#  
# Example 1:
# 
# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# 
# 
# Example 2:
# 
# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length, t.length <= 1000
# 	s and t consist of English letters.
# 
 

# CODE-START
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        return self.dp1d(s, t)
        return self.dp(s, t)
        return self.backtracking(s, t)

    @staticmethod
    def dp1d(s, t):
        n, m = len(s), len(t)
        dp = [1] + [0] * m
        for i in range(n):
            for j in range(min(i + 1, m), 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] += dp[j - 1]
        
        return dp[-1]

    @staticmethod
    def dp(s, t):
        n, m = len(s), len(t)
        dp = [[0] * m for i in range(n)]
        dp[0][0] = int(s[0] == t[0])

        for i in range(1, n):
            dp[i][0] = int(s[i] == t[0]) + dp[i - 1][0]
        
        for i in range(1, n):
            for j in range(1, min(i + 1, m)):
                dp[i][j] = dp[i - 1][j] + int(s[i] == t[j]) * dp[i - 1][j - 1]

        return dp[n - 1][m - 1]

    @staticmethod
    def backtracking(s, t):
        n, m = len(s), len(t)
        def bt(i=0, j=0):
            if i == n or j == m:
                return int(j == m)

            return sum(
                bt(ndx + 1, j + 1)
                for ndx in range(i, n - m + j + 1)
                if s[ndx] == t[j]
            )

        return bt()
        
# CODE-END
