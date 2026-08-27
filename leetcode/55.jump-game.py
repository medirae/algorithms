# Category: algorithms
# Level: Medium
# Percent: 41.20129%



# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# 
# Return true if you can reach the last index, or false otherwise.
# 
#  
# Example 1:
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10⁴
# 	0 <= nums[i] <= 10⁵
# 
 

# CODE-START
class Node:
    def __init__(self, start, end=None, checked=False):
        self.start = start
        self.end = end
        self.checked = checked
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.tail is None:
            self.head = self.tail = node
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def insert_after(self, current, node):
        nxt = current.next

        node.prev = current
        node.next = nxt
        current.next = node

        if nxt is not None:
            nxt.prev = node
        else:
            self.tail = node

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.greedy(nums)
        return self.greedier(nums)

    @staticmethod
    def greedier(nums):
        n = len(nums)
        p = LinkedList()
        p.append(Node(0))
        ndx = 0
        while ndx < n - 1:
            c = p.tail
            t = ndx

            if ndx + nums[ndx] <= t:
                c.end = ndx
                p.append(Node(ndx))

            while (c is not None and ndx < n - 1 and ndx + nums[ndx] <= t):
                if c.checked:
                    c = c.prev
                    continue

                sndx = c.end - 1
                while (c.start < sndx and sndx + nums[sndx] <= t):
                    sndx -= 1

                if sndx <= c.start:
                    c.checked = True
                    c = c.prev
                    continue

                p.insert_after(c, Node(sndx, c.end, True))
                c.end = sndx
                ndx = sndx + nums[sndx]

            if c is None or ndx >= n - 1:
                break

            p.tail.end = ndx
            p.append(Node(ndx))
            ndx += nums[ndx]

        return ndx >= n - 1

    @staticmethod
    def greedy(nums):
        n = len(nums)
        maxleft = 0
        for ndx in range(n - 1):
            maxleft = max(maxleft, nums[ndx])
            if maxleft <= 0:
                return False
            maxleft -= 1

        return True
        
# CODE-END
