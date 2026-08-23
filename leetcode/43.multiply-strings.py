# Category: algorithms
# Level: Medium
# Percent: 44.47368%



# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# 
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
# 
#  
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
#  
# Constraints:
# 
# 
# 	1 <= num1.length, num2.length <= 200
# 	num1 and num2 consist of digits only.
# 	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# 
 

# CODE-START
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return self.mulsim(num1, num2)
        return self.sumsim(num1, num2)

    @staticmethod
    def mulsim(num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        r = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            d1 = ord(num1[i]) - 48
            for j in range(m - 1, -1, -1):
                r[i + j + 1] += d1 * (ord(num2[j]) - 48)

        c = 0
        for rndx in range(len(r) - 1, -1, -1):
            c, r[rndx] = divmod(c + r[rndx], 10)

        return ''.join(map(lambda x: chr(x + 48), r)).lstrip('0') or '0'

    @staticmethod
    def sumsim(num1, num2):
        summs = list()
        mb = len(num2) + len(num1) - 2
        for base in range(len(num1)):
            for _ in range(ord(num1[-base-1]) - 48):
                summs.append(num2 + '0' * base)
        
        n = len(summs)
        summ = list()
        c = 0
        for base in range(mb + 1):
            s = c
            for vndx in range(n):
                if len(summs[vndx]) - 1 < base:
                    continue
                s += ord(summs[vndx][-base-1]) - 48
            c, s = divmod(s, 10)
            summ.append(chr(s + 48))
        
        return ''.join(summ[::-1])
        
# CODE-END
