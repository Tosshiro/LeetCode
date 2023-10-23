'''
Description
LeetCode solution to 15. 3Sum

@author: Jw
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for ind, value in enumerate(nums):
            # To check if its duplicate value
            if ind > 0 and nums[ind - 1] == value:
                continue

            # Two pointer (Look at solution 167 similar two pointer solution)
            left = ind + 1
            right = len(nums) - 1

            while left < right:
                sum = value + nums[left] + nums[right]

                if sum == 0:
                    res.append([value, nums[left], nums[right]])
                    # might have more solutions with current index value
                    left += 1
                    # check if duplicate and make sure left pointer dont pass right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif sum > 0:
                    right -= 1

                elif sum < 0:
                    left += 1

        return res

# Time complexity: O(nlog(n)) + O(n^2)  -->  O(n^2)
# O(nlog(n)) from sorted function
# Memory Complexity: O(1)