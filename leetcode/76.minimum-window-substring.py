# Category: algorithms
# Level: Hard
# Percent: 48.000942%



# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
# 
# The testcases will be generated such that the answer is unique.
# 
#  
# Example 1:
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# 
# 
# Example 2:
# 
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# 
# Example 3:
# 
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# 
#  
# Constraints:
# 
# 
# 	m == s.length
# 	n == t.length
# 	1 <= m, n <= 10⁵
# 	s and t consist of uppercase and lowercase English letters.
# 
# 
#  
# Follow up: Could you find an algorithm that runs in O(m + n) time?
 

# CODE-START
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t in s:
            return t

        n, m = len(s), len(t)
        if n < m:
            return ""

        count = [0] * 128
        for c in t.encode():
            count[c] += 1

        mc = 0
        left = right = 0
        sb = s.encode()
        ml, mr, ms = 0, n, n + 1
        while right < n:
            while right < n and mc < m:
                if count[sb[right]] > 0:
                    mc += 1

                count[sb[right]] -= 1
                right += 1

            if mc != m:
                break

            right -= 1
            while count[sb[left]]:
                count[sb[left]] += 1
                left += 1

            if right - left < ms:
                ml, mr, ms = left, right, right - left
                if ms + 1 == m:
                    break

            count[sb[left]] += 1
            left += 1
            mc -= 1
            
            right += 1

        return s[ml:mr + 1 if mr < n else ml]
        
# CODE-END
