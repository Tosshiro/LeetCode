'''
Description
LeetCode solution to 84. Largest Rectangle in Histogram
Hard question can look back at it

@author: Jw
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        # Stack approach
        stack = [] # Contains pair (index, height)
        for i in range(len(heights)):
            start = i
            # Check if stack is empty, and if stack top value is greater than heights[i]
            while stack and stack[-1][1] > heights[i]:
                # Pop if top value greater than heights[i]
                index, height = stack.pop()
                tmp_area = height * (i - index)
                max_area = max(max_area, tmp_area)
                # Extend start index to index of top value that was popped
                start = index
            stack.append((start,heights[i]))

        # Remaining values in stack, check whether there is larger rectangle area
        for i, h in stack:
            tmp_area = h * (len(heights) - i)
            max_area = max(max_area, tmp_area)
        
        return max_area

# Time complexity: O(n) , push and pop each element in heights once
# Space complexity: O(n), stack can be entire size of heights