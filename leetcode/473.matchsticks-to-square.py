# Category: algorithms
# Level: Medium
# Percent: 42.08166%



# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
# 
# Return true if you can make this square and false otherwise.
# 
#  
# Example 1:
# 
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# 
# 
# Example 2:
# 
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= matchsticks.length <= 15
# 	1 <= matchsticks[i] <= 10⁸
# 
 

# CODE-START
class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        n = len(matchsticks)
        if n < 4:
            return False

        s = sum(matchsticks)
        if s % 4 != 0:
            return False

        l = s // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > l:
            return False

        sides = [0, 0, 0, 0]
        valid = [l] * 4
        def bt(ndx=0):
            if ndx == n:
                return sides == valid
            
            stick = matchsticks[ndx]
            v = set()
            for sndx in range(4):
                if sides[sndx] in v:
                    continue
                v.add(sides[sndx])
                if sides[sndx] + stick > l:
                    continue

                sides[sndx] += stick
                if bt(ndx + 1):
                    return True
                sides[sndx] -= stick

            return False

        return bt()
# CODE-END
