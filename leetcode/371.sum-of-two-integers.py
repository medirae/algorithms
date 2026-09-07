# Category: algorithms
# Level: Medium
# Percent: 55.8537%



# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# 
#  
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
# 
#  
# Constraints:
# 
# 
# 	-1000 <= a, b <= 1000
# 
 

# CODE-START
class Solution:
    def getSum(self, a: int, b: int) -> int:
        m = 0xfff
        c, s = (a & b) << 1, a ^ b
        while c & m:
            c, s = (s & c) << 1, s ^ c

        return s & m if c else s
        
# CODE-END
