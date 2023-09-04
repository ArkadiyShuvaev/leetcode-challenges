# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
 
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 9


from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        idx = 0
        while idx < len(arr):
            if arr[idx] == 0:
                for i in range(len(arr) - 1, idx, -1): # [0, 1, 2, 3, 4]
                    arr[i] = arr[i-1]
                idx += 2
            else:
                idx += 1
        return
    
    # This solution is several times faster
    def duplicateZeros_Copilot_Solution(self, arr: List[int]) -> None:
        # Count the number of zeros
        num_zeros = 0
        for num in arr:
            if num == 0:
                num_zeros += 1
        
        # Iterate through the array from the end and copy the elements to their new positions
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + num_zeros < n:
                arr[i+num_zeros] = arr[i]
            if arr[i] == 0:
                num_zeros -= 1
                if i + num_zeros < n:
                    arr[i+num_zeros] = 0
        return

solution = Solution()
arr = [1,0,2,3,0,4,5,0]
solution.duplicateZeros_Copilot_Solution(arr)
print(arr) #[1,0,0,2,3,0,0,4]

arr = [1,2,3]
solution.duplicateZeros(arr)
print(arr) #[1,2,3]

arr = [0,0,3]
solution.duplicateZeros(arr)
print(arr) #[0,0,0]

arr = [0,0,0]
solution.duplicateZeros(arr)
print(arr) #[0,0,0]

arr = [0,1,0]
solution.duplicateZeros(arr)
print(arr) #[0,0,1]