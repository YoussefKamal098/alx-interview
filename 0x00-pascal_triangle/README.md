# Pascal's Triangle Problem

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Function Prototype](#function-prototype)
3. [Solution Explanation](#solution-explanation)
   - [1. Initialization](#1-initialization)
   - [2. Building the Triangle](#2-building-the-triangle)
   - [3. Returning the Result](#3-returning-the-result)
4. [Solution Code](#solution-code)
   - [Example Usage](#example-usage)
5. [Detailed Walkthrough](#detailed-walkthrough)
   - [Initialization](#initialization-1)
   - [Constructing Each Row](#constructing-each-row)
   - [Final Output](#final-output)
6. [Time Complexity](#time-complexity)
7. [Space Complexity](#space-complexity)
8. [Edge Cases](#edge-cases)
   - [1. Zero or Negative Input](#1-zero-or-negative-input)
   - [2. One Row Triangle](#2-one-row-triangle)
   - [3. Two Rows Triangle](#3-two-rows-triangle)

### Problem Statement
You are tasked with generating the first `n` rows of Pascal's Triangle. Each number in Pascal's Triangle is the sum of the two numbers directly above it. The triangle starts with a single `1` at the top.

### Function Prototype
```python
def pascal_triangle(n)
```

- **Parameters:**
  - `n`: An integer representing the number of rows to generate in Pascal's Triangle.

- **Return Value:**
  - A list of lists representing the first `n` rows of Pascal's Triangle.

### Solution Explanation

The function follows these steps to generate Pascal's Triangle:

1. **Initialization:**
   - If `n` is less than or equal to 0, an empty list is returned.
   - If `n` is equal to 1 or 2, the function returns the appropriate lists for the first row or two rows of the triangle.

2. **Building the Triangle:**
   - An initial triangle with the first two rows is created: `[[1], [1, 1]]`.
   - For each subsequent row, a new list is created where the first and last elements are `1`. The inner elements are calculated as the sum of the two elements from the previous row.

3. **Returning the Result:**
   - Finally, the triangle is returned after all rows have been constructed.

### [Solution Here](0-pascal_triangle.py)

### Example Usage:
```python
#!/usr/bin/python3

pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

print(pascal_triangle(0))  # Output: []
print(pascal_triangle(1))  # Output: [[1]]
print(pascal_triangle(2))  # Output: [[1], [1, 1]]
print(pascal_triangle(5))  # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
```

### Detailed Walkthrough

- **Initialization:**
  - The function first checks if `n` is less than or equal to 0. If so, it returns an empty list. For `n` equal to 1 or 2, it returns the corresponding simple lists representing Pascal's Triangle.

- **Constructing Each Row:**
  - Starting from the third row onward, the function creates each new row by initializing a list with `1`s at both ends. For the inner elements, it calculates the values by adding the two elements directly above them from the previous row. This process continues until all `n` rows are generated.

- **Final Output:**
  - After constructing all the rows, the complete triangle is returned.

### Time Complexity
- The time complexity of the solution is **O(n^2)**, where `n` is the number of rows. Each row contains an increasing number of elements, and the inner loop computes the values for each row.

### Space Complexity
- The space complexity is **O(n^2)** as well, due to the storage required for the list of lists that represent Pascal's Triangle.

### Edge Cases
1. **Zero or Negative Input:** If `n` is 0 or negative, the function returns an empty list since there are no rows to generate.
2. **One Row Triangle:** If `n` is 1, the function returns `[[1]]`, representing the single row of Pascal's Triangle.
3. **Two Rows Triangle:** If `n` is 2, the function returns `[[1], [1, 1]]`, representing the first two rows.
