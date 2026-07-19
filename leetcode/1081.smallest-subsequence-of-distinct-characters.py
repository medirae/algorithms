# Category: algorithms
# Level: Medium
# Percent: 63.665245%



# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
# 
#  
# Example 1:
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 1000
# 	s consists of lowercase English letters.
# 
# 
#  
# Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
 

# CODE-START
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        stack = list()
        picked = set()
        last_index = {char: ndx for ndx, char in enumerate(s)}
        for ndx in range(n):
            if s[ndx] in picked:
                continue

            while stack and s[ndx] <= stack[-1] and last_index[stack[-1]] > ndx:
                picked.remove(stack.pop())

            stack.append(s[ndx])
            picked.add(s[ndx])

        return "".join(stack)
        
# CODE-END
