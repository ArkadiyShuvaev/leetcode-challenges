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
    # It is O(n) complexity with extra memory (set)
    def findDisappearedNumbersUsingSet(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len == 1:
            return []

        all_numbers_set = set(range(1, nums_len + 1))

        for i in range(0, nums_len):
            value = nums[i]
            if value in all_numbers_set:
                all_numbers_set.remove(value)

        return list(all_numbers_set)

    # This method has O(n) complexity with O(1) memory (It is assumed the returned list does not count as extra space)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len == 1:
            return []

        disappeared_nums = []

        # Iterate through the array and mark the value at the current index as negative
        # if the value at the current index is positive.
        # If the value at the current index is negative, then it is already marked.
        for item in nums:
            idx = abs(item) - 1
            idx_value = nums[idx]
            if idx_value > 0:
                nums[idx] = -idx_value

        # Iterate through the array and add the index of the values that are positive
        # to the final result. The index of the values that are positive represent
        # the numbers that never appeared in the array.
        for i in range(0, nums_len):
            if nums[i] > 0:
                disappeared_nums.append(i + 1)

        return disappeared_nums

solution = Solution()


assert solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
assert solution.findDisappearedNumbers([1,1,1]) == [2,3]
assert solution.findDisappearedNumbers([4,3,2,7,8,2,3,2]) == [1, 5, 6] # [2, 2, 2, 3, 3, 4, 7, 8]
assert solution.findDisappearedNumbers([4,3,2,7,7,2,3,1]) == [5, 6, 8]
assert solution.findDisappearedNumbers([3,2, 3]) == [1]
assert solution.findDisappearedNumbers([1,1]) == [2]
assert solution.findDisappearedNumbers([1]) == []
