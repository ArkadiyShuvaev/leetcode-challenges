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

# Out of range cases:
# 1. from left to rigth
# a.  m = -1 AND n = mat[0].length => m = m + 2, n = mat[i].length - 1
# b . m = -1                       => m = 0

# 2. from right to left
# a. n = -1 AND m = mat.length => n = n + 2, m = mat.length - 1
# b. n = -1                    => n = 0



#         -10      -13
#      00  01  02   03
#      10  11  12
# 2-1  20  21  22

# 00 -> -11 reset to 01, left_to_rigth = true
# 01 -> if (left_to_rigth == true)


from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        number_of_rest_elements = len(mat) * len(mat[0])
        result: List[int] = []
        is_left_to_right = True
        idx_m = 0
        idx_n = 0

        while(True):
            result.append(mat[idx_m][idx_n])
            print(result)
            number_of_rest_elements -= 1

            if (number_of_rest_elements <= 0):
                break

            if (is_left_to_right):
                idx_m -= 1
                idx_n += 1

                if idx_m == -1 and idx_n == len(mat[0]):# Both axes are out of their boards
                    idx_n = len(mat[0]) - 1
                    idx_m += 2
                    is_left_to_right = False
                elif idx_n == len(mat[0]):
                    idx_n = len(mat[0]) - 1
                    idx_m += 2
                    is_left_to_right = False
                elif idx_m == -1:
                    idx_m = 0
                    is_left_to_right = False

                continue

            idx_m += 1
            idx_n -= 1

            # a. n = -1 AND m = mat.length => n = n + 2, m = mat.length - 1
            # b. m = mat.length            => n = n + 2, m = mat.length - 1
            # c. n = -1                    => n = 0
            if idx_n == -1 and idx_m == len(mat):
                idx_m = len(mat) - 1
                idx_n += 2
                is_left_to_right = True
            elif idx_m == len(mat):
                idx_m = len(mat) - 1
                idx_n += 2
                is_left_to_right = True
            elif idx_n == -1:
                idx_n = 0
                is_left_to_right = True

        return result

solution = Solution()

# solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
assert solution.findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
assert solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
assert solution.findDiagonalOrder([[1,2],[3,4]]) == [1,2,3,4]
