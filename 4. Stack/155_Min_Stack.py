'''
Description
LeetCode solution to 155. Min Stack

Good question to get started with stack and oop

@author: Jw
'''


class MinStack:

    def __init__(self):
        self.stack = []
        # Min stack to keep track of minimum value
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Update min value
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()