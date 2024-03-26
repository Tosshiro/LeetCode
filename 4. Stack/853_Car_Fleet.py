'''
Description
LeetCode solution to 853. Car Fleet

@author: Jw
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_zipped = list(zip(position, speed))
        # Sort zipped lists by positions
        cars = sorted(cars_zipped, key = lambda x: x[0])

        # Start from the cars closest to target as cars furthest from destination might travel at different speeds (Collide with other cars)
        # One pointer
        right = len(cars) - 1
        while right > 0:
            time1, time2 = (target - cars[right][0]) / cars[right][1], (target - cars[right -1][0]) / cars[right - 1][1]
            # If car behind takes lesser time to reach destination than the car infront, the car behind will catch up to the car in front
            if time1 >= time2:
                # Remove the car behind and form one car fleet
                cars.pop(right-1)
                right = len(cars) - 1
            # If car behind cannot catch up
            else:
                right -= 1

        return len(cars)
    

# Time complexity: O(nlogn) -> Sort cars list and also loop through cars list with n elements
# Space complexity: O(n), new cars list created