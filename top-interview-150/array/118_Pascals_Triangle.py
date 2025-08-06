# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown

#        1           
#       1 1
#      1 2 1         1: 1; 2: 1 + 1; 1: 1
#     1 3 3 1        1: 1; 3: 1 + 2; 3: 2 + 1; 1: 1
#    1 4 6 4 1
#  1 5 10 10 5 1
# 1 6 15 20 15 6 1

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]
 
# Constraints:
# 1 <= numRows <= 30

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res: List[List[int]] = [[1]] # idx = 0
        
        if numRows == 1:
            return res
        
        for rowNumber in range(1, numRows): # numRows = 4 => 1, 2, 3
            res.append([])
            # res[rowNumber].append(...)
            parentRowFirstElementIdx = 0
            parentRowNextElementIdx = 0

            for j in range(0, rowNumber + 1):


            
        return res


solution = Solution()

# assert solution.generate(2) == [[1],[1,1]]
# assert solution.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# assert solution.generate(1) == [[[1]]]