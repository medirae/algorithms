# Category: algorithms
# Level: Medium
# Percent: 59.36985%



# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# 
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# 
# 
# 	For example, "ace" is a subsequence of "abcde".
# 
# 
# A common subsequence of two strings is a subsequence that is common to both strings.
# 
#  
# Example 1:
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= text1.length, text2.length <= 1000
# 	text1 and text2 consist of only lowercase English characters.
# 
 

# CODE-START
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        row = [0] * n2
        row[0] = int(text1[0] == text2[0])
        for j in range(1, n2):
            row[j] = max(row[j - 1], int(text1[0] == text2[j]))

        for i in range(1, n1):
            new_row = [0] * n2
            new_row[0] = max(row[0], int(text1[i] == text2[0]))
            for j in range(1, n2):
                new_row[j] = 1 + row[j - 1] if text1[i] == text2[j] else max(new_row[j - 1], row[j])
            row = new_row

        return row[-1]
        
# CODE-END
