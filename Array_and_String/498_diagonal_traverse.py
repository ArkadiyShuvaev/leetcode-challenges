# Given an m x n matrix mat, return an array of all
# the elements of the array in a diagonal order.

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]


# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# -105 <= mat[i][j] <= 105

# https://stackoverflow.com/a/20422854/3394179


# 1. (m, n) = (3, 3)
# 1 2 3
# 4 5 6
# 7 8 9

# Result: 1, 2, 4, 7, 5, 3, 6, 8, 9

# (m, n) = (3, 4)
# 1  2  3  4
# 5  6  7  8
# 9 10 11 12

# Result: 1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12

# (m, n) = (5, 2)
# 1  2
# 3  4
# 5  6
# 7  8
# 9 10

# Result: 1, 2, 3, 5, 4, 6, 7, 9, 8, 10

# (m, n) = (2, 5)
# 1 2 3 4 5
# 6 7 8 9 10

# Result: 1, 2, 6, 7, 3, 4, 8, 9, 5, 10

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        number_of_rest_elements = len(mat) * len(mat[0])
        result: List[int] = []
        is_left_to_right = True
        idx_m = 0
        idx_n = 0

        while number_of_rest_elements > 0:
            result.append(mat[idx_m][idx_n])
            number_of_rest_elements -= 1

            if is_left_to_right:
                idx_m -= 1
                idx_n += 1

                if idx_m < 0 or idx_n >= len(mat[0]):
                    if idx_n >= len(mat[0]):
                        idx_n = len(mat[0]) - 1
                        idx_m += 2
                    else:
                        idx_m = 0

                    is_left_to_right = False

                continue

            idx_m += 1
            idx_n -= 1

            # a. n = -1 AND m = mat.length => n = n + 2, m = mat.length - 1
            # b. m = mat.length            => n = n + 2, m = mat.length - 1
            # c. n = -1                    => n = 0
            if idx_n < 0 or idx_m >= len(mat):
                if idx_m >= len(mat):
                    idx_m = len(mat) - 1
                    idx_n += 2
                else:
                    idx_n = 0

                is_left_to_right = True

        return result

solution = Solution()

# solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
assert solution.findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
assert solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
assert solution.findDiagonalOrder([[1,2],[3,4]]) == [1,2,3,4]
