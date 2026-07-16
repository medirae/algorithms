# Category: algorithms
# Level: Medium
# Percent: 69.64241%



# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# 
#  
# Example 1:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is in the range [2, 10⁵].
# 	-10⁹ <= Node.val <= 10⁹
# 	All Node.val are unique.
# 	p != q
# 	p and q will exist in the tree.
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val == q.val:
            return p

        def dfs(node):
            if node is None:
                return
            if node.val == p.val or node.val == q.val:
                return node
            left, right = dfs(node.left), dfs(node.right)
            if left and right:
                return node
            return left or right

        return dfs(root)
        
# CODE-END
