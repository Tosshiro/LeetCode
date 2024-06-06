'''
Description
LeetCode solution to 1512. Number of Good Pairs

@author: Jw
'''

from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Key = number in list, Value = Total appearance in the list
        numDict = dict()
        for num in nums:
            if num not in numDict.keys():
                numDict[num] = 1
            else:
                numDict[num] += 1
        
        pairs = 0
        for key in numDict:
            if numDict[key] > 1:
                pairs += comb(numDict[key], 2)
        
        return pairs