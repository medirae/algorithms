# Category: algorithms
# Level: Easy
# Percent: 80.754395%



# Given the head of a singly linked list, reverse the list, and return the reversed list.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# 
# Example 2:
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# 
# Example 3:
# 
# Input: head = []
# Output: []
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the list is the range [0, 5000].
# 	-5000 <= Node.val <= 5000
# 
# 
#  
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
 

# CODE-START
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node is not None:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        
        return prev
        
# CODE-END
