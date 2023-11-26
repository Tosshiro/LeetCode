'''
Description
LeetCode solution to 392. Is Subsequence


@author: Jw
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left1 = 0
        left2 = 0
        # Two pointer, one for each string and both start from the left
        while left1 < len(s) and left2 < len(t):
            if s[left1] == t[left2]:
                left1 += 1
            left2 += 1

        return left1 == len(s)

    # Time Complexity: O(n)  (n = len(t))
    # Space Complexity: O(1)