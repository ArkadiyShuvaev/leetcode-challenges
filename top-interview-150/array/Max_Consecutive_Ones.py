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
        if nums is None or len(nums) == 0:
            return 0

        current_consecutive_ones = 0
        max_consecutive_ones = 0

        for num in nums:
            if num:
                current_consecutive_ones += 1
            else:
                max_consecutive_ones = max(max_consecutive_ones, current_consecutive_ones)
                current_consecutive_ones = 0

        return max(max_consecutive_ones, current_consecutive_ones)


solution = Solution()
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1,0]))
print(solution.findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1]))
print(solution.findMaxConsecutiveOnes([0,0,0,0,0,1]))
print(solution.findMaxConsecutiveOnes([1,1,1,1,1,0]))