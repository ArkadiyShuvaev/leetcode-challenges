// 347. Top K Frequent Elements
// Given an integer array nums and an integer k, return the k most frequent elements.
// You may return the answer in any order.

// Example 1:
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1, 2]

// Example 2:
// Input: nums = [1], k = 1
// Output: [1]

// Example 3:
// Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
// Output: [1, 2]

// Constraints:
// * 1 <= nums.length <= 10^5
// * -10^4 <= nums[i] <= 10^4
// * k is in the range [1, the number of unique elements in the array].
// * It is guaranteed that the answer is unique.

// Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    const map = new Map();

    // O(n)
    // map = {
    //     3: 1,
    //     1: 3,
    //     2: 2,
    //     7: 3
    // };
    for (const numb of nums) {
        if (!map.has(numb)) {
            map.set(numb, 1);
            continue;
        }

        let count = map.get(numb);
        map.set(numb, ++count);
    }

    // O(n)
    // frequencyMap = {
    //     1: [3],
    //     2: [2],
    //     3: [1, 7],
    //     4: []
    // }
    const frequencyMap = new Array();
    for (const item of map) {
        const key = item[0];
        const value = item[1];

        const existing = frequencyMap[value];
        if (existing === undefined) {
            frequencyMap[value] = [key];
            continue;
        }

        const newValue = [...existing, key];
        frequencyMap[value] = newValue;
    }

    const result = [];
    for (let i = frequencyMap.length - 1; i >= 0; i--) {
        const values = frequencyMap[i];
        if (values === undefined) {
            continue;
        }

        result.push(...values);
    }

    return result.slice(0, k);
};

let result = topKFrequent([1, 1, 1, 2, 2, 3], 2);
console.log(`[1, 2]: ${result}`);
console.assert(topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2], "Test 1 failed");
console.assert(topKFrequent([1], 1) == [1], "Test 2 failed");
console.assert(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2) == [1, 2], "Test 3 failed");
