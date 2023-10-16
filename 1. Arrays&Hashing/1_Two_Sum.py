'''
Description
LeetCode solution to 1. Two Sum

@author: Jw
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap = {}  #Map val : index

        # run loop to form list containing tuples of idx & num value
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:    #Testing if two numbers add up to target, else add to dictionary
                return [prevMap[diff],i]
            prevMap[n] = i

#Time complexity: O(n)
#Memory: O(n)