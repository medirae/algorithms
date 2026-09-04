# Category: algorithms
# Level: Medium
# Percent: 77.089615%



# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
# 
#  
# Example 1:
# 
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# 
# 
# Example 2:
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the tree is n.
# 	1 <= k <= n <= 10⁴
# 	0 <= Node.val <= 10⁴
# 
# 
#  
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if node is None:
                return -k - 1
            
            if (l := inorder(node.left)) >= 0:
                return l
            k -= 1
            if k <= 0:
                return node.val
            if (r := inorder(node.right)) >= 0:
                return r
            
            return -k - 1
        
        return inorder(root)
        
# CODE-END
