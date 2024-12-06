# Island Perimeter

## Overview

The **Island Perimeter** problem is a geometric challenge designed to test your understanding of 2D arrays, iterative algorithms, and conditional logic. The task is to calculate the perimeter of an island represented within a rectangular grid, where `1` indicates land and `0` indicates water. This problem is a practical application of matrix traversal and logic-based counting.

---

## Project Description

This project involves implementing a Python function `island_perimeter(grid)` that computes the perimeter of a single island within a given grid. The function ensures the following conditions:

- The grid contains only one island (or none).
- Cells of the island are connected either horizontally or vertically.
- The island is surrounded by water and contains no internal "lakes."

---

## Concepts Needed

To solve this problem, you should be familiar with the following topics:

### 1. **2D Arrays**
- Representing data as nested lists in Python.
- Iterating through rows and columns using nested loops.
- Accessing adjacent cells in a 2D grid for logical comparisons.

### 2. **Conditional Logic**
- Identifying when a grid cell contributes to the perimeter.
- Handling boundary cases (e.g., grid edges and corners).

### 3. **Algorithm Design**
- Decomposing the problem into subtasks:
    - Identifying land cells (`1`).
    - Calculating the perimeter contribution for each land cell.

### 4. **Python Basics**
- Writing and executing Python functions.
- Using nested loops and conditional statements.
- Adhering to PEP 8 coding standards.

---

## Requirements

### General

- Files should execute on Ubuntu 20.04 LTS using Python 3.4.3.
- Ensure all files are PEP 8 compliant.
- Use the line `#!/usr/bin/python3` at the start of all Python files.
- Avoid importing external modules; rely only on Python’s built-in features.
- All files and functions must include clear and concise documentation.
- The project must include a `README.md` file in the root directory.

---

## Task

### **Island Perimeter Function**

#### **Specifications**
- Create a function `def island_perimeter(grid):` that:
    - Takes a `grid` as input (a list of lists of integers).
    - Returns the perimeter of the island in the grid.

#### **Input Format**
- `grid`: A 2D list where:
    - `0` represents water.
    - `1` represents land.
    - Each cell is a square with side length `1`.
    - The grid is completely surrounded by water.

#### **Output**
- An integer representing the perimeter of the island.

---

## Implementation Details

### Approach

1. **Iterate Through the Grid**:
    - Use nested loops to traverse each cell in the grid.

2. **Identify Land Cells**:
    - Check if the current cell has a value of `1`.

3. **Calculate Perimeter Contribution**:
    - For each land cell, check its four neighbors (top, bottom, left, right).
    - Increment the perimeter count if the neighbor is water (`0`) or lies outside the grid.

4. **Edge Cases**:
    - Handle grids with no islands or fully water-filled grids.
    - Ensure calculations are correct at the grid's boundaries.

### Solution **[Here](./0-island_perimeter.py)**

---

## Example

### Input Grid
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

### Execution
```bash
./0-main.py
```

### Output
```
12
```

---

## Resources

1. **Python Documentation**:
    - [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-lists)
    - [Control Flow](https://docs.python.org/3/tutorial/controlflow.html)

2. **GeeksforGeeks**:
    - [2D Arrays in Python](https://www.geeksforgeeks.org/python-using-2d-arrays-lists/)

3. **TutorialsPoint**:
    - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

4. **YouTube**:
    - [Python Tutorials on Grid Problems](https://www.youtube.com/results?search_query=python+grid+problems)

---

## Testing

### Test Grid
```python
grid = [
    [1, 1],
    [1, 0]
]
```

### Test Script
```python
from 0-island_perimeter import island_perimeter

print(island_perimeter(grid))  # Output should be 8
```

---

## Submission Checklist

- [x] Python files are executable and PEP 8 compliant.
- [x] README.md is included and well-documented.
- [x] Code is thoroughly tested with edge cases.
- [x] Includes no external module imports.

**Repository**:
- **GitHub**: [alx-interview](https://github.com/alx-interview)
- **Directory**: `0x09-island_perimeter`
- **File**: `0-island_perimeter.py`

---

Happy coding! 🚀