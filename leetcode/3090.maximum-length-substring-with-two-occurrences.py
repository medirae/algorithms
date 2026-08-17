# Category: algorithms
# Level: Easy
# Percent: 65.884%



# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
#  
# Example 1:
# 
# 
# Input: s = "bcbbbcba"
# 
# Output: 4
# 
# Explanation:
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# 
# Example 2:
# 
# 
# Input: s = "aaaa"
# 
# Output: 2
# 
# Explanation:
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
# 
#  
# Constraints:
# 
# 
# 	2 <= s.length <= 100
# 	s consists only of lowercase English letters.
# 
 

# CODE-START
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        c = Counter()
        left = 0
        right = 0
        maximum = 0
        while right < n:
            c[s[right]] += 1
            while left <= right and c[s[right]] > 2:
                c[s[left]] -= 1
                left += 1
            
            left = min(left, right)
            if right - left + 1 > maximum:
                maximum = right - left + 1
        
            right += 1
        
        return maximum
        
# CODE-END
