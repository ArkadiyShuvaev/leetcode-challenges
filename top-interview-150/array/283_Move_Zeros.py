# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?


from typing import List


# Solution with space O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if nums is None or len(nums) == 0:
            return

        write_idx = 0
        read_idx = 0

        while read_idx < len(nums):
            if nums[read_idx] != 0:
                nums[write_idx] = nums[read_idx]
                write_idx += 1

            read_idx += 1
            
        for i in range(write_idx, len(nums)):
            nums[i] = 0
    
    def moveZeroes_space_O_n(self, nums: List[int]) -> None:
        if nums is None or len(nums) == 0:
            return

        result = []
        read_idx = 0

        while read_idx < len(nums):
            if nums[read_idx] != 0:
                result.append(nums[read_idx])

            read_idx += 1

        nums[0:len(result)] = result
        for i in range(len(result), len(nums)):
          nums[i] = 0
        
solution = Solution()

nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums) # [1,3,12,0,0]

nums = [1, 1]
solution.moveZeroes(nums)
print(nums) # 1, 1

nums = [0]
solution.moveZeroes(nums)
print(nums) # 0

nums = [0, 0]
solution.moveZeroes(nums)
print(nums) # 0, 0

nums = [1, 0]
solution.moveZeroes(nums)
print(nums) # 1, 0

nums = [0, 1]
solution.moveZeroes(nums)
print(nums) # 1, 0
