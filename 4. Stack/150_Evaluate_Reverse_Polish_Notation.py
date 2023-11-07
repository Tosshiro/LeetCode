'''
Description
LeetCode solution to 150. Evaluate Reverse Polish Notation

@author: Jw
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        # Use stack to solve
        stack = []
        for i in tokens:
            if i == "*":
                number = int(stack[-1]) * int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(number)

            elif i == "+":
                number = int(stack[-1]) + int(stack[-2])
                stack.pop()
                stack.pop()
                stack.append(number)

            elif i == "-":
                number = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(number)

            elif i == "/":
                number = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(number)

            # if element is number
            else:
                stack.append(i)

        return int(stack[0])

# Time complexity: O(n)
# Memory complexity: O(n)  (for loop for tokens)
