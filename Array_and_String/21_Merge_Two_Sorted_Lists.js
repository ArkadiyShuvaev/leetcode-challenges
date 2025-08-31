// Has not been solved!

// 21. Merge Two Sorted Lists

// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists into one sorted list.
// The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.

// Example 1:
// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]

// Example 2:
// Input: list1 = [], list2 = []
// Output: []

// Example 3:
// Input: list1 = [], list2 = [0]
// Output: [0]

// Constraints:
// The number of nodes in both lists is in the range [0, 50].
// -100 <= Node.val <= 100
// Both list1 and list2 are sorted in non-decreasing order.


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} list1
 * @param {number[]} list2
 * @return {number[]}
 */
var mergeTwoLists = function (list1, list2) {
    const result = [];
    // Input: list1 = [2,2,4], list2 = [1,1,5]
    // Output: [1,1,2,2,4,5]

    let writePointer = 0;
    let list1Pointer = 0;
    let list2Pointer = 0;

    while (list1Pointer < list1.length) {

        if (list1[list1Pointer] <= list2[list2Pointer]) {
            result[writePointer] = list1[list1Pointer];
            writePointer++;
            list1Pointer++;
        }

        while (list1[list1Pointer] > list2[list2Pointer]) {
            result[writePointer] = list2[list2Pointer];
            writePointer++;
            list2Pointer++;
        }
    }

    while (list2Pointer < list2.length) {
        result[writePointer] = list2[list2Pointer];
        writePointer++;
        list2Pointer++;
    }

    return result;
};

let list1 = [2, 2, 4];
let list2 = [1, 1, 5];
console.info(`Actual: ${mergeTwoLists(list1, list2)}, Expected: [1,1,2,2,4,5]`);

list1 = [1, 2, 4];
list2 = [1, 3, 4];
console.info(`Actual: ${mergeTwoLists(list1, list2)}, Expected: [1,1,2,3,4,4]`);

list1 = [];
list2 = [];
console.info(`Actual: ${mergeTwoLists(list1, list2)}, Expected: []`);

list1 = [];
list2 = [0];
console.info(`Actual: ${mergeTwoLists(list1, list2)}, Expected: [0]`);

list1 = [];
list2 = [1, 2, 3, 4, 5, 6];
console.info(`Actual: ${mergeTwoLists(list1, list2)}, Expected: [1, 2, 3, 4, 5, 6]`);