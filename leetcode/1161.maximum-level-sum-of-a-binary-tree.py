# Category: algorithms
# Level: Medium
# Percent: 70.012054%



# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# 
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# 
#  
# Example 1:
# 
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# Example 2:
# 
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is in the range [1, 10⁴].
# 	-10⁵ <= Node.val <= 10⁵
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximum = root.val
        max_depth = depth = 1
        q = [root]
        while q:
            nxt = list()
            som = 0
            for node in q:
                som += node.val
                if node.left is not None:
                    nxt.append(node.left)
                if node.right is not None:
                    nxt.append(node.right)
            
            if som > maximum:
                maximum = som
                max_depth = depth
            
            q = nxt
            depth += 1
        
        return max_depth
        
# CODE-END
