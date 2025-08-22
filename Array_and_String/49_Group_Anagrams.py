# 49. Group Anagrams
# Medium

# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        signatures = {}

        for idx, word in enumerate(strs):
            sign = "".join(sorted(word))

            if sign in signatures:
                signatures[sign].append(idx)
                continue

            signatures[sign] = []
            signatures[sign].append(idx)

        for sign in signatures:
            anargams = []
            values = signatures[sign]
            for idx in values:
                anargams.append(strs[idx])

            result.append(anargams)

        return result


solution = Solution()

# assert solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
assert solution.groupAnagrams([""]) == [[""]]
assert solution.groupAnagrams(["a"]) == [["a"]]
