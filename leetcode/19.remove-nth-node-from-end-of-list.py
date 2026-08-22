# Category: algorithms
# Level: Medium
# Percent: 52.10507%



# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# Input: head = [1], n = 1
# Output: []
# 
# 
# Example 3:
# 
# Input: head = [1,2], n = 1
# Output: [1]
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the list is sz.
# 	1 <= sz <= 30
# 	0 <= Node.val <= 100
# 	1 <= n <= sz
# 
# 
#  
# Follow up: Could you do this in one pass?
 

# CODE-START
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
        
# CODE-END
