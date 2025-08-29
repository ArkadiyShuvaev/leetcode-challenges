// 414. Third Maximum Number
//
// Given an integer array nums, return the third distinct maximum number in this array.
// If the third maximum does not exist, return the maximum number.
//
// Example 1:
// Input: nums = [3,2,1]
// Output: 1
// Explanation:
// The first distinct maximum is 3.
// The second distinct maximum is 2.
// The third distinct maximum is 1.
//
// Example 2:
// Input: nums = [1,2]
// Output: 2
// Explanation:
// The first distinct maximum is 2.
// The second distinct maximum is 1.
// The third distinct maximum does not exist, so the maximum (2) is returned instead.
//
// Example 3:
// Input: nums = [2,2,3,1]
// Output: 1
// Explanation:
// The first distinct maximum is 3.
// The second distinct maximum is 2 (both 2's are counted together since they have the same value).
// The third distinct maximum is 1.
//
// Constraints:
// 1 <= nums.length <= 104
// -2^31 <= nums[i] <= 2^31 - 1

// Follow up: Can you find an O(n) solution?

/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {

    let first = -Infinity;
    let second = -Infinity;
    let third = -Infinity;

    for (const num of nums) {
        if (num === first || num === second || num === third) {
            continue;
        }

        if (num > first) {
            [first, second, third] = [num, first, second];
        } else if (num > second) {
            [second, third] = [num, second];
        } else if (num > third) {
            third = num;
        }
    }

    const result = third === -Infinity ? first : third;
    return result;
};

console.assert(thirdMax([5,6,1]) === 1, "[5,6,1]");
console.assert(thirdMax([2]) === 2, "[2]");
console.assert(thirdMax([6,7]) === 7, "[6,7]");
console.assert(thirdMax([6,7,6]) === 7, "[6,7,6]");
console.assert(thirdMax([3,2,3,1,2,4,5,5,6]) === 4, "[3,2,3,1,2,4,5,5,6]");
console.assert(thirdMax([1,2,2,5,3,5]) === 2, "[1,2,2,5,3,5]");
console.assert(thirdMax([2,2,3,1]) === 1, "[2,2,3,1]");
console.assert(thirdMax([2,2,3,1,1,1,2,3]) === 1);
console.assert(thirdMax([2]) === 2);
console.assert(thirdMax([1,2,3,4,6,1,2,6]) === 3);
// console.assert(thirdMax([1,2,3]) === 1);
