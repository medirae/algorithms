# Category: algorithms
# Level: Easy
# Percent: 58.784653%



# Given a binary tree, determine if it is height-balanced.
# 
#  
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# 
# 
# Example 2:
# 
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# 
# 
# Example 3:
# 
# Input: root = []
# Output: true
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is in the range [0, 5000].
# 	-10⁴ <= Node.val <= 10⁴
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def valid(node):
            if node is None:
                return 0
            
            l = valid(node.left)
            if l is False:
                return False
            
            r = valid(node.right)
            if r is False:
                return False

            return 1 + max(l, r) if abs(l - r) <= 1 else False
        
        return valid(root) is not False
        
# CODE-END
