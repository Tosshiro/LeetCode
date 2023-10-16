'''
Description
LeetCode solution to 128. Longest Consecutive Sequence

@author: Jw
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0

        for i in nums:
            #check if its start of sequence
            if (i - 1) not in nums_set:
                length = 0
                #Check how long the length of consecutive elements is for every element in list
                while (i + length) in nums_set:
                    length += 1
                #subtstitute length if there is new higher longest consecutive elements
                count = max(count,length)

        return count

    # Time Complexity: O(n)
    # Memory Complexity: O(n)