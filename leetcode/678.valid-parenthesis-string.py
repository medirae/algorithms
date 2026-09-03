# Category: algorithms
# Level: Medium
# Percent: 40.311947%



# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# 
# The following rules define a valid string:
# 
# 
# 	Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# 	Any right parenthesis ')' must have a corresponding left parenthesis '('.
# 	Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 	'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
# 
# 
#  
# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "(*)"
# Output: true
# Example 3:
# Input: s = "(*))"
# Output: true
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 100
# 	s[i] is '(', ')' or '*'.
# 
 

# CODE-START
class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.greedy(s)
        return self.dp(s)

    @staticmethod
    def dp(s):
        n = len(s)
        dp = [dict() for _ in range(n)]
        def bt(i=0, st=0):
            if i == n:
                return st == 0

            if st in dp[i]:
                return dp[i][st]

            dp[i][st] = (
                (s[i] == '(' and bt(i + 1, st + 1)) or 
                (s[i] == ')' and st > 0 and bt(i + 1, st - 1)) or
                (s[i] == '*' and (
                    (st > 0 and bt(i + 1, st - 1)) or 
                    bt(i + 1, st + 1) or
                    bt(i + 1, st)
                ))
            )
            
            return dp[i][st]

        return bt()

    @staticmethod
    def greedy(s):
        omax = omin = 0
        for c in s:
            if c == '(':
                omax, omin = omax + 1, omin + 1
            elif c == ')':
                if omax == 0:
                    return False

                omax, omin = omax - 1, omin - 1
                if omin < 0:
                    omin = 0
            else:
                omax, omin = omax + 1, omin - 1
                if omin < 0:
                    omin = 0

        return omin <= 0
        
# CODE-END
