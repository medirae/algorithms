#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (28.82%)
# Likes:    7434
# Dislikes: 1328
# Total Accepted:    1.4M
# Total Submissions: 4.8M
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
# 
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return true if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule and
# false otherwise.
# 
# 
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
# 
# 
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        from math import ceil
        
        N = len(flowerbed)
        if n == 0:
            return True
        if N < 3:
            return sum(flowerbed) == 0 and n <= 1
        if n > ceil(N/2):
            return False
        for ndx in range(N):
            if flowerbed[ndx] == 0 and \
                ((ndx > 0 and flowerbed[ndx-1] == 0) or ndx == 0) and \
                ((ndx < N-1 and flowerbed[ndx+1] == 0) or ndx == N-1):
                flowerbed[ndx] = 1
                n -= 1
                if n == 0:
                    return True
        return n <= 0

# @lc code=end

