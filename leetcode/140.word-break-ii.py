# Category: algorithms
# Level: Hard
# Percent: 55.845745%



# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# 
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# 
#  
# Example 1:
# 
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# 
# 
# Example 2:
# 
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 20
# 	1 <= wordDict.length <= 1000
# 	1 <= wordDict[i].length <= 10
# 	s and wordDict[i] consist of only lowercase English letters.
# 	All the strings of wordDict are unique.
# 	Input is generated in a way that the length of the answer doesn't exceed 10⁵.
# 
 

# CODE-START
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        t = dict()
        for word in wordDict:
            d = t
            for ch in word:
                if ch not in d:
                    d[ch] = dict()

                d = d[ch]

            d['.'] = True

        n = len(s)
        memo = [None for _ in range(n)]
        def bt(ndx=0):
            if ndx == n:
                return ['']

            if memo[ndx] is not None:
                return memo[ndx]

            d = t
            o = list()
            for i in range(ndx, n):
                if s[i] not in d:
                    break
                
                d = d[s[i]]

                if '.' in d:
                    o.extend([s[ndx:i + 1] + (f' {v}' if v else "") for v in bt(i + 1)])

            memo[ndx] = o
            return o

        return bt()
# CODE-END
