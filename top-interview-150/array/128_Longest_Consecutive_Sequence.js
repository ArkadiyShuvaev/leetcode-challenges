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
    const set = new Set(nums);

    let longestSecuence = 0;
    let currentSecuenceLength = 0;

    for (const number of set) {
        // Only start when there is no predecessor
        if (!set.has(number - 1)) {
            let startNumber = number;

            while (set.has(startNumber++)) {
                currentSecuenceLength++;
            }

            longestSecuence = Math.max(longestSecuence, currentSecuenceLength);
            currentSecuenceLength = 0;
        }
    }

    return longestSecuence;
};

console.assert(longestConsecutive([100,4,200,1,3,2]) === 4, "Test 1 failed");
console.assert(longestConsecutive([0,3,7,2,5,8,4,6,0,1]) === 9, "Test 2 failed");
console.assert(longestConsecutive([1,0,1,2]) === 3, "Test 3 failed");
console.assert(longestConsecutive([-100, -101, -1,0,1,2, 100, 101]) === 4, "Test 4 failed");
console.assert(longestConsecutive([]) === 0, "Test 5 failed");

const startDt = new Date();
console.assert(longestConsecutive([0,1,2,4,8,5,6,7,9,3,55,88,77,99,999999999]) === 10)
const stopDt = new Date();

const diff = (stopDt.getTime() - startDt.getTime());
console.info(`Diff in seconds: ${diff/1000}`);
