# Category: algorithms
# Level: Hard
# Percent: 66.92855%



# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
# 
# Implement the FreqStack class:
# 
# 
# 	FreqStack() constructs an empty frequency stack.
# 	void push(int val) pushes an integer val onto the top of the stack.
# 	int pop() removes and returns the most frequent element in the stack.
# 	
# 		If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
# 	
# 	
# 
# 
#  
# Example 1:
# 
# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]
# 
# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= val <= 10⁹
# 	At most 2 * 10⁴ calls will be made to push and pop.
# 	It is guaranteed that there will be at least one element in the stack before calling pop.
# 
 

# CODE-START
class FreqStack:
    def __init__(self):
        self.vs = dict()
        self.fs = dict()
        self.mf = 0

    def push(self, val: int) -> None:
        f = self.vs.get(val, 0) + 1
        self.vs[val] = f

        if f not in self.fs:
            self.fs[f] = list()
        
        self.fs[f].append(val)
        if f > self.mf:
            self.mf = f
        
    def pop(self) -> int:
        f = self.mf

        val = self.fs[f].pop()
        self.vs[val] -= 1
        if self.vs[val] == 0:
            del self.vs[val]
        
        if not self.fs[f]:
            del self.fs[f]
            self.mf = f - 1
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# CODE-END
