// 283. Move Zeroes

// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
// Note that you must do this in-place without making a copy of the array.

// Example 1:
// Input: nums = [0,0,1,3,12]
// Output: [1,3,12,0,0]

// Example 2:
// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]

// Example 3:
// Input: nums = [0]
// Output: [0]

// Constraints:
// 1 <= nums.length <= 10^4
// -2^31 <= nums[i] <= 2^31 - 1

// Follow up: Could you minimize the total number of operations done?


/**
 Do not return anything, modify nums in-place instead.
 @param { number[] } nums
 */
function moveZeroes(nums) {
    let insertIdx = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[insertIdx] = nums[i];
            if (insertIdx !== i) {
                nums[i] = 0;
            }
            insertIdx++;
        }
    }

};

let array = [0, 1, 0, 3, 12];
moveZeroes(array);
console.log(array);
console.assert(array.toString() === [1, 3, 12, 0, 0].toString());


array = [0, 0, 1, 3, 12];
moveZeroes(array);
console.log(array);
console.assert(array.toString() === [1, 3, 12, 0, 0].toString());

array = [1, 12, 3];
moveZeroes(array);
console.log(array);
console.assert(array.toString() === [1, 12, 3].toString());

array = [0];
moveZeroes(array);
console.log(array);
console.assert(array.toString() === [0].toString());

array = [45192,0,-659,-52359,-99225,-75991,0,-15155,27382,59818,0,-30645,-17025,81209,887,64648];
moveZeroes(array);
console.log(array);
console.assert(array.toString() === [45192,-659,-52359,-99225,-75991,-15155,27382,59818,-30645,-17025,81209,887,64648,0,0,0].toString());