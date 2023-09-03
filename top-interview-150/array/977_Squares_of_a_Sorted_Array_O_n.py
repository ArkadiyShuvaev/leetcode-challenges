# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.


# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) == 0:
            return nums

        result = [0] * len(nums)

        l_pointer, r_pointer = 0, len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            l_value = nums[l_pointer] * nums[l_pointer]
            r_value = nums[r_pointer] * nums[r_pointer]

            if r_value > l_value:
                result[i] = r_value
                r_pointer -= 1
            else:
                result[i] = l_value
                l_pointer += 1

        return result

solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10])) # [0, 1, 9, 16, 100]
print(solution.sortedSquares([-12,-3,2,3,11])) # [4, 9, 9, 121, 144]
print(solution.sortedSquares([-7,-3,0,0,3,11])) # [0, 0, 9, 9, 49, 121]
