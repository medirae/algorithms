# Category: algorithms
# Level: Easy
# Percent: 68.88306%



# Reverse bits of a given 32 bits signed integer.
# 
#  
# Example 1:
# 
# 
# Input: n = 43261596
# 
# Output: 964176192
# 
# Explanation:
# 
# 
# 	
# 		
# 			Integer
# 			Binary
# 		
# 		
# 			43261596
# 			00000010100101000001111010011100
# 		
# 		
# 			964176192
# 			00111001011110000010100101000000
# 		
# 	
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 2147483644
# 
# Output: 1073741822
# 
# Explanation:
# 
# 
# 	
# 		
# 			Integer
# 			Binary
# 		
# 		
# 			2147483644
# 			01111111111111111111111111111100
# 		
# 		
# 			1073741822
# 			00111111111111111111111111111110
# 		
# 	
# 
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= n <= 2³¹ - 2
# 	n is even.
# 
# 
#  
# Follow up: If this function is called many times, how would you optimize it?
 

# CODE-START
class Solution:
    def reverseBits(self, n: int) -> int:
        return self.bitwise(n)
        return self.itr(n)

    @staticmethod
    def bitwise(n):
        def rv(x, bl):
            if bl < 2:
                return x

            if bl == 2:
                return ((x << 1) & 0b11) | ((x >> 1) & 0b11)

            bl //= 2
            m = (1 << bl) - 1
            rs = x & m
            ls = (x >> bl) & m
            return rv(ls, bl) | (rv(rs, bl) << bl)
        
        return rv(n, 32)

    @staticmethod
    def itr(n):
        o = 0
        z = n.bit_length()
        for _ in range(z):
            o = (o << 1) | (n & 1)
            n >>= 1

        return o << (32 - z)
        
# CODE-END
