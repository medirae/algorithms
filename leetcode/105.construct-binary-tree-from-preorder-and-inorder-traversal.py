# Category: algorithms
# Level: Medium
# Percent: 69.19712%



# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
# 
#  
# Example 1:
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= preorder.length <= 3000
# 	inorder.length == preorder.length
# 	-3000 <= preorder[i], inorder[i] <= 3000
# 	preorder and inorder consist of unique values.
# 	Each value of inorder also appears in preorder.
# 	preorder is guaranteed to be the preorder traversal of the tree.
# 	inorder is guaranteed to be the inorder traversal of the tree.
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, p: List[int], i: List[int]) -> Optional[TreeNode]:
        inxs = {v: ndx for ndx, v in enumerate(i)}
        def mk(lp=0, li=0, ri=len(i)-1):
            if li > ri:
                return None

            return TreeNode(
                p[lp], mk(
                    lp + 1,
                    li,
                    inxs[p[lp]] - 1
                ), mk(
                    lp + 1 + inxs[p[lp]] - li,
                    inxs[p[lp]] + 1,
                    ri
                )
            )

        return mk()
        
# CODE-END
