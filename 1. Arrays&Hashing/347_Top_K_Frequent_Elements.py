'''
Description
LeetCode solution to 347. Top K Frequent Elements
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hset = set(nums)
        counter = {}  # Map num to counts
        for i in hset:
            counter[i] = nums.count(i)

        #Creating new sorted dictionary (descending)
        new_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        most_freq = []
        #Appending top k elements from dict into list
        for i in new_counter:
            if k > 0:
                most_freq.append(i[0])
            else:
                break
            k -= 1
        return most_freq

    #Time Complexity: O(n)
    #Memory Complexity: O(n)