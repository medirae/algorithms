# Category: algorithms
# Level: Hard
# Percent: 31.323198%



# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# 
# 
# 	'.' Matches any single character.​​​​
# 	'*' Matches zero or more of the preceding element.
# 
# 
# Return a boolean indicating whether the matching covers the entire input string (not partial).
# 
#  
# Example 1:
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 20
# 	1 <= p.length <= 20
# 	s contains only lowercase English letters.
# 	p contains only lowercase English letters, '.', and '*'.
# 	It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
# 
 

# CODE-START
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, pn = len(s), len(p)
        dp = dict()
        def bt(sndx, pndx):
            key = (sndx, pndx)
            if key in dp:
                return dp[key]

            if sndx == n:
                if pndx == pn:
                    dp[key] = True
                
                elif pndx < pn - 1 and p[pndx + 1] == '*':
                    dp[key] = bt(sndx, pndx + 2)

                else:
                    dp[key] = False
            
            elif pndx == pn:
                dp[key] = False

            elif pndx < pn - 1 and p[pndx + 1] == '*':
                dp[key] = ((p[pndx] == '.' or p[pndx] == s[sndx]) and bt(sndx + 1, pndx)) or bt(sndx, pndx + 2)

            else:
                dp[key] = (p[pndx] == '.' or p[pndx] == s[sndx]) and bt(sndx + 1, pndx + 1)

            return dp[key]

        return bt(0, 0)
        
# CODE-END
