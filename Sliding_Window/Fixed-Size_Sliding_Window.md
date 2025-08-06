### 🔍 What is the "Sliding Window Algorithm"?

At its core, the **Sliding Window Algorithm** is a technique to **reduce the time complexity** of algorithms that process **contiguous chunks** (or "windows") of data — especially in **arrays** or **strings**.

---

### 👣 Imagine This Situation:

You’re given an array:

```
[1, 3, 5, 2, 8, 1, 5]
```

And the task:

> Find the **maximum sum of any subarray** of size 3.

Instead of summing all possible subarrays of size 3 *from scratch*, we can:

1. Compute the first window sum: `1 + 3 + 5 = 9`
2. Slide the window by 1:

   * Subtract the element leaving the window (`1`)
   * Add the new element entering the window (`2`)
   * New sum: `9 - 1 + 2 = 10`
3. Repeat.

This avoids redundant work — and makes things **much faster**.

---

### ✅ When to Use It?

Use Sliding Window when:

* You're dealing with arrays or strings.
* You're working with **subarrays/substrings of fixed or variable length**.
* You want **optimal** performance (O(n)) instead of brute force (O(n²)).

---

### 🧠 Key Types of Sliding Window

| Type              | Description                                                                           |
| ----------------- | ------------------------------------------------------------------------------------- |
| **Fixed-size**    | Window size is constant (e.g., "length 3")                                            |
| **Variable-size** | You expand/shrink the window based on some condition (e.g., "at most K unique chars") |

---

### ✍️ Template for Fixed-Size Sliding Window (Python)

```python
def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```
