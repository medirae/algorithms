# Category: algorithms
# Level: Medium
# Percent: 38.98549%



# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# 
#  
# Example 1:
# 
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# Input: x = 2.10000, n = 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/2² = 1/4 = 0.25
# 
# 
#  
# Constraints:
# 
# 
# 	-100.0 < x < 100.0
# 	-2³¹ <= n <= 2³¹-1
# 	n is an integer.
# 	Either x is not zero or n > 0.
# 	-10⁴ <= xn <= 10⁴
# 
 

# CODE-START
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if x == 0:
            return 0

        if n < 0:
            x = 1 / x
            n = -n

        v = 1
        while n > 0:
            if n & 1:
                v *= x
            x *= x
            n //= 2
        
        return v
        
        
# CODE-END
