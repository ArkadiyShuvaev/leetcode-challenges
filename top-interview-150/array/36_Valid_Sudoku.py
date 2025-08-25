# 36. Valid Sudoku

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true


# Example 2:
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false

# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.


# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # [0][0], [0][1], [0][2]...
        # [1][0], [1][1], [1][2]...
        for row_idx in range(0, 9):
            validation_set = set()
            for col_idx in range(0, 9):
                value = board[row_idx][col_idx]
                if value == ".":
                    continue

                if value in validation_set:
                    return False

                validation_set.add(value)

        # [0][0], [1][0], [2][0], [3][0]
        # [0][1], [1][1], [2][1], [3][1]
        for col_idx in range(0, 9):
            validation_set = set()
            for row_idx in range(0, 9):
                value = board[row_idx][col_idx]
                if value == ".":
                    continue

                if value in validation_set:
                    return False

                validation_set.add(value)

        # Iterate sub-boxes
        # [0][0], [0][1], [0][2]
        # [1][0], [1][1], [1][2]
        # [2][0], [2][1], [2][2]

        for box_row in range(3):
            for box_col in range(3):
                validation_set = set()
                for row in range(3):
                    for col in range(3):
                        value = board[box_row * 3 + row][box_col * 3 + col]
                        if value == ".":
                            continue

                        if value in validation_set:
                            return False

                        validation_set.add(value)

        return True

solution = Solution()

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
assert solution.isValidSudoku(board) is True

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

assert solution.isValidSudoku(board) is False

board = [
    ["5","3",".",".","5",".",".",".","."], # 5 and 5
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
assert solution.isValidSudoku(board) is False

board =[
    [".",".",".",".","5",".",".","1","."], # [0][0], [0][1], [0][2]
    [".","4",".","3",".",".",".",".","."], # [1][0], [1][1], [1][2]
    [".",".",".",".",".","3",".",".","1"], # [2][0], [2][1], [2][2]
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]

assert solution.isValidSudoku(board) is False
