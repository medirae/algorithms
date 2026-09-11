# Category: algorithms
# Level: Easy
# Percent: 47.962585%



# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".
# 
#  
# Example 1:
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= strs.length <= 200
# 	0 <= strs[i].length <= 200
# 	strs[i] consists of only lowercase English letters if it is non-empty.
# 
 

# CODE-START
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = dict()
        for w in strs:
            d = t
            for c in w:
                if c not in d:
                    d[c] = dict()
                
                d = d[c]

            d['.'] = True

        o = list()
        d = t
        n = len(strs)
        while len(d) == 1 and '.' not in d:
            k, d = d.popitem()
            o.append(k)
        
        return ''.join(o)
        
# CODE-END
