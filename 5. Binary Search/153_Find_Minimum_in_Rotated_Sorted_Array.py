'''
Description
LeetCode solution to 153. Find Minimum in Rotated Sorted Array

@author: Jw
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # Base case
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break

            # Binary search
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                # Middle part is part of left portion, search right portion as it contains smaller values
                l = mid + 1
            else:
                # Middle part is part of right portion, search left as it contains smaller values
                r = mid - 1

        return res