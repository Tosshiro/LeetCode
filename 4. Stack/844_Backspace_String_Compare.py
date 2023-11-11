'''
Description
LeetCode solution to 844. Backspace String Compare


@author: Jw
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in s:
            if i == "#":
                if len(stack1) != 0:
                    stack1.pop()
            else:
                stack1.append(i)

        for i in t:
            if i == "#":
                if len(stack2) != 0:
                    stack2.pop()
            else:
                stack2.append(i)

        if "".join(stack1) == "".join(stack2):
            return True
        else:
            return False

    # Time Complexity: O(n), n = total length of s and t
    # Space complexity: O(n), if no "#" and whole string stored in stack list