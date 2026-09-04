# Category: algorithms
# Level: Easy
# Percent: 80.253494%



# Given the root of a binary tree, invert the tree, and return its root.
# 
#  
# Example 1:
# 
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# 
# 
# Example 2:
# 
# Input: root = [2,1,3]
# Output: [2,3,1]
# 
# 
# Example 3:
# 
# Input: root = []
# Output: []
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is in the range [0, 100].
# 	-100 <= Node.val <= 100
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return
            
            node.left, node.right = dfs(node.right), dfs(node.left)
            return node
        
        return dfs(root)
        
# CODE-END
