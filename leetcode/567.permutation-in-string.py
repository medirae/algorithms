# Category: algorithms
# Level: Medium
# Percent: 49.293076%



# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# 
# In other words, return true if one of s1's permutations is the substring of s2.
# 
#  
# Example 1:
# 
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s1.length, s2.length <= 10⁴
# 	s1 and s2 consist of lowercase English letters.
# 
 

# CODE-START
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        c1, c2 = [0] * 26, [0] * 26  # counters
        for ndx in range(n1):
            c1[ord(s1[ndx]) - 97] += 1
            c2[ord(s2[ndx]) - 97] += 1

        mc = 0  # matched counts
        cc = 0  # count of counts
        for c in range(26):
            if c1[c] > 0:
                cc += 1
                if c2[c] == c1[c]:
                    mc += 1

        if mc == cc:
            return True

        for ndx in range(n1, n2):
            r = ord(s2[ndx]) - 97
            c2[r] += 1
            if c1[r] > 0:
                if c2[r] == c1[r]:
                    mc += 1
                elif c2[r] == c1[r] + 1:
                    mc -= 1

            l = ord(s2[ndx - n1]) - 97
            c2[l] -= 1
            if c1[l] > 0:
                if c2[l] == c1[l]:
                    mc += 1
                elif c2[l] == c1[l] - 1:
                    mc -= 1

            if mc == cc:
                return True

        return False
        
# CODE-END
