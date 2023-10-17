'''
Description
LeetCode solution to 704. Binary Search

@author: Jw
'''

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

        return -1

#Worst Time Complexity: O(log(n)), Best case O(1) if element is in middle of list
#Memory Complexity: O(1)        uses no extra space to search element
