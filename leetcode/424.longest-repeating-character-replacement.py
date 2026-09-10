# Category: algorithms
# Level: Medium
# Percent: 60.154705%



# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# 
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# 
#  
# Example 1:
# 
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# 
# 
# Example 2:
# 
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 10⁵
# 	s consists of only uppercase English letters.
# 	0 <= k <= s.length
# 
 

# CODE-START
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        c = [0] * 26
        l = mf = m = 0
        for r, ch in enumerate(s.encode()):
            ch -= 65
            c[ch] += 1
            mf = max(mf, c[ch])
            while (r - l + 1) - mf > k:
                c[ord(s[l]) - 65] -= 1
                l += 1

            m = max(m, r - l + 1)

        return m
        
# CODE-END
