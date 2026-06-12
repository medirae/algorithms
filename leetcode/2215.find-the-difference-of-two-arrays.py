#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#
# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/
#
# algorithms
# Easy (80.24%)
# Likes:    2635
# Dislikes: 129
# Total Accepted:    657.4K
# Total Submissions: 806.9K
# Testcase Example:  '[1,2,3]\n[2,4,6]'
#
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
# size 2 where:
# 
# 
# answer[0] is a list of all distinct integers in nums1 which are not present
# in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present
# in nums1.
# 
# 
# Note that the integers in the lists may be returned in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1
# and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4
# and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] ==
# nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# -1000 <= nums1[i], nums2[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def findDifference(sel1f, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        return [
            list(nums1.difference(nums2)),
            list(nums2.difference(nums1))
        ]
# @lc code=end

