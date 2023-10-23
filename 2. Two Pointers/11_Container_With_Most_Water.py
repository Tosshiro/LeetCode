'''
Description
LeetCode solution to 11. Container With Most Water

@author: Jw
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer
        max_area = 0
        left = 0
        right = len(height) - 1

        for i in range(len(height)):
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            elif height[left] > height[right]:
                area = height[right] * (right - left)
                right -= 1

            # same height (left and right)
            else:
                area = height[left] * (right - left)
                left += 1

            if area > max_area:
                max_area = area

        return max_area

# Time complexity: O(n)
# Space complexity: O(1)
