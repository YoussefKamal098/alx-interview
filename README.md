# alx-interview

# Table of Contents

1. [Lockboxes Problem](#lockboxes-problem)
   - [Problem Statement](#problem-statement)
   - [Function Prototype](#function-prototype)
2. [Solution Explanation](#solution-explanation)
   - [1. Initialization of the `unlocked_boxes` list](#1-initialization-of-the-unlocked_boxes-list)
   - [2. Recursive Box Unlocking (Depth-First Search)](#2-recursive-box-unlocking-depth-first-search)
   - [3. Starting from the First Box](#3-starting-from-the-first-box)
   - [4. Verification](#4-verification)
3. [Solution Code](#solution-code)
   - [Example Usage](#example-usage)
4. [Detailed Walkthrough](#detailed-walkthrough)
   - [Initialization](#initialization)
   - [Recursive Function (`tryUnlockBoxes`)](#recursive-function-tryunlockboxes)
   - [Final Check](#final-check)
5. [Time Complexity](#time-complexity)
6. [Space Complexity](#space-complexity)
7. [Edge Cases](#edge-cases)
   - [1. No boxes or only one box](#1-no-boxes-or-only-one-box)
   - [2. Unreachable boxes](#2-unreachable-boxes)
   - [3. Boxes containing no keys](#3-boxes-containing-no-keys)

### 1 - Lockboxes Problem

#### Problem Statement
You are given `n` number of locked boxes arranged sequentially, where each box is indexed from 0 to `n-1`. Each box may contain keys to open other boxes. The task is to determine whether all the boxes can be unlocked. The first box (`boxes[0]`) is already unlocked, and you must check if you can open all other boxes using the keys found inside.

#### Function Prototype
```python
def canUnlockAll(boxes)
```

- **Parameters:**
  - `boxes`: A list of lists. Each element in the list represents a box, and each box contains a list of keys that can unlock other boxes.

- **Return Value:**
  - `True` if all the boxes can be unlocked.
  - `False` if not all boxes can be unlocked.

### Solution Explanation

The function follows these steps to solve the problem:

1. **Initialization of the `unlocked_boxes` list:**
   - A list `unlocked_boxes` of length `n` (same as the number of boxes) is created, where each element is initially set to `False`. This list keeps track of which boxes have been unlocked.
   - The first box (`boxes[0]`) is always unlocked from the start.

2. **Recursive Box Unlocking (Depth-First Search):**
   - A helper function `tryUnlockBoxes(key)` is used to recursively unlock boxes. It accepts a `key` as input and performs the following:
     - Marks the box corresponding to the key as unlocked by setting `unlocked_boxes[key] = True`.
     - Then, it loops through all the keys found inside the current box and tries to unlock the corresponding boxes recursively by calling `tryUnlockBoxes` again. This ensures that as soon as a box is unlocked, all the keys it contains are checked to open other boxes.

3. **Starting from the First Box:**
   - The unlocking process starts by calling `tryUnlockBoxes(0)`, which attempts to unlock the first box and recursively any other boxes that can be unlocked from it.

4. **Verification:**
   - After attempting to unlock all possible boxes, the function checks the `unlocked_boxes` list to see if all boxes have been unlocked. If any box remains locked (`False`), the function returns `False`; otherwise, it returns `True`.

### [Solution Here](./0-lockboxes.py)

### Example Usage:
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes)) # Output True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes)) # Output True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes)) # Output False
```

### Detailed Walkthrough

- **Initialization:**
  - A list `unlocked_boxes = [False, False, False, ...]` is created, with length equal to the number of boxes. Initially, all boxes are locked (`False`).
  - The first box (`box 0`) is unlocked at the beginning, so the function starts by calling `tryUnlockBoxes(0)`.

- **Recursive Function (`tryUnlockBoxes`):**
  - When `tryUnlockBoxes(0)` is called, it unlocks the first box and retrieves any keys inside it. It then recursively attempts to unlock the boxes corresponding to those keys.
  - If a key opens a previously locked box, that box is marked as unlocked, and the process continues by attempting to open the boxes for the keys found in this newly unlocked box.
  
- **Final Check:**
  - After the recursive unlocking process completes, the function checks whether every box has been unlocked by looking through the `unlocked_boxes` list.
  - If every element in the `unlocked_boxes` list is `True`, meaning all boxes were unlocked, the function returns `True`. Otherwise, it returns `False` if any box remains locked.

### Time Complexity
- The time complexity of the solution is **O(n + k)**, where `n` is the number of boxes and `k` is the total number of keys inside all the boxes. The function visits each box once and processes each key once, making it efficient.

### Space Complexity
- The space complexity of the solution is **O(n)**, where `n` is the number of boxes. The space is primarily used for:
  - The `unlocked_boxes` list, which tracks the status of each box and requires **O(n)** space.
  - The recursive call stack, which can go as deep as `n` in the worst case, also contributing **O(n)** space.


### Edge Cases
1. **No boxes or only one box:** If there is only one box (`boxes = [[]]`), it is considered unlocked, so the function will return `True`.
2. **Unreachable boxes:** If some boxes do not contain the necessary keys to unlock others, the function will correctly return `False`.
3. **Boxes containing no keys:** If a box is present but contains no keys, this is handled, as the function continues attempting to unlock boxes based on previously found keys.

This solution ensures that all boxes are checked recursively and correctly handles cases where some boxes remain locked due to missing keys.
