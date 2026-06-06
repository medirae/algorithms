#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (56.53%)
# Likes:    5406
# Dislikes: 2861
# Total Accepted:    1.6M
# Total Submissions: 2.6M
# Testcase Example:  '"IceCreAm"'
#
# Given a string s, reverse only all the vowels in the string and return it.
# 
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases, more than once.
# 
# 
# Example 1:
# 
# 
# Input: s = "IceCreAm"
# 
# Output: "AceCreIm"
# 
# Explanation:
# 
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes
# "AceCreIm".
# 
# 
# Example 2:
# 
# 
# Input: s = "leetcode"
# 
# Output: "leotcede"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AaEeIiOoUu")
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1            

        return "".join(s)

# @lc code=end

