# Category: algorithms
# Level: Medium
# Percent: 58.218998%



# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# 
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
# 
#  
# Example 1:
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# 
# 
# Example 2:
# 
# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
# 
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= hand.length <= 10⁴
# 	0 <= hand[i] <= 10⁹
# 	1 <= groupSize <= hand.length
# 
# 
#  
# Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
 

# CODE-START
class Solution:
    def isNStraightHand(self, hand: List[int], gsize: int) -> bool:
        n = len(hand)

        if n % gsize != 0:
            return False

        if gsize == 1:
            return True

        if gsize == n:
            return set(hand) == set(range((m := min(hand)), m + n))

        c = Counter(hand)
        for v in hand:
            if c[v] <= 0:
                continue

            r = v
            while c[r - 1] > 0:
                r -= 1

            while r <= v:
                l = r
                r += 1

                mi = c[l]
                if mi <= 0:
                    continue

                for _ in range(gsize):
                    if c[l] >= mi:
                        c[l] -= mi
                        l += 1
                    else:
                        return False

        return True
        
# CODE-END
