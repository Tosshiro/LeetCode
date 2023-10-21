'''
Description
LeetCode solution to 167. Two Sum II - Input Array Is Sorted

@author: Jw
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers solution
        left = 0
        right = len(numbers) - 1

        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1  # since list is sorted, decreasing right index will cause sum of both numbers to become lower
            else:
                left += 1  # increasing left index will cause sum of numbers to become higher


# Time complexity: O(n) (Worst case)
# Memory complexity: O(1) (No extra memory needed)