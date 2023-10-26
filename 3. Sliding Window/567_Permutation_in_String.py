'''
Description
LeetCode solution to 567. Permutation in String

@author: Jw
'''

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Sliding Window
        left = 0
        count = Counter(s1)

        for right in range(len(s1), len(s2) + 1):
            if count == Counter(s2[left:right]):
                return True
            left += 1

        return False

# Time Complexity: O(n)
# Memory Complexity: O(1)