# Category: algorithms
# Level: Easy
# Percent: 51.894577%



# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# 
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
# 
#  
# Example 1:
# 
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# 
# 
# Example 2:
# 
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the root tree is in the range [1, 2000].
# 	The number of nodes in the subRoot tree is in the range [1, 1000].
# 	-10⁴ <= root.val <= 10⁴
# 	-10⁴ <= subRoot.val <= 10⁴
# 
 

# CODE-START
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.strings(root, subRoot)
        return self.lists(root, subRoot)
        return self.bf(root, subRoot)

    @staticmethod
    def strings(root, sub):
        def mksub(node):
            return f'{mksub(node.left)} {mksub(node.right)} {node.val}' if node is not None else '-'
        
        sub = mksub(sub)

        def find(node):
            if node is None:
                return "-" if sub != "-" else True

            return (
                (l := find(node.left)) is True or
                (r := find(node.right)) is True or
                (s := f'{l} {r} {node.val}') == sub or
                s
            )

        return find(root) is True

    @staticmethod
    def lists(root, sub):
        def mksub(node):
            if node is None:
                return [None]
            return [*mksub(node.left), *mksub(node.right), node.val]

        sub = mksub(sub)
        sn = len(sub)

        def dfs(node):
            if node is None:
                return [None], sn == 1 and sub[0] is None
            
            l, valid = dfs(node.left)
            if valid:
                return None, True

            r, valid = dfs(node.right)
            if valid:
                return None, True
            
            ln, rn = len(l), len(r)
            if ln + rn + 1 == sn and \
                l == sub[:ln] and \
                r == sub[ln:ln + rn] and \
                node.val == sub[-1]:
                return None, True
            
            return l + r + [node.val], False

        return dfs(root)[1]

    @staticmethod
    def bf(root, sub):
        def dfs(n1, n2, exact=False):
            if n1 is None:
                return n2 is None

            if n2 is None:
                return False

            return (
                n1.val == n2.val
                and dfs(n1.left, n2.left, True)
                and dfs(n1.right, n2.right, True)
            ) or (not exact and (dfs(n1.left, n2) or dfs(n1.right, n2)))

        return dfs(root, sub)
        
# CODE-END
