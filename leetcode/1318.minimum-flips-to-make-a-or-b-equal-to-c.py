# Category: algorithms
# Level: Medium
# Percent: 72.02189%



# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
# 
#  
# Example 1:
# 
# 
# 
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# 
# Example 2:
# 
# Input: a = 4, b = 2, c = 7
# Output: 1
# 
# 
# Example 3:
# 
# Input: a = 1, b = 2, c = 3
# Output: 0
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= a <= 10^9
# 	1 <= b <= 10^9
# 	1 <= c <= 10^9
 

# CODE-START
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # ((a | b) ^ c) shows which bits differ from c.
        #  c=0
        #   a=0, b=0 -> flip=1
        #  c=1
        #   a=0, b=1 -> flip=1
        #   a=1, b=0 -> flip=1
        #   a=1, b=1 -> flip=2
        #
        #  ((a | b) ^ c) & (a & b)   -> flip=2
        #   (a & b) implies (a | b) == 1 ->
        #   (1 ^ c) & (a & b) =
        #   (a & b) & ~c
        #  ((a | b) ^ c) & (a ^ b)   -> flip=1
        #  ((a | b) ^ c) & (~a & ~b) -> flip=1
        #   (((a | b) ^ c) & (a ^ b)) | ((a | b) ^ c) & (~a & ~b) =
        #   ((a | b) ^ c) & ((a ^ b) | (~a & ~b)) = 
        #   ((a | b) ^ c) & ~(a & b)

        ab = a & b
        return (((a ^ b) ^ c) & ~ab).bit_count() + 2 * (ab & ~c).bit_count()
        
# CODE-END
