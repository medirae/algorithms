# Category: algorithms
# Level: Easy
# Percent: 50.937496%



# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# 
# If the town judge exists, then:
# 
# 
# 	The town judge trusts nobody.
# 	Everybody (except for the town judge) trusts the town judge.
# 	There is exactly one person that satisfies properties 1 and 2.
# 
# 
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# 
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
# 
#  
# Example 1:
# 
# Input: n = 2, trust = [[1,2]]
# Output: 2
# 
# 
# Example 2:
# 
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# 
# 
# Example 3:
# 
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= n <= 1000
# 	0 <= trust.length <= 10⁴
# 	trust[i].length == 2
# 	All the pairs of trust are unique.
# 	ai != bi
# 	1 <= ai, bi <= n
# 
 

# CODE-START
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        i, o = [0] * n, [0] * n
        for u, v in trust:
            o[u - 1] += 1
            i[v - 1] += 1
        
        for ndx in range(n):
            if i[ndx] == n - 1 and o[ndx] == 0:
                return ndx + 1
        
        return -1
# CODE-END
