# Category: algorithms
# Level: Medium
# Percent: 60.92252%



# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# 
# You have the following three operations permitted on a word:
# 
# 
# 	Insert a character
# 	Delete a character
# 	Replace a character
# 
# 
#  
# Example 1:
# 
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# 
# 
# Example 2:
# 
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= word1.length, word2.length <= 500
# 	word1 and word2 consist of lowercase English letters.
# 
 

# CODE-START
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        if n1 < n2:
            n1, n2, word1, word2 = n2, n1, word2, word1

        dp1 = [j for j in range(n2 + 1)]
        for i in range(1, n1 + 1):
            dp2 = [i] * (n2 + 1)
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp2[j] = dp1[j - 1]
                else:
                    dp2[j] = 1 + min(
                        dp1[j - 1],
                        dp2[j - 1],
                        dp1[j],
                    )
            
            dp1 = dp2
        
        return dp1[-1]

        cache = [[0] * (n2 + 1) for i in range(n1 + 1)]
        cache[0][0] = 0
        for i in range(1, n1+1):
            cache[i][0] = i # delete
        for j in range(1, n2+1):
            cache[0][j] = j # insert

        for i in range(1, n1 + 1):
            c1 = word1[i - 1]
            for j in range(1, n2 + 1):
                if c1 == word2[j - 1]:
                    cache[i][j] = cache[i - 1][j - 1] # nothing
                else:
                    cache[i][j] = 1 + min(
                        cache[i - 1][j - 1], # replace
                        cache[i - 1][j], # insert
                        cache[i][j - 1] # delete
                    )
 
        return cache[n1][n2]

        @lru_cache
        def bt(ndx1, ndx2):
            if ndx1 < 0 and ndx2 < 0: # nothing
                return 0

            if ndx1 >= 0 and ndx2 < 0: # delete
                 return 1 + bt(ndx1 - 1, ndx2)

            if ndx1 < 0 and ndx2 >= 0: # insert
                return 1 + bt(ndx1, ndx2 - 1)

            if word1[ndx1] == word2[ndx2]:
                return bt(ndx1 - 1, ndx2 - 1)

            return 1 + min(
                bt(ndx1 - 1, ndx2 - 1), # replace
                bt(ndx1, ndx2 - 1), # insert
                bt(ndx1 - 1, ndx2), # delete
            )
        
        
        r = bt(len(word1) - 1, len(word2) - 1)
        
# CODE-END
