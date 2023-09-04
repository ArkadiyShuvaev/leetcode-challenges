# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        result = nums_len
        buf_idx_r = nums_len - 1

        for i in range(nums_len - 1, -1, -1):
            if nums[i] == val:
                result -= 1
                if i == buf_idx_r: # process the found value at the end of the array
                    nums[i] = -100 # TODO Remove after debagging
                else:
                    nums[i] = nums[buf_idx_r]
                    nums[buf_idx_r] = -100 # TODO Remove after debagging
                    buf_idx_r -= 1
            else:
                if buf_idx_r == nums_len - 1 and result != nums_len: # this case occurs when the last element is the element that has to be removed.
                    buf_idx_r = i

        return result

solution = Solution()
nums = [0,2,2,2,4,5,6]
print(solution.removeElement(nums, val = 2)) # 3
print(nums) # [0,4,5,6,_,_,_]

nums = [0,1,2,2,3,0,4,2]
print(solution.removeElement(nums, val = 2)) # 3
print(nums) # [0,1,0,4,3,-100,-100,-100]

nums = [3,2,2,3]
print(solution.removeElement(nums, val = 3)) # 2
print(nums) # [2,2,_,_]

nums = [0,3,1,1,0,1,3,0,3,3,1,1]
print(solution.removeElement(nums, val = 1)) # 7
print(nums) # [0,3,3,3,0,0,3]