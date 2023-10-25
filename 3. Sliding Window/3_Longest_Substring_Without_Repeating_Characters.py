'''
Description
LeetCode solution to 3. Longest Substring Without Repeating Characters

@author: Jw
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Record down duplicates
        char_set = set()

        longest_sub = 0
        # Sliding window method, two end pointers needed
        left = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            if len(char_set) > longest_sub:
                longest_sub = len(char_set)

        return longest_sub

# Time Complexity: O(n)   Runs through string once
# Space Complexity: O(n)