# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10E-05 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

# Constraints:
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            raise IndexError(nums)

        max_sum = sum(nums[:k])
        sum_range = max_sum

        for i in range(k, len(nums)):
            sum_range += nums[i] - nums[i - k]
            max_sum = max(sum_range, max_sum)

        return max_sum / k


solution = Solution()

assert solution.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
assert solution.findMaxAverage([5], 1) == 5.0
