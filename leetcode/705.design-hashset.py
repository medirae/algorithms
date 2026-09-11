# Category: algorithms
# Level: Easy
# Percent: 68.25043%



# Design a HashSet without using any built-in hash table libraries.
# 
# Implement MyHashSet class:
# 
# 
# 	void add(key) Inserts the value key into the HashSet.
# 	bool contains(key) Returns whether the value key exists in the HashSet or not.
# 	void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
# 
# 
#  
# Example 1:
# 
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
# 
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
# 
#  
# Constraints:
# 
# 
# 	0 <= key <= 10⁶
# 	At most 10⁴ calls will be made to add, remove, and contains.
# 
 

# CODE-START
class MyHashSet:
    def __init__(self):
        self.base = 32
        self.bs = list()

    def chsize(self, ndx):
        if (d := ndx - len(self.bs)) >= 0:
            self.bs.extend([0] * (d + 1))

    def add(self, key: int) -> None:
        ndx, v = divmod(key, self.base)
        self.chsize(ndx)
        self.bs[ndx] |= 1 << v

    def remove(self, key: int) -> None:
        ndx, v = divmod(key, self.base)
        self.chsize(ndx)
        self.bs[ndx] &= ~(1 << v)

    def contains(self, key: int) -> bool:
        ndx, v = divmod(key, self.base)
        self.chsize(ndx)
        return bool(self.bs[ndx] & (1 << v))

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# CODE-END
