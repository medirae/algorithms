# Category: algorithms
# Level: Easy
# Percent: 65.89229%



# Given the root of a binary tree, return the length of the diameter of the tree.
# 
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# 
# The length of a path between two nodes is represented by the number of edges between them.
# 
#  
# Example 1:
# 
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Example 2:
# 
# Input: root = [1,2]
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is in the range [1, 10⁴].
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return 0
        
        maximum = 0
        def dfs(node):
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            nonlocal maximum
            if l + r > maximum:
                maximum = l + r

            return max(l, r) + 1
        
        dfs(root)
        return maximum
        
# CODE-END
