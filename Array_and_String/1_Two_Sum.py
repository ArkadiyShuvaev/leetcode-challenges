# 1. Two Sum

# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0,1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9

# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #        [2,7,11,15], 9
        # Index:  0 1  2  3
        index_of = {}

        for pointer_idx in range(len(nums) - 1):
            index_of[nums[pointer_idx]] = pointer_idx
            next_pointer_idx = pointer_idx + 1
            required_number = target - nums[next_pointer_idx]

            if required_number in index_of:
                return [index_of[required_number], next_pointer_idx]

        return []


solution = Solution()

assert solution.twoSum([2, 5, 5, 11], 10) == [1, 2]
assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
assert solution.twoSum([3, 3], 6) == [0, 1]
assert solution.twoSum([3, 2, 3], 6) == [0, 2]
