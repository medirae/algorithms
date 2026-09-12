# Category: algorithms
# Level: Easy
# Percent: 44.486355%



# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# 
#  
# Example 1:
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# Input: s = "abc"
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 10⁵
# 	s consists of lowercase English letters.
# 
 

# CODE-START
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                tl = l
                tr = r

                valid = True
                l += 1
                while l < r:
                    if s[l] != s[r]:
                        valid = False
                        break

                    l += 1
                    r -= 1

                if valid:
                    return True

                valid = True
                l = tl
                r = tr - 1
                while l < r:
                    if s[l] != s[r]:
                        valid = False
                        break
                    
                    l += 1
                    r -= 1

                return valid

            l += 1
            r -= 1
        
        return True
        
# CODE-END
