# Category: algorithms
# Level: Medium
# Percent: 51.91728%



# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# 
# 
# Example 2:
# 
# Input: head = [5], left = 1, right = 1
# Output: [5]
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the list is n.
# 	1 <= n <= 500
# 	-500 <= Node.val <= 500
# 	1 <= left <= right <= n
# 
# 
#  
# Follow up: Could you do it in one pass?
 

# CODE-START
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if left == right:
            return head

        nh = ListNode(val=-1, next=head)
        node = nh
        for _ in range(1, left):
            node = node.next

        le = node
        l = prev = node.next
        node = prev.next
        for _ in range(left, right):
            prev, node.next, node = node, prev, node.next

        l.next = node
        le.next = prev
        return nh.next
        
# CODE-END
