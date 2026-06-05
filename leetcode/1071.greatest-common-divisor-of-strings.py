#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (52.39%)
# Likes:    6047
# Dislikes: 1665
# Total Accepted:    965.5K
# Total Submissions: 1.8M
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For two strings s and t, we say "t divides s" if and only if s = t + t + t +
# ... + t + t (i.e., t is concatenated with itself one or more times).
# 
# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.
# 
# 
# Example 1:
# 
# 
# Input: str1 = "ABCABC", str2 = "ABC"
# 
# Output: "ABC"
# 
# 
# Example 2:
# 
# 
# Input: str1 = "ABABAB", str2 = "ABAB"
# 
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: str1 = "LEET", str2 = "CODE"
# 
# Output: ""
# 
# 
# Example 4:
# 
# 
# Input: str1 = "AAAAAB", str2 = "AAA"
# 
# Output: ""​​​​​​​
# 
# 
# 
# Constraints:
# 
# 
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
# 
# 
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == "" or str2 == "":
            return ""

        n1, n2 = len(str1), len(str2)
        sm, lg =  (str1, str2) if n1 < n2 else (str2, str1)
        n1, n2 = len(sm), len(lg)
        x = sm

        from math import gcd, sqrt
        g = gcd(n1, n2)
        divisors = list()
        for i in range(1, int(sqrt(g)) + 1):
            if g % i == 0:
                divisors.append(i)
                if i != g // i:
                    divisors.append(g // i)
        divisors.sort(reverse=True)

        for idx in divisors:
            x = sm[:idx]
            if len(sm) % len(x) != 0 or len(lg) % len(x) != 0:
                continue
            if len(sm) // len(x) * x == sm and len(lg) // len(x) * x == lg:
                return x
        return ""

# @lc code=end

