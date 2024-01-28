'''
Description
LeetCode solution to 153. Find Minimum in Rotated Sorted Array

@author: Jw
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        low, high = 0, len(nums) - 1

        while low <= high:
            # Base case
            if nums[low] < nums[high]:
                res = min(res,nums[low])
                break

            # Binary search
            mid = (low + high) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[low]:
                # Middle part is part of left portion, search right portion as it contains smaller values
                low = mid + 1
            else:
                # Middle part is part of right portion, search left as it contains smaller values
                high = mid - 1

        return res