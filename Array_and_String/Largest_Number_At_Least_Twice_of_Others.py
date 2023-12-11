# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as
# much as every other number in the array. If it is, return the index of the largest element,
# or return -1 otherwise.

# Example 1:
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.

# Constraints:
# 2 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = 0
        next_max_num = 0
        max_idx = -1

        for i in range(0, len(nums)):
            if nums[i] > max_num:
                next_max_num = max_num
                max_num = nums[i]
                max_idx = i

            elif nums[i] > next_max_num:
                next_max_num = nums[i]

        if max_num >= next_max_num * 2:
            return max_idx
        return -1

solution = Solution()

assert solution.dominantIndex([0,0]) == -1
assert solution.dominantIndex([3,6,1,0]) == 1
assert solution.dominantIndex([10,10]) == -1
assert solution.dominantIndex([1,2,3,4]) == -1
assert solution.dominantIndex([10,5,1,0]) == 0
assert solution.dominantIndex([10,5,1,9]) == -1
assert solution.dominantIndex([0,10]) == 1
