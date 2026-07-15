# Category: algorithms
# Level: Medium
# Percent: 62.622166%



# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# 
# The first node is considered odd, and the second node is even, and so on.
# 
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# 
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
# 
#  
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
# 
# 
# Example 2:
# 
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
# 
# 
#  
# Constraints:
# 
# 
# 	The number of nodes in the linked list is in the range [0, 10⁴].
# 	-10⁶ <= Node.val <= 10⁶
# 
 

# CODE-START
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ndx = 0
        odd = ListNode()
        oddEnd = odd
        node = head
        prev = ListNode(next=node)
        while node is not None:
            if ndx % 2 == 1:
                prev.next = node.next
                node.next = None
                oddEnd.next = node
                oddEnd = oddEnd.next
                node = prev.next
            else:
                node = node.next
                prev = prev.next
            ndx += 1
        
        prev.next = odd.next
        return head
# CODE-END
