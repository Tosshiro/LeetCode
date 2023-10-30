'''
Description
LeetCode solution to 42. Trapping Rain Water

@author: Jw
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0

        # Two Pointer
        # Formula to check if can store water at that point (Current max pointer - current height at that point)
        while right > left:
            if max_left < max_right:
                left += 1
                # Check left pointer if can store water at that axis
                if max_left - height[left] > 0:
                    water += (max_left - height[left])
                max_left = max(max_left, height[left])

            else:
                right -= 1
                # Check right pointer if can store water at that axis
                if max_right - height[right] > 0:
                    water += (max_right - height[right])
                max_right = max(max_right, height[right])

        return water

# Time Complexity: O(n)
# Memory Complexity: O(1)

