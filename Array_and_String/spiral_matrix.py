# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Example 3:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]]
# Output: [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16

# Example 4:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16], [17,18,19,20]]
# Output: [1,2,3,4,8,12,16,20,19,18,17,13.....

#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16
# 17 18 19 20

# number_of_rows = 5
# number_of_columns = 4
# row_idx = 0
# row_idx = 4
# row_idx = 1
# row_idx = 3
# row_idx = 2
# number_of_row_iterations = int(number_of_rows / 2) + 1
# 1, 2, 3, 4, 5 => 1, 5, 2, 4, 3

# left_to_right = True
# top_to_down = True

# col_left_idx = 0
# col_right_idx = 3
# row_top_idx = 0
# row_bottom_idx = 3

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        number_elements_to_process = len(matrix) * len(matrix[0])
        current_step = -1
        row_length = len(matrix[0])
        col_length = len(matrix) - 1
        low_idx_m = 0
        high_idx_m = len(matrix) - 1
        left_idx_n = 0
        rigth_idx_n = len(matrix[0]) - 1

        while number_elements_to_process > 0:
            current_step += 1

            if current_step % 2 == 0:
                for n in range(0, row_length):
                    res.append(matrix[low_idx_m][n])
                    number_elements_to_process -= 1

                low_idx_m += 1
                continue

            res.append(arr[high_idx])
            high_idx -= 1

        print(res)

        print(res)
        # number_of_rows = len(matrix)
        # number_of_columns = len(matrix[0])
        # number_of_row_iterations = int(number_of_rows / 2) + 1

        # for m in range(number_of_rows):
        #     if m % 2 == 0:
        #         m_idx = m
        #     else:
        #         m_idx = number_of_rows - m
        #     print(m_idx)
        #     # for n in range(number_of_columns):

        return []


solution = Solution()
assert solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
