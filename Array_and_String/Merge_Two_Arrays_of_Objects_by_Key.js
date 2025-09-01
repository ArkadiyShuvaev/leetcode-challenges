// Merge Two Arrays of Objects by Key

// You are given two arrays of objects, arr1 and arr2,
// and a string key representing a property that exists in all objects.

// Implement a function mergeBy that merges these two arrays according to the following rules:

// 1. Objects with the same value for key are merged.
//   - If a property exists in both objects, the value from arr2 should overwrite the value from arr1.
//   - If a property exists in only one object, it should remain unchanged.
// 2. The order of elements in the final array must preserve the order of arr1 first.
//   - Merged objects remain in the position of their counterpart in arr1.
//   - Objects from arr2 that do not exist in arr1 should be appended in their original order.
// 3. Neither arr1 nor arr2 should be mutated.

// Return the resulting merged array.

// Function Signature
// /**
//  * @param {string} key
//  * @param {Object[]} arr1
//  * @param {Object[]} arr2
//  * @return {Object[]}
//  */
// function mergeBy(key, arr1, arr2) {
//     // your code here
// }

// Example 1
// const arr1 = [
//   { id: 2, name: 'Anakin', age: 10 },
//   { id: 0, name: 'Obi-Wan', side: 'light', age: 25 },
// ];

// const arr2 = [
//   { id: 1, name: 'Luke', side: 'light', age: 50 },
//   { id: 2, name: 'Darth Vader', side: 'dark' },
//   { id: 7, name: 'Yoda', side: 'light', age: 1000 },
// ];

// mergeBy('id', arr1, arr2);

// Output:
// [
//   { id: 2, name: 'Darth Vader', age: 10, side: 'dark' },
//   { id: 0, name: 'Obi-Wan', side: 'light', age: 25 },
//   { id: 1, name: 'Luke', side: 'light', age: 50 },
//   { id: 7, name: 'Yoda', side: 'light', age: 1000 },
// ]

// Example 2
// const arr1 = [
//   { username: 'alice', score: 10 },
// ];

// const arr2 = [
//   { username: 'bob', score: 15 },
//   { username: 'alice', level: 2 },
// ];

// mergeBy('username', arr1, arr2);


// Output:
// [
//   { username: 'alice', score: 10, level: 2 },
//   { username: 'bob', score: 15 },
// ]

// Constraints
// 1 <= arr1.length, arr2.length <= 10^4
// Each object contains at most 20 properties.
// key exists in all objects and has unique values within each array.
// Object property values are strings, numbers, or booleans.

/**
 * @param {string} key
 * @param {Object[]} arr1
 * @param {Object[]} arr2
 * @return {Object[]}
 */
function mergeBy(key, arr1, arr2) {
    const result = [];

    const map = new Map();

    for (const item of arr1) {
        const cloned = { ...item };
        map.set(item[key], cloned);
    }

    for (const item of arr2) {
        const keyValue = item[key];

        if (map.has(keyValue)) {
            const existing = map.get(keyValue);
            Object.assign(existing, item);
            continue;
        }

        const cloned = { ...item };
        map.set(keyValue, cloned);
    }

    return Array.from(map.values());
}

// === Base Example (merging + overwriting) ===
console.log(mergeBy(
  'id',
  [
    { id: 2, name: 'Anakin', age: 10 },
    { id: 0, name: 'Obi-Wan', side: 'light', age: 25 },
  ],
  [
    { id: 1, name: 'Luke', side: 'light', age: 50 },
    { id: 2, name: 'Darth Vader', side: 'dark' },
    { id: 7, name: 'Yoda', side: 'light', age: 1000 },
  ],
));
// [
//   { id: 2, name: 'Darth Vader', age: 10, side: 'dark' },
//   { id: 0, name: 'Obi-Wan', side: 'light', age: 25 },
//   { id: 1, name: 'Luke', side: 'light', age: 50 },
//   { id: 7, name: 'Yoda', side: 'light', age: 1000 },
// ]


// === Case 1: arr1 empty, arr2 non-empty ===
console.log(mergeBy(
  'id',
  [],
  [
    { id: 1, name: 'Luke' },
    { id: 2, name: 'Vader' },
  ],
));
// [
//   { id: 1, name: 'Luke' },
//   { id: 2, name: 'Vader' },
// ]


// === Case 2: arr2 empty, arr1 non-empty ===
console.log(mergeBy(
  'id',
  [
    { id: 3, name: 'Rey' },
    { id: 4, name: 'Kylo' },
  ],
  [],
));
// [
//   { id: 3, name: 'Rey' },
//   { id: 4, name: 'Kylo' },
// ]


// === Case 3: Disjoint keys (no overlap) ===
console.log(mergeBy(
  'id',
  [
    { id: 1, name: 'Ahsoka' },
  ],
  [
    { id: 2, name: 'Grogu' },
    { id: 3, name: 'Mando' },
  ],
));
// [
//   { id: 1, name: 'Ahsoka' },
//   { id: 2, name: 'Grogu' },
//   { id: 3, name: 'Mando' },
// ]


// === Case 4: Overlap with additional fields ===
console.log(mergeBy(
  'id',
  [
    { id: 10, username: 'alice', score: 5 },
  ],
  [
    { id: 10, level: 2 },
  ],
));
// [
//   { id: 10, username: 'alice', score: 5, level: 2 },
// ]


// === Case 5: Multiple properties overwritten ===
console.log(mergeBy(
  'id',
  [
    { id: 99, name: 'TempUser', active: true, score: 0 },
  ],
  [
    { id: 99, name: 'Admin', active: false, role: 'superuser' },
  ],
));
// [
//   { id: 99, name: 'Admin', active: false, score: 0, role: 'superuser' },
// ]


// === Case 6: Both arrays empty ===
console.log(mergeBy('id', [], []));
// []