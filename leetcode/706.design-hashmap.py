# Category: algorithms
# Level: Easy
# Percent: 66.71192%



# Design a HashMap without using any built-in hash table libraries.
# 
# Implement the MyHashMap class:
# 
# 
# 	MyHashMap() initializes the object with an empty map.
# 	void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# 	int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# 	void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
# 
# 
#  
# Example 1:
# 
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# 
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= key, value <= 10⁶
# 	At most 10⁴ calls will be made to put, get, and remove.
# 
 

# CODE-START
class Node:
    __slots__ = ('k', 'v', 'prev', 'next')
    def __init__(self, k: int, v: int, prev=None, next=None):
        self.k, self.v, self.prev, self.next = k, v, prev, next

class MyHashMap:
    def __init__(self):
        self.base = 32
        self.roots = list()
    
    def put(self, key: int, value: int) -> None:
        ndx = key // self.base
        if (d := ndx - len(self.roots)) >= 0:
            self.roots.extend([None] * (d + 1))

        node = dmy = Node(-1, -1, next=self.roots[ndx])
        while node.k != key and node.next is not None:
            node = node.next

        if node.k == key:
            node.v = value
        else:
            node.next = Node(k=key, v=value, prev=node)
        
        self.roots[ndx] = dmy.next
        if node is dmy:
            node.next.prev = None
        del dmy

    def get(self, key: int) -> int:
        ndx = key // self.base
        if ndx - len(self.roots) >= 0:
            return -1

        node = dmy = Node(-1, -1, next=self.roots[ndx])
        while node.k != key and node.next is not None:
            node = node.next

        return node.v if node.k == key else -1

    def remove(self, key: int) -> None:
        ndx = key // self.base
        if ndx - len(self.roots) >= 0:
            return

        node = dmy = Node(-1, -1, next=self.roots[ndx])
        while node.k != key and node.next is not None:
            node = node.next

        if node.k == key:
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.roots[ndx] = node.next

            if node.next is not None:
                node.next.prev = node.prev

            del node

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# CODE-END
