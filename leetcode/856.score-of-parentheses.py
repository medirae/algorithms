# Category: algorithms
# Level: Medium
# Percent: 63.5231%



# Given a balanced parentheses string s, return the score of the string.
# 
# The score of a balanced parentheses string is based on the following rule:
# 
# 
# 	"()" has score 1.
# 	AB has score A + B, where A and B are balanced parentheses strings.
# 	(A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
#  
# Example 1:
# 
# Input: s = "()"
# Output: 1
# 
# 
# Example 2:
# 
# Input: s = "(())"
# Output: 2
# 
# 
# Example 3:
# 
# Input: s = "()()"
# Output: 2
# 
# 
#  
# Constraints:
# 
# 
# 	2 <= s.length <= 50
# 	s consists of only '(' and ')'.
# 	s is a balanced parentheses string.
# 
 

# CODE-START
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sc = 0
        st = list()
        for c in s:
            if c == '(':
                st.append(0)
            else:
                v = st.pop()
                v = 1 if v == 0 else 2 * v
                if st:
                    st[-1] += v
                else:
                    sc += v

        return sc
# CODE-END
