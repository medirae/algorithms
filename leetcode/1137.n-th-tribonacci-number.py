# Category: algorithms
# Level: Easy
# Percent: 63.11781%



# The Tribonacci sequence Tn is defined as follows: 
# 
# T₀ = 0, T₁ = 1, T₂ = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# 
# Given n, return the value of Tn.
# 
#  
# Example 1:
# 
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# 
# 
# Example 2:
# 
# Input: n = 25
# Output: 1389537
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= n <= 37
# 	The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
# 
 

# CODE-START
class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [0] * max(3, n + 1)
        cache[0], cache[1], cache[2] = 0, 1, 1
        for num in range(3, n + 1):
            cache[num] = cache[num - 1] + cache[num - 2] + cache[num - 3]
        
        return cache[n]
        
# CODE-END
