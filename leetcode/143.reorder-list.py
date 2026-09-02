# Category: algorithms
# Level: Medium
# Percent: 65.72945%



# You are given the head of a singly linked-list. The list can be represented as:
# 
# L₀ → L₁ → … → Ln - 1 → Ln
# 
# 
# Reorder the list to be on the following form:
# 
# L₀ → Ln → L₁ → Ln - 1 → L₂ → Ln - 2 → …
# 
# 
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# 
# 
# Example 2:
# 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the list is in the range [1, 5 * 10⁴].
# 	1 <= Node.val <= 1000
# 
 

# CODE-START
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = list()
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next
        
        l, r = 0, len(nodes) - 1
        while l + 1 < r:
            nodes[l].next, nodes[r].next = nodes[r], nodes[l + 1]
            l, r = l + 1, r - 1

        nodes[r].next = None
        return nodes[0]
        
# CODE-END
