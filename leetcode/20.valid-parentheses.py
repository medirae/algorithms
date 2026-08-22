# Category: algorithms
# Level: Easy
# Percent: 44.520588%



# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# 	Open brackets must be closed by the same type of brackets.
# 	Open brackets must be closed in the correct order.
# 	Every close bracket has a corresponding open bracket of the same type.
# 
# 
#  
# Example 1:
# 
# 
# Input: s = "()"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# 
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# 
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([])"
# 
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: s = "([)]"
# 
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 10⁴
# 	s consists of parentheses only '()[]{}'.
# 
 

# CODE-START
class Solution:
    def isValid(self, s: str) -> bool:
        st = list()
        m = {'{': '}', '(': ')', '[': ']'}
        for c in s:
            if c in '([{':
                st.append(m[c])
            elif st and c == st[-1]:
                st.pop()
            else:
                return False
        
        return not st
            
        
# CODE-END
