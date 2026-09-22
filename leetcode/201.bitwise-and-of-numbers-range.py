# Category: algorithms
# Level: Medium
# Percent: 49.137177%



# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
# 
#  
# Example 1:
# 
# Input: left = 5, right = 7
# Output: 4
# 
# 
# Example 2:
# 
# Input: left = 0, right = 0
# Output: 0
# 
# 
# Example 3:
# 
# Input: left = 1, right = 2147483647
# Output: 0
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= left <= right <= 2³¹ - 1
# 
 

# CODE-START
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0 or right > (2 ** left.bit_length() - 1):
            return 0

        o = 0
        v = left
        while v:
            p = 2 ** (v.bit_length() - 1)
            o += int(o | p <= left and right <= o | (2 * p - 1)) * p
            v &= ~p

        return o
# CODE-END
