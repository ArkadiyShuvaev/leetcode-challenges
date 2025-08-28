// The Problem has not been solved.

// 15. 3Sum

// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
// Notice that the solution set must not contain duplicate triplets.

// Example 1:
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.

// Example 2:
// Input: nums = [0,1,1]
// Output: []
// Explanation: The only possible triplet does not sum up to 0.

// Example 3:
// Input: nums = [0,0,0]
// Output: [[0,0,0]]
// Explanation: The only possible triplet sums up to 0.

// Constraints:
// 3 <= nums.length <= 3000
// -10^5 <= nums[i] <= 10^5

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
    // [-1,0,1,2,-1,-4]
    // 0 = 0 - 1 - (-1) = -1 + 1 = 0
    // 0 - 2 = -1 + (-1)
    const result = [];

    [-4, -1, -1, 0, 1, 2]
    // -4 + -1 + [0, 1, 2]
    // -1 + -1 + [1, 2]
    nums.sort((a, b) => a - b);

    for (let idx = 0; idx < nums.length - 2; idx++) {
        let leftIdx = idx + 1;

        for (let rightIdx = nums.length - 1; rightIdx > leftIdx; rightIdx--) {
            if (nums[idx] + nums[leftIdx] + nums[rightIdx] === 0) {
                result.push([nums[idx], nums[leftIdx], nums[rightIdx]])
            }
        }

    }

    return result;
};

let result = threeSum([0,0,0,0]);
console.info(`[0,0,0]: ${result}`)


result = threeSum([-1, 0, 1, 2, -1, -4]);
console.info(`[[-1,-1,2],[-1,0,1]]: ${result}`)

result = threeSum([0, 1, 1]);
console.info(`[]: ${result}`)

result = threeSum([0, 0, 0]);
console.info(`[0,0,0]: ${result}`)

