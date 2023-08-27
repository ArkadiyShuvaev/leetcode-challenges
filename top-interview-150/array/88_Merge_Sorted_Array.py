# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# Example 4:
# Input: nums1 = [2,3,0,0,0,0], m = 2, nums2 = [1,2,5,6], n = 4
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [2,3] and [1,2,5,6].




# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109


# Follow up: Can you come up with an algorithm that runs in O(m + n) time?


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[0:] = nums2
            return
        if n == 0:
            return

        for i in range(0, m):
            if nums1[i] < nums2[0]:
                continue

            tmp = nums1[i]
            nums1[i] = nums2[0]
            self.__insert_in_increasing_order(tmp, nums2)

        nums1[m:] = nums2

    def __insert_in_increasing_order(self, number: int, arr: List[int]) -> None:
        arr[0] = number
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                break
            tmp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = tmp

solution = Solution()

arr1 = [0,0,0,0]
solution.merge(arr1, 0, [1,2,3,4], 4)
print(arr1)

arr1 = [1,2,3,4]
solution.merge(arr1, 4, [0], 0)
print(arr1)

arr1 = [2, 3, 4, 5, 0, 0, 0]
solution.merge(arr1, 4, [1, 2, 8], 3)
print(arr1)
