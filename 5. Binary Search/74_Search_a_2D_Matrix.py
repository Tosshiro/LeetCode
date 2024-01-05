'''
Description
LeetCode solution to 74. Search a 2D Matrix

@author: Jw
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix[0]) - 1

        for row in matrix:
            while low <= high:
                # Binary Search
                mid = (low + high) // 2

                if row[mid] == target:
                    return True  # Return true if target is in that row of the matrix
                elif row[mid] < target:
                    low = mid + 1
                elif row[mid] > target:
                    high = mid - 1

            low, high = 0, len(matrix[0]) - 1  # Reset values for low and high

        return False