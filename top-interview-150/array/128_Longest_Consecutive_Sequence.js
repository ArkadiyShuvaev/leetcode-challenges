// 128. Longest Consecutive Sequence
// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

// Example 1:
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

// Example 2:
// Input: nums = [0,3,7,2,5,8,4,6,0,1]
// Output: 9

// Example 3:
// Input: nums = [1,0,1,2]
// Output: 3


// Constraints:
// 0 <= nums.length <= 10^5
// -10^9 <= nums[i] <= 10^9

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
    // [100,4,200,1,3,2] === 4
    // { 100,4,200,1,3,2 }
    // -109, -108, -107, 1, ..... 108, 109

    const set = new Set();
    let longestSecuence = 0;

    for (let i = 0; i < nums.length; i++) {
        set.add(nums[i]);
    }
    // 100 -> longestSecuence: 1
    // 1 -> longestSecuence: 1, longestSecuence: 2
    let currentSecuenceLength = 0;
    for (let number = -109; number <= 109; number++) {
        if (set.has(number)) {
            currentSecuenceLength += 1;

            if (currentSecuenceLength > longestSecuence) {
                longestSecuence = currentSecuenceLength;
            }

            continue;
        }

        currentSecuenceLength = 0;
    }

    return longestSecuence;
};

console.assert(longestConsecutive([100,4,200,1,3,2]) === 4, "Test 1 failed");
console.assert(longestConsecutive([0,3,7,2,5,8,4,6,0,1]) === 9, "Test 2 failed");
console.assert(longestConsecutive([1,0,1,2]) === 3, "Test 3 failed");
console.assert(longestConsecutive([-100, -101, -1,0,1,2, 100, 101]) === 4, "Test 4 failed");
console.assert(longestConsecutive([]) === 0, "Test 5 failed");
