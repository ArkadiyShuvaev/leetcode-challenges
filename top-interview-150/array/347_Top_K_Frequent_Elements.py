# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [-1]

# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_of_uniq_elements = defaultdict(int)
        # dict = {
        #     1: 3,
        #     2: 2,
        #     3: 1
        # }

        # dict2 = {
        #     1: 4,
        #     2: 4,
        #     3: 3
        # }
        result = []

        for elem in nums:
            dict_of_uniq_elements[elem] += 1

        for item in dict_of_uniq_elements.items():
            if item[1] >= k:
                result.append(item[0])

        if len(result) == len(dict_of_uniq_elements) and k != 1:
            return [-1]

        ordered = sorted(result)
        return ordered[:k]



solution = Solution()


assert solution.topKFrequent([3, 1, 1, 1, 2, 2], 2) == [1, 2]
assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert solution.topKFrequent([1], 1) == [1]
assert solution.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [-1]
assert solution.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2) == [-1]
