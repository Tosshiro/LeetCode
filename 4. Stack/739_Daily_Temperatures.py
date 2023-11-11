'''
Description
LeetCode solution to 739. Daily Temperatures

Hard question can look back at it

@author: Jw
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = [0] * len(temperatures)
        stack = []  # append [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                temp[stackInd] = (i - stackInd)
            stack.append([t, i])

        return temp

#Time complexity: O(n)