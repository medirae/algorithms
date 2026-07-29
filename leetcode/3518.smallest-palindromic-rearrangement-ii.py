# Category: algorithms
# Level: Hard
# Percent: 14.834406%



# You are given a palindromic string s and an integer k.
# 
# Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.
# 
# Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.
# 
#  
# Example 1:
# 
# 
# Input: s = "abba", k = 2
# 
# Output: "baab"
# 
# Explanation:
# 
# 
# 	The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
# 	Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".
# 
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", k = 2
# 
# Output: ""
# 
# Explanation:
# 
# 
# 	There is only one palindromic rearrangement: "aa".
# 	The output is an empty string since k = 2 exceeds the number of possible rearrangements.
# 
# 
# 
# Example 3:
# 
# 
# Input: s = "bacab", k = 1
# 
# Output: "abcba"
# 
# Explanation:
# 
# 
# 	The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
# 	Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".
# 
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 10⁴
# 	s consists of lowercase English letters.
# 	s is guaranteed to be palindromic.
# 	1 <= k <= 10⁶
# 
 

# CODE-START
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        mid = s[n//2] if n % 2 == 1 else ''
        n = n // 2
        c  = Counter(s[:n])
        chars = [char for char in ascii_lowercase if char in c]

        total_perm_count = 1
        remaining = n
        for char, count in c.items():
            total_perm_count *= comb(remaining, count)
            remaining -= count
        if k > total_perm_count:
            return ""

        picked = list()
        perm_count = total_perm_count
        lower = 0
        while n > 0:
            for char in chars:
                if c[char] <= 0:
                    continue
                
                sub_perm_count = perm_count * c[char] // n
                c[char] -= 1
                if k <= lower + sub_perm_count:
                    picked.append(char)
                    n -= 1
                    perm_count = sub_perm_count
                    break
                c[char] += 1
                lower += sub_perm_count

        return "".join(picked) + mid + "".join(picked[::-1])
        
# CODE-END
