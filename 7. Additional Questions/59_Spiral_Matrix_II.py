'''
Description
LeetCode solution to 59. Spiral Matrix II

@author: Jw
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n 
        top, bottom = 0, n 

        # Create temporary placeholders (0) for matrix
        ans = [[0] * n for _ in range(n)]
        count = 1

        # count cannot be larger than the total number of boxes on board
        while count <= (n * n):
            # Add top row
            for i in range(left,right):
                ans[top][i] = count
                count += 1
            # Update top variable
            top += 1

            # Add right column
            for i in range(top, bottom):
                ans[i][right - 1] = count
                count += 1
            #Update right variable
            right -= 1

            # Add bottom row
            for i in range(right - 1, left - 1, -1):
                ans[bottom - 1][i] = count
                count += 1
            #Update bottom variable
            bottom -= 1

            # Add left column
            for i in range(bottom - 1, top - 1, -1):
                ans[i][left] = count
                count += 1
            #Update left variable
            left += 1
        
        return ans


        # Time Complexity: O(n^2), looping through every box on board, where there is (n x n) boxes
        # Space Complexity: O(1)