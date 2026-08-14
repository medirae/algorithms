# Category: algorithms
# Level: Hard
# Percent: 47.079773%



# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# 
# The overall run time complexity should be O(log (m+n)).
# 
#  
# Example 1:
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
#  
# Constraints:
# 
# 
# 	nums1.length == m
# 	nums2.length == n
# 	0 <= m <= 1000
# 	0 <= n <= 1000
# 	1 <= m + n <= 2000
# 	-10⁶ <= nums1[i], nums2[i] <= 10⁶
# 
 

# CODE-START
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        med = (n1 + n2) // 2
        odd = (n1 + n2) % 2 != 0

        ul, ur = 0, n1
        while ul <= ur:
            undx = ul + (ur - ul) // 2
            dndx = med + 1 - undx
            if dndx > n2:
                ul = undx + 1
                continue
            elif dndx < 0:
                ur = undx - 1
                continue

            if undx - 1 >= 0 and dndx < n2 and nums1[undx - 1] > nums2[dndx]:
                ur = undx - 1
                continue
            if undx < n1 and dndx - 1 >= 0 and nums2[dndx - 1] > nums1[undx]:
                ul = undx + 1
                continue

            UR, DR = float('-inf'), float('-inf')
            if undx - 1 >= 0:
                UR = nums1[undx - 1]
            if dndx - 1 >= 0:
                DR = nums2[dndx - 1]

            if odd:
                return max(UR, DR)

            UL, DL = float('-inf'), float('-inf')
            if undx - 2 >= 0:
                UL = nums1[undx - 2]
            if dndx - 2 >= 0:
                DL = nums2[dndx - 2]

            l, r = max(UR, DR), max(UL, DL)
            if l == UR:
                r = max(r, DR)
            else:
                r = max(r, UR)

            return (l + r) / 2

        return 1.0
        
# CODE-END
