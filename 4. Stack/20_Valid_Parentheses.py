'''
Description
LeetCode solution to 20. Valid Parentheses

@author: Jw
'''

class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if "()" in s:
                s = s.replace("()", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            elif "[]" in s:
                s = s.replace("[]", "")

        if s != "":
            return False

        else:
            return True



