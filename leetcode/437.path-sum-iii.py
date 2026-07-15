# Category: algorithms
# Level: Medium
# Percent: 46.496292%



# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# 
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
# 
#  
# Example 1:
# 
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# 
# 
# Example 2:
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is in the range [0, 1000].
# 	-10⁹ <= Node.val <= 10⁹
# 	-1000 <= targetSum <= 1000
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        from collections import defaultdict

        count = 0
        cache = defaultdict(int)
        cache[0] = 1
        stack = [(root, 0, False)]
        while stack:
            node, som, exiting = stack.pop()
            if exiting:
                cache[som] -= 1
                continue
            som += node.val

            if (diff := som - targetSum) in cache:
                count += cache[diff]

            cache[som] += 1
            stack.append((node, som, True))

            if node.right is not None:
                stack.append((node.right, som, False))
            if node.left is not None:
                stack.append((node.left, som, False))

        return count
        
# CODE-END
