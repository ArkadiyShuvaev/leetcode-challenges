# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.
 

# Constraints:
# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        uniq_values = set()
        
        for item in arr:
            if 2 * item in uniq_values or item / 2 in uniq_values:
                return True
            uniq_values.add(item)

        return False

solution = Solution()
print(solution.checkIfExist([10,2,5,3])) # true
print(solution.checkIfExist([5,2,10,3])) # true
print(solution.checkIfExist([4,2,5,3])) # true
print(solution.checkIfExist([2,4,5,3])) # true
print(solution.checkIfExist([3,1,7,11])) # false
