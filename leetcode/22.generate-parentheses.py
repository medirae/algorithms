# Category: algorithms
# Level: Medium
# Percent: 78.92592%



# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
#  
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
#  
# Constraints:
# 
# 
# 	1 <= n <= 8
# 
 

# CODE-START
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = list()
        def bt(s):
            if len(s) == 2 * n:
                r.append(s)
                return
            
            o, c = s.count('('), s.count(')')
            if o < n:
                bt(s + "(")
            if c < n and c < o:
                bt(s + ')')

        bt("(")
        return r
        
# CODE-END
