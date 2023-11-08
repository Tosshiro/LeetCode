'''
Description
LeetCode solution to 22. Generate Parentheses
Hard question can look back on it

@author: Jw
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Add parentheses if open < n (Base case)
        # Add close parentheses if close < open
        # Open = Close

        stack = []
        res = []

        def backtrack(openN, closeN):
            # Base case
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                # Recursion
                backtrack(openN + 1, closeN)
                # Clear stack (global variable)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
