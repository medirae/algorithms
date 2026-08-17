# Category: algorithms
# Level: Medium
# Percent: 32.183693%



# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# 
#  
# Example 1:
# 
# Input: x = 123
# Output: 321
# 
# 
# Example 2:
# 
# Input: x = -123
# Output: -321
# 
# 
# Example 3:
# 
# Input: x = 120
# Output: 21
# 
# 
#  
# Constraints:
# 
# 
# 	-2³¹ <= x <= 2³¹ - 1
# 
 

# CODE-START
class Solution:
    def reverse(self, x: int) -> int:
        return self.string(x)
        return self.math(x)
    
    @staticmethod
    def string(x: int) -> int:
        m = 2147483648
        x = str(x)
        if x[0] != '-':
            x = int(x[::-1])
            if x >= m:
                return 0
        else:
            x = -int(x[:0:-1])
            if x < -m:
                return 0

        return x

    @staticmethod
    def math(x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        m = 2147483648
        m = m if sign == -1 else m - 1

        o = 0
        c = len(str(x))
        for p in range(c - 1, -1, -1):
            x, r = divmod(x, 10)
            o += r * 10**p
            if c == 10 and o > m:
                return 0
        
        return sign * o
        
# CODE-END
