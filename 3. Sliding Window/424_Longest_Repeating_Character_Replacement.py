'''
Description
LeetCode solution to 424. Longest Repeating Character Replacement

@author: Jw
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        letter_dic = {}
        longest_sub = 0

        # Sliding Window
        left = 0
        for right in range(len(s)):
            # add character R
            letter_dic[s[right]] = 1 + letter_dic.get(s[right], 0)

            max_f = letter_dic.values()
            while (right - left + 1) - max(max_f) > k:
                letter_dic[s[left]] -= 1
                left += 1

            longest_sub = max(right - left + 1, longest_sub)

        return longest_sub

# Time Complexity: O(n)   Runs through string once
# Space Complexity: O(1)