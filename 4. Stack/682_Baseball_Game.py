'''
Description
LeetCode solution to 682. Baseball Game


@author: Jw
'''

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                if len(stack) != 0:
                    stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                if len(stack) > 1:
                    stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
