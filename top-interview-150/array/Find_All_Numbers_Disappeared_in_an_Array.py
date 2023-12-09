# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n


# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len == 1:
            return []

        all_numbers_set = set(range(1, nums_len + 1))

        for i in range(0, nums_len):
            value = nums[i]
            if value in all_numbers_set:
                all_numbers_set.remove(value)

        return list(all_numbers_set)

solution = Solution()


assert solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
assert solution.findDisappearedNumbers([4,3,2,7,8,2,3,2]) == [1, 5, 6] # [2, 2, 2, 3, 3, 4, 7, 8]
assert solution.findDisappearedNumbers([4,3,2,7,7,2,3,1]) == [5, 6, 8]
assert solution.findDisappearedNumbers([3,2]) == [1]
assert solution.findDisappearedNumbers([1,1]) == [2]
assert solution.findDisappearedNumbers([1,1,1]) == [2,3]
assert solution.findDisappearedNumbers([1]) == []
