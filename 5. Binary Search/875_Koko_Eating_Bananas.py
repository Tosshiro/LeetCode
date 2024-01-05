'''
Description
LeetCode solution to 875. Koko Eating Bananas

@author: Jw
'''

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = max(piles)

        # Binary Search
        while low <= high:
            k = (high + low) // 2
            hrs = 0
            for pile in piles:
                # Round up value (EG: 7 banana / 4 banana per hour eaten = 2 when rounded up)
                hrs += math.ceil(pile / k)

            if hrs <= h:
                # Update res where theres a smaller k value
                res = min(res, k)
                high = k - 1
            else:
                low = k + 1

        return res