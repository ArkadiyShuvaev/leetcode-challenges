# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.

# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

from math import inf
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result_arr: List[int] = []
        processed_numbers = set()
        
        for item in nums:
            if item in processed_numbers:
                continue
            
            if len(result_arr) < 3:
                result_arr.append(item)
                processed_numbers.add(item)
                continue
            
            min_value = min(result_arr)
            if item > min_value:
                idx_of_min_value = result_arr.index(min_value)
                result_arr[idx_of_min_value] = item
                processed_numbers.add(item)

        return min(result_arr) if len(result_arr) == 3 else max(result_arr)
        

solution = Solution()


print(solution.thirdMax([3,2,3,1,2,4,5,5,6])) # 4
print(solution.thirdMax([1,2,2,5,3,5])) # 2
print(solution.thirdMax([2,2,3,1])) # 1
print(solution.thirdMax([2,2,3,1,1,1,2,3])) # 1
print(solution.thirdMax([2])) # 2
print(solution.thirdMax([1,2,3,4,6,1,2,6])) # 3
print(solution.thirdMax([1,2,3])) # 1
print(solution.thirdMax([6,7])) # 7
