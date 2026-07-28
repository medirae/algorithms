# Category: algorithms
# Level: Medium
# Percent: 63.93348%



# You are given a palindromic string s.
# 
# Return the lexicographically smallest palindromic permutation of s.
# 
#  
# Example 1:
# 
# 
# Input: s = "z"
# 
# Output: "z"
# 
# Explanation:
# 
# A string of only one character is already the lexicographically smallest palindrome.
# 
# 
# Example 2:
# 
# 
# Input: s = "babab"
# 
# Output: "abbba"
# 
# Explanation:
# 
# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.
# 
# 
# Example 3:
# 
# 
# Input: s = "daccad"
# 
# Output: "acddca"
# 
# Explanation:
# 
# Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 10⁵
# 	s consists of lowercase English letters.
# 	s is guaranteed to be palindromic.
# 
 

# CODE-START
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        mid = s[n // 2] if n % 2 == 1 else ""
        c = Counter(s[:n // 2])

        picked = list()
        for ch in string.ascii_lowercase:
            if ch in c:
                picked.extend([ch] * c[ch])

        return "".join(picked) + mid + "".join(picked[::-1])
        
# CODE-END
