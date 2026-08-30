# Category: algorithms
# Level: Medium
# Percent: 44.365063%



# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# 
# An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:
# 
# 
# 	s = s₁ + s₂ + ... + sn
# 	t = t₁ + t₂ + ... + tm
# 	|n - m| <= 1
# 	The interleaving is s₁ + t₁ + s₂ + t₂ + s₃ + t₃ + ... or t₁ + s₁ + t₂ + s₂ + t₃ + s₃ + ...
# 
# 
# Note: a + b is the concatenation of strings a and b.
# 
#  
# Example 1:
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.
# 
# 
# Example 2:
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
# 
# 
# Example 3:
# 
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= s1.length, s2.length <= 100
# 	0 <= s3.length <= 200
# 	s1, s2, and s3 consist of lowercase English letters.
# 
# 
#  
# Follow up: Could you solve it using only O(s2.length) additional memory space?
 

# CODE-START
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        return self.topdown(s1, s2, s3)
        return self.backtrack(s1, s2, s3)

    @staticmethod
    def topdown(s1, s2, s3):
        n, m, t = len(s1), len(s2), len(s3)
        dp = dict()
        def bt(i=0, j=0):
            if i == n and j == m:
                return True
            
            h = (m + 1) * i + j
            if h in dp:
                return dp[h]
            
            dp[h] = ((
                i < n and
                s1[i] == s3[i + j] and
                bt(i + 1, j)
            ) or (
                j < m and
                s2[j] == s3[i + j] and
                bt(i, j + 1)
            ))
            return dp[h]
        
        return bt()

    @staticmethod
    def backtrack(s1, s2, s3):
        n, m, t = len(s1), len(s2), len(s3)
        dp = dict()
        def bt(s1x=0, s2x=0):
            if s1x == n and s2x == m:
                return True

            h = m * s1x + s2x
            if h in dp:
                return dp[h]

            i, j = s1x, s2x
            while i < n and s1[i] == s3[i + j]:
                i += 1
                h += m
                dp[h] = bt(i, j)
                if dp[h] is True:
                    return True

            h = m * s1x + s2x
            i, j = s1x, s2x
            while j < m and s2[j] == s3[i + j]:
                j += 1
                h += 1
                dp[h] = bt(i, j)
                if dp[h] is True:
                    return True

            dp[m * s1x + s2x] = False
            return False

        return bt()
        
# CODE-END
