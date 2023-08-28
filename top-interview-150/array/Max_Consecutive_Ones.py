# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        is_count_reset = False
        current_consecutive_ones = 0
        max_consecutive_ones = 0
        for _, item in enumerate(nums):
            if item == 1 and is_count_reset:
                is_count_reset = False
                current_consecutive_ones = 0

            if item == 1:
                current_consecutive_ones += 1
            else:
                is_count_reset = True
                max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)

        return max(max_consecutive_ones, current_consecutive_ones)


solution = Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1,0]))
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1]))
print(solution.findMaxConsecutiveOnes([0,0,0,0,0,1]))
print(solution.findMaxConsecutiveOnes([1,1,1,1,1,0]))