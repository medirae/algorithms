# Category: algorithms
# Level: Hard
# Percent: 66.66202%



# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# 
# 
# Example 2:
# 
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the list is n.
# 	1 <= k <= n <= 5000
# 	0 <= Node.val <= 1000
# 
# 
#  
# Follow-up: Can you solve the problem in O(1) extra memory space?
 

# CODE-START
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, node = ListNode(0, head), head
        head, next = prev, prev
        for _ in range(k):
            if next is None:
                break
            next = next.next

        while next is not None:
            nn = next.next
            p, n = node, node.next
            while p is not next:
                n.next, p, n = p, n, n.next  # delicate order

            node.next = nn
            node, next = next, node
            prev.next = node

            for _ in range(k):
                if next is None:
                    break
                prev, node, next = prev.next, node.next, next.next

        return head.next
        
# CODE-END
