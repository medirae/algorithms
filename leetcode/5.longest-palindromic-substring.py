# Category: algorithms
# Level: Medium
# Percent: 38.241478%



# Given a string s, return the longest palindromic substring in s.
# 
#  
# Example 1:
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 1000
# 	s consist of only digits and English letters.
# 
 

# CODE-START
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.itr(s)
        return self.dp(s)
    
    @staticmethod
    def dp(s: str) -> str:
        n = len(s)
        maximum = s[0]

        if n == 1 or s == s[::-1]:
            return s

        dp = [['' for right in range(n)] for left in range(n)]
        for left in range(n):
            dp[left][left] = s[left]

        for depth in range(1, n):
            for ndx in range(n - depth):
                left = ndx
                right = depth + ndx
                if s[left] != s[right]:
                    continue
                if right - left > 1 and dp[left + 1][right - 1]:
                    dp[left][right] = s[left:right + 1]
                    maximum = dp[left][right]
                elif right - left <= 1:
                    dp[left][right] = s[left] + s[right]
                    maximum = dp[left][right]

        return maximum

    @staticmethod
    def itr(s: str) -> str:
        n = len(s)
        left = 0
        maxlen = 1
        for right in range(1, n):
            if right - maxlen > 0:
                odd = s[right - maxlen - 1:right + 1]
                if odd == odd[::-1]:
                    left = right - maxlen - 1
                    maxlen += 2
                    continue
            
            even = s[right - maxlen:right + 1]
            if even == even[::-1]:
                left = right - maxlen
                maxlen += 1

        return s[left:left + maxlen]
        
# CODE-END
