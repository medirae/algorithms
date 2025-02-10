#!/usr/bin/env python3

from math import floor, log2

class Node:
    def __init__(self, value: int,
                 parent: "Node" = None,
                 left: "Node" = None,
                 right: "Node" = None):
        self.value: int = value
        self.parent: "Node" = parent
        self.left: "Node" = left
        self.right: "Node" = right

    def swap(self, node: "Node"):
        self.value, node.value = node.value, self.value

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str(self.value)

class HeapBTree:
    """Max Heap Binary Tree"""

    def __init__(self, root: "Node" = None):
        self.n = 0
        self.root: "Node" = root
        self.last: "Node" = root
        
        if self.root is not None:
            self.n += 1
    
    def __iter__(self):
        return HeapBTree.Iterator(self.root)

    class Iterator:
        """preorder traversal iterator for HeapBTree"""
        def __init__(self, root):
            self.stack = [root]

        def __iter__(self):
            return self
        
        def __next__(self):
            while self.stack:
                current_node = self.stack.pop()

                if current_node.right:
                    self.stack.append(current_node.right)
                if current_node.left:
                    self.stack.append(current_node.left)

                return current_node
            raise StopIteration

    @property
    def height(self):
        return self.calculate_height(self.n)
    
    @staticmethod
    def calculate_height(n: int) -> int:
        if n > 0:
            return floor(log2(n)) + 1
        return 0

    @classmethod
    def get_route(cls, n: int) -> list[int]:
        if n == 0:
            return list()
        height = cls.calculate_height(n)
        preheight_nodes = 2 ** (height - 1) - 1
        height_nodes = n - preheight_nodes

        route = list()
        node_meter = 0
        for height in range(height - 1, 0, -1):
            divider = 1/2 * (2 ** height)
            if height_nodes - node_meter <= divider:
                route.append(0)
            else:
                route.append(1)
                node_meter += divider
        
        return route
    
    def traverse_route(self, route: list) -> "Node":
        node = self.root
        for idx in range(len(route)):
            if route[idx] == 0:
                if node.left is None:
                    return node
                node = node.left
            else:
                if node.right is None:
                    return node
                node = node.right
        return node

    def insert(self, node: "Node"):
        if self.n == 0:
            self.root = node
            self.n += 1
            return

        route = self.get_route(self.n + 1)
        parent = self.traverse_route(route)
        if route[-1] == 0:
            parent.left = node
        else:
            parent.right = node
        node.parent = parent
        self.n += 1

        self.bubbleup_node(node)
    
    def heapify_node(self, node: "Node"):
        if node is None:
            return

        while True:
            smallest = node
            if node.left is not None and node.left.value < smallest.value:
                smallest = node.left
            if node.right is not None and node.right.value < smallest.value:
                smallest = node.right
            
            if smallest is node:
                break
            
            node.swap(smallest)
            node = smallest

    def bubbleup_node(self, node: "Node"):
        if node is None:
            return
        
        while node.parent is not None and node.parent.value > node.value:
            node.swap(node.parent)
            node = node.parent

    def pop(self) -> int:
        if self.n == 0:
            return
        if self.n == 1:
            value = self.root.value
            self.root = None
            self.n -= 1
            return value

        last_node = self.traverse_route(self.get_route(self.n))
        if last_node is None or last_node.parent is None:
            return
        value = self.root.value

        if  last_node.parent.left is last_node:
            last_node.parent.left = None
        elif last_node.parent.right is last_node:
            last_node.parent.right = None
        last_node.parent = None
        if self.root.left is not None:
            last_node.left = self.root.left
            self.root.left.parent = last_node
        if self.root.right is not None:
            last_node.right = self.root.right
            self.root.right.parent = last_node
        self.root = last_node
        self.n -= 1
        
        self.heapify_node(self.root)
        return value

    def extend(self, items: list):
        for item in items:
            self.insert(Node(item))

    def sorted(self) -> list:
        return [self.pop() for _ in range(self.n)]

    def print(self, node, prefix="", is_left=True):
        if node is not None:
            print(prefix + ("|-- " if is_left else "`--") + str(node.value))
            new_prefix = prefix + ("|   " if is_left else "    ")
            self.print(node.left, new_prefix, True)
            self.print(node.right, new_prefix, False)

    def __repr__(self):
        self.print(self.root)
        return str()

def heapsort(items: list):
    heap = HeapBTree()
    heap.extend(items)
    return heap.sorted()
