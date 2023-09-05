# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
 
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if arr is None or len(arr) < 3:
            return False

        isIncreasing = False
        isDecreasing = False
        
        for i in range(1, len(arr), 1):
            if arr[i] == arr[i - 1]:
                return False
            
            if isDecreasing == True and isIncreasing == False:
                return False

            if arr[i] > arr[i - 1]:
                isIncreasing = True
                if isDecreasing:
                    return False
            
            if arr[i] < arr[i - 1]:
                isDecreasing = True

        return isDecreasing and isIncreasing

solution = Solution()
print(solution.validMountainArray([1,3,2])) # True
print(solution.validMountainArray([2,1])) # False
print(solution.validMountainArray([3,5,5])) # False
print(solution.validMountainArray([0,3,2,1])) # True
print(solution.validMountainArray([0,2,3,5,2,1,0])) # True
print(solution.validMountainArray([0,2,3,5,2,7,1,0])) # False
print(solution.validMountainArray([0,2,3,3,5,2,1,0])) # False
