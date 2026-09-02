# Category: algorithms
# Level: Medium
# Percent: 49.66793%



# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# 
#  
# Example 1:
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# 
# 
# Example 2:
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 300
# 	1 <= wordDict.length <= 1000
# 	1 <= wordDict[i].length <= 20
# 	s and wordDict[i] consist of only lowercase English letters.
# 	All the strings of wordDict are unique.
# 
 

# CODE-START
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dp(s, wordDict)
        return self.trie(s, wordDict)
    
    @staticmethod
    def dp(s, wordDict):
        n = len(s)
        dp = [True] + [False] * n
        words = set(wordDict)
        lens = {len(w) for w in words}

        for i in range(1, n + 1):
            for wl in lens:
                j = i - wl
                if (
                    j >= 0 and
                    dp[j] and
                    s[j:i] in words
                ):
                    dp[i] = True
                    break

        return dp[n]

    @staticmethod
    def trie(s, wordDict):
        t = dict()
        for word in wordDict:
            d = t
            for c in word:
                if c not in d:
                    d[c] = dict()
                
                d = d[c]
            
            d['.'] = True
   
        n = len(s)
        dp = dict()
        def bt(ndx=0):
            if ndx == n:
                return '.' in d
            
            if ndx in dp:
                return dp[ndx]

            d = t
            for j in range(ndx, n):
                c = s[j]
                if c not in d:
                    break
                d = d[c]
                if '.' in d and bt(j + 1):
                    dp[ndx] = True
                    return True
            
            dp[ndx] = False
            return False

        return bt()
        
# CODE-END
