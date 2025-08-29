// 242. Valid Anagram

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// Example 1:
// Input: s = "anagram", t = "nagaram"
// Output: true

// Example 2:
// Input: s = "rat", t = "car"
// Output: false

// Constraints:
// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.

// Follow up: What if the inputs contain Unicode characters?
// How would you adapt your solution to such a case?

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    // s = "anagram", t = "nagaram"
    // const dict = {
    //     "a": 3,
    //     "n": 1,
    //     // ...
    // }

    // O(n)
    const map = new Map();

    for (const char of s) {
        if (char === " ") {
            continue;
        }

        if (!map.has(char)) {
            map.set(char, 1);
            continue;
        }

        let count = map.get(char);
        map.set(char, ++count);
    }


    for (const char of t) {
        if (char === " ") {
            continue;
        }

        if (!map.has(char)) {
            return false;
        }

        let count = map.get(char);
        const newCountValue = count - 1;

        if (newCountValue === 0) {
            map.delete(char);
            continue;
        }
        map.set(char, newCountValue);
    }

    return map.size === 0;
};

console.assert(isAnagram("anagram", "nagaram") === true);
console.assert(isAnagram("anagram", "nag a ram") === true);
console.assert(isAnagram("rat", "car") === false);
console.assert(isAnagram("eleven plus two", "twelve plus one") === true);