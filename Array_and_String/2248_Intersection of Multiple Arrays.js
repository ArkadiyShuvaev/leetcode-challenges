// 2248. Intersection of Multiple Arrays

// Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers,
// return the list of integers that are present in each array of nums sorted in ascending order.

// Example 1:
// Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
// Output: [3,4]
// Explanation:
// The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4],
// and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

// Example 2:
// Input: nums = [[1,2,3],[4,5,6]]
// Output: []
// Explanation:
// There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].

// Constraints:
// 1 <= nums.length <= 1000
// 1 <= sum(nums[i].length) <= 1000
// 1 <= nums[i][j] <= 1000
// All the values of nums[i] are unique.

/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var intersection = function (nums) {
    const result = [];
    const map = new Map();

    if (nums.length === 1) {
        nums[0].sort((a, b) => a - b);
        return nums[0];
    }

    for (const number of nums[0]) {
        map.set(number, 1);
    }

    for (let subArrayIdx = 1; subArrayIdx < nums.length - 1; subArrayIdx++) {
        for (const number of nums[subArrayIdx]) {
            map.set(number, (map.get(number) || 0) + 1);
        }
    }

    // the last suArray
    for (const number of nums[nums.length - 1]) {
        if (!map.has(number)) {
            continue;
        }

        const numberCounts = map.get(number);
        if (numberCounts === nums.length - 1) {
            result.push(number);
        }
    }


    result.sort((a, b) => a - b);

    return result;
};

let testNums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
console.assert(intersection(testNums).toString() === [3, 4].toString(), "The 1st test failed")

testNums = [[1, 2, 3], [4, 5, 6]]
console.assert(intersection(testNums).toString() === [].toString(), "The 2nd test failed")

testNums = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]]
console.assert(intersection(testNums).toString() === [10,12,13,27,45].toString(), "The 3rd test failed")
