// 350. Intersection of Two Arrays II

// Given two integer arrays nums1 and nums2, return an array of their intersection.
// Each element in the result must appear as many times as it shows in both arrays
// and you may return the result in any order.

// Example 1:
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]

// Example 2:
// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Explanation: [9,4] is also accepted.

// Constraints:
// 1 <= nums1.length, nums2.length <= 1000
// 0 <= nums1[i], nums2[i] <= 1000

// Follow up:
// What if the given array is already sorted? How would you optimize your algorithm?
// What if nums1's size is small compared to nums2's size? Which algorithm is better?
// What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
    // Input: nums1 = [1,2,2,1], nums2 = [2,2]
    // Output: [2,2]

    const array_to_map = nums1.length < nums2.length ? nums1 : nums2;
    const array_to_iterate  = nums1.length < nums2.length ? nums2 : nums1;

    const result = [];
    const map = new Map();

    array_to_map.forEach((value) => {
        if (map.has(value)) {
            map.set(value, map.get(value) + 1);
        } else {
            map.set(value, 1);
        }
    });

    for (const number of array_to_iterate) {
        if (map.has(number)) {
            result.push(number);
            let valueInMap = map.get(number);
            valueInMap -= 1;

            if (valueInMap <= 0) {
                map.delete(number);
                continue;
            }

            map.set(number, valueInMap);
        }
    }

    return result;
};

let nums1 = [1, 2, 2, 1], nums2 = [2, 2]
console.assert(intersect(nums1, nums2).toString() === [2,2].toString())

nums1 = [4,9,5], nums2 = [9,4,9,8,4]
console.assert(intersect(nums1, nums2).toString() === [4,9].toString() || 
    intersect(nums1, nums2).toString() === [9,4].toString())
