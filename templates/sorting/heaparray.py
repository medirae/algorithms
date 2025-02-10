#!/usr/bin/env python3

from math import floor, log2

class HeapArray:
    def __init__(self) -> None:
        self.array = list()
    
    @property
    def n(self) -> int:
        return len(self.array)

    @staticmethod
    def calculate_height(n: int) -> int:
        return floor(log2(n)) + 1

    @property
    def height(self) -> int:
        return self.calculate_height(self.n)

    def sorted(self) -> list[int]:
        return [self.pop() for _ in range(self.n)]

    def swap(self, findex: int, sindex: int):
        self[findex], self[sindex] = self[sindex], self[findex]

    def insert(self, el: int):
        self.array.append(el)
        self.bubbleup(self.n - 1)

    def extend(self, items: list[int]):
        for item in items:
            self.insert(item)

    def bubbleup(self, index: int):
        while index > 0 and self[self.parent(index)] > self[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def pop(self) -> int:
        self.swap(0, self.n - 1)
        value = self.array.pop()
        self.heapify(0)
        return value

    def heapify(self, index: int):
        while True:
            smallest = index
            if self.hasleft(index)  and self[self.left(index)] < self[smallest]:
                smallest = self.left(index)
            if self.hasright(index) and self[self.right(index)] < self[smallest]:
                smallest = self.right(index)
            
            if smallest == index:
                break

            self.swap(index, smallest)
            index = smallest

    @staticmethod
    def left(index: int) -> int:
        return 2 * index + 1
    
    @staticmethod
    def right(index: int) -> int:
        return 2 * index + 2
    
    @staticmethod
    def parent(index: int) -> int:
        return (index - 2 + index % 2) // 2

    def hasleft(self, index: int) -> bool:
        if 0 <= self.left(index) < self.n:
            return True
        return False
    
    def hasright(self, index: int) -> bool:
        if 0 <= self.right(index) < self.n:
            return True
        return False

    def hasparent(self, index: int) -> bool:
        if 0 <= self.parent(index) < self.n:
            return True
        return False

    @staticmethod
    def calculate_start_index(height: int) -> int:
        return 2 ** (height - 1)

    def height_nodes(self, height: int) -> list:
        start_index = self.calculate_start_index(height)
        end_index = self.calculate_start_index(height + 1) - 1
        
        if end_index >= self.n or start_index < 0 or end_index < start_index:
            return list()
        
        return self.array[start_index:end_index + 1]
    
    def __validateitem__(self, key):
        if not isinstance(key, int) and not isinstance(key, slice):
            raise TypeError(f"wrong type: {type(key)}. must be int or slice.")
        elif isinstance(key, int):
            return
        
        if key.step:
            raise ValueError(f"the third slice argument must not be provided: {key.step}")
        if key.stop > 2 or key.stop < 0:
            raise ValueError(f"the second slice argument must be 0:left or 1:right or 2:parent: {key.stop}")
        
    def __portitem__(self, key) -> int:
        if isinstance(key, int):
            return key
        
        index, child = key.start, key.stop
        if   child == 0:
            return self.left(index)
        elif child == 1:
            return self.right(index)
        elif child == 2:
            if index == 0:
                raise ValueError("the root does not have any parents.")
            return self.parent(index)

    def __getitem__(self, key):
        self.__validateitem__(key)
        return self.array[self.__portitem__(key)]
    
    def __setitem__(self, key, value):
        self.__validateitem__(key)
        if not str(value).isnumeric():
            raise ValueError(f"value should be of type numeric: {value}")
        
        self.array[self.__portitem__(key)] = value
    
    def __str__(self):
        self.tree(0)
        return str(self.array)
    
    def __repr__(self):
        return str(self)
    
    def tree(self, index, prefix=""):
        if 0 <= index < self.n:
            is_left = index % 2 == 1
            print(prefix + ("|-- " if is_left else "`--") + str(self[index]))
            new_prefix = prefix + ("|   " if is_left else "    ")
            self.tree(self.left(index), new_prefix)
            self.tree(self.right(index), new_prefix)

    def clear(self):
        self.array.clear()
    
    def __iter__(self):
        return iter(self.array)
    
    def __next__(self):
        return next(self.array)

def heapsort(items: list) -> list:
    h = HeapArray()
    h.extend(items)
    return h.sorted()
