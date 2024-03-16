'''
Description
LeetCode solution to 54. Spiral Matrix

@author: Jw
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time complexity: O(m*n), dimensions of matrix
        # Space complexity: O(1), no additional variables added

        ans = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # Keep looping until left cross right or top cross bottom
        while left < right and top < bottom:
            # Get top row
            for i in range(left,right):
                ans.append(matrix[top][i])
            # Update top value
            top += 1

            # Get right column
            for i in range(top,bottom):
                ans.append(matrix[i][right-1])
            #Update right
            right -= 1

            # Deal with single row/column testcase
            if not (left < right and top < bottom):
                break

            # Get bottom row
            for i in range(right - 1,left - 1, -1):
                ans.append(matrix[bottom-1][i])
            #Update bottom
            bottom -= 1

            # Get left column
            for i in range(bottom - 1,top - 1, -1):
                ans.append(matrix[i][left])
            #Update left
            left += 1
        
        return ans
        