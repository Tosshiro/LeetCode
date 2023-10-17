'''
Description
LeetCode solution to 36. Valid Sudoku

@author: Jw
'''

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Hashmap solution
        rows = defaultdict(set)  # Map index row value to values of nums in that row
        colms = defaultdict(set)  # Map index column value to values of nums in that column
        squares = defaultdict(set)  # Map key value (r//3, c//3) to values of that square

        for r in range(9):
            for c in range(9):
                # If current value is empty on board
                if board[r][c] == ".":
                    continue

                # Check if current value is duplicate in current row,colms or squares
                if (board[r][c] in rows[r] or
                        board[r][c] in colms[c] or
                        board[r][c] in squares[r // 3, c // 3]):
                    return False

                # Add current value to current row,colms and squares if not duplicate
                rows[r].add(board[r][c])
                colms[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])

        return True

# Time complexity: O(9^2)
# Space complexity: O(9^2)