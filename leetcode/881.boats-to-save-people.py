# Category: algorithms
# Level: Medium
# Percent: 62.09135%



# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
# 
# Return the minimum number of boats to carry every given person.
# 
#  
# Example 1:
# 
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# 
# 
# Example 2:
# 
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# 
# 
# Example 3:
# 
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= people.length <= 5 * 10⁴
# 	1 <= people[i] <= limit <= 3 * 10⁴
# 
 

# CODE-START
class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        wl = max(p) + 1
        ws = [0] * wl
        for w in p:
            ws[w] += 1

        wndxs = list(filter(ws.__getitem__, range(wl)))
        l, r = 0, len(wndxs) - 1
        m = 0
        while l <= r:
            lw, rw = wndxs[l], wndxs[r]
            lc, rc = ws[lw], ws[rw]

            if l < r and lw + rw <= limit:
                if lc < rc:
                    m += lc
                    ws[rw] -= lc
                    l += 1
                else:
                    m += rc
                    ws[lw] -= rc
                    r -= 1
            elif l == r and lw * 2 <= limit and 0 < (ld := lc // 2):
                m += ld
                ws[lw] = lc % 2
                l += ws[lw] == 0
            else:
                m += rc
                r -= 1

        return m
        
# CODE-END
