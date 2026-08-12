# Category: algorithms
# Level: Medium
# Percent: 39.49911%



# Given a string s, find the length of the longest substring without duplicate characters.
# 
#  
# Example 1:
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# 
# 
# Example 2:
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= s.length <= 10⁵
# 	s consists of English letters, digits, symbols and spaces.
# 
 

# CODE-START
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = [-2] * 127
        left = -1
        maxlen = 0
        maxmaxlen = min(len(s), 127)
        for right, code in enumerate(s.encode()):
            if c[code] > left:
                left = c[code]
            elif (clen := right - left) > maxlen and clen == maxmaxlen:
                return maxmaxlen
            elif clen > maxlen:
                maxlen = clen

            c[code] = right

        return maxlen
        
# CODE-END
