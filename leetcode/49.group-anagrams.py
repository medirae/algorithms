# Category: algorithms
# Level: Medium
# Percent: 72.94284%



# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# 
#  
# Example 1:
# 
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
# 
# 
# 	There is no string in strs that can be rearranged to form "bat".
# 	The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# 	The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: strs = [""]
# 
# Output: [[""]]
# 
# 
# Example 3:
# 
# 
# Input: strs = ["a"]
# 
# Output: [["a"]]
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= strs.length <= 10⁴
# 	0 <= strs[i].length <= 100
# 	strs[i] consists of lowercase English letters.
# 
 

# CODE-START
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.sorting(strs)
        return self.frequency_count(strs)
    
    @staticmethod
    def sorting(strs):
        gs = list()
        gm = dict()
        for s in strs:
            h = ''.join(sorted(s))
            if h not in gm:
                gm[h] = len(gs)
                gs.append(list())
            gs[gm[h]].append(s)

        return gs

    @staticmethod
    def frequency_count(strs):
        gs = list()
        gm = dict()
        for s in strs:
            h = [0] * 26
            for c in s:
                h[ord(c) - 97] += 1
            h = ",".join(f'{c}:{cc}' for c, cc in enumerate(h) if cc > 0)
            if h not in gm:
                gm[h] = len(gs)
                gs.append(list())
            gs[gm[h]].append(s)
        
        return gs
        
# CODE-END
