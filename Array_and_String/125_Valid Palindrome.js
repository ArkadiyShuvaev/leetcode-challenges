// 125. Valid Palindrome

// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
// and removing all non-alphanumeric characters, it reads the same forward and backward.
// Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.

// Example 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.

// Example 2:
// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.

// Example 3:
// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.

// Constraints:
// 1 <= s.length <= 2 * 105
// s consists only of printable ASCII characters.


/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    let convertedString = "";

    for (let char of s) {
        const regExp = /^[a-zA-Z0-9]/;
        if (regExp.exec(char)) {
            convertedString += char.toLowerCase();
        }
    }

    if (convertedString.length <= 1) {
        return true;
    }

    let leftPointer = 0;
    let rightPointer = convertedString.length - 1;

    while (leftPointer < rightPointer) {
        if (convertedString.charAt(leftPointer) !== convertedString.charAt(rightPointer)) {
            return false;
        }
        leftPointer++;
        rightPointer--;
    }

    return true;
};

console.assert(isPalindrome("A man, a plan, a canal: Panama") === true)
console.assert(isPalindrome("race a car") === false)
console.assert(isPalindrome(" ") === true)
console.assert(isPalindrome("aA") === true)
console.assert(isPalindrome("0P") === false)
console.assert(isPalindrome("P") === true)