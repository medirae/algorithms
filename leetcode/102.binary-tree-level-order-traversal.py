# Category: algorithms
# Level: Medium
# Percent: 73.08087%



# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# 
#  
# Example 1:
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# 
# 
# Example 2:
# 
# Input: root = [1]
# Output: [[1]]
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
# 	The number of nodes in the tree is in the range [0, 2000].
# 	-1000 <= Node.val <= 1000
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        o = list()
        while q:
            ot = list()
            for _ in range(len(q)):
                node = q.popleft()
                ot.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            o.append(ot)
        
        return o
        
# CODE-END
