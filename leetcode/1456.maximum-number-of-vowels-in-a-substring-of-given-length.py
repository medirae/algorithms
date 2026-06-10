#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
#
# algorithms
# Medium (59.67%)
# Likes:    3974
# Dislikes: 153
# Total Accepted:    706.6K
# Total Submissions: 1.1M
# Testcase Example:  '"abciiidef"\n3'
#
# Given a string s and an integer k, return the maximum number of vowel letters
# in any substring of s with length k.
# 
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# 
# 
# Example 1:
# 
# 
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# 
# 
# Example 2:
# 
# 
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# 
# 
# Example 3:
# 
# 
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 1 <= k <= s.length
# 
# 
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = lambda x: x in 'aeiou'
        n = len(s)
        if n == 1:
            return int(vowel(s))
        if k == 1:
            return int(any(vowel(c) for c in s))
        left, right = 0, k - 1
        maximum = count = [vowel(c) for c in s[left:right+1]].count(True)
        left, right = left + 1, right + 1
        while right < n:
            if vowel(s[left-1]):
                count -= 1
            if vowel(s[right]):
                count += 1
            maximum = max(maximum, count)
            left += 1
            right += 1
        return maximum
# @lc code=end

