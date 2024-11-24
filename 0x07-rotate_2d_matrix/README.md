# Rotate 2D Matrix Problem

### Problem Breakdown

1. **Matrix Representation**: A 2D matrix can be represented as a list of lists in Python. For example:
   ```python
   matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
   ```

2. **90-degree Rotation Logic**: A 90-degree clockwise rotation means that the rows of the matrix will become the columns in reverse order.

   To rotate the matrix in place, the best approach is to:
    - **Transpose the matrix**: Convert rows to columns.
    - **Reverse each row**: After transposing, reversing each row gives the rotated matrix.

   ### Steps:
    1. **Transpose**: Swap matrix[i][j] with matrix[j][i].
    2. **Reverse each row**: After transposing, reverse the elements of each row.

### Solution

[**`Solution here`**](./0-rotate_2d_matrix.py)

### Explanation

1. **Transposition**:
    - For each pair of elements (i, j) where `i < j`, swap the elements `matrix[i][j]` with `matrix[j][i]`. This converts the rows into columns.

2. **Reversing each row**:
    - After transposition, each row of the matrix needs to be reversed to achieve the 90-degree clockwise rotation.

### Time Complexity

- **Transpose**: We loop through the upper triangular part of the matrix, which is `O(n^2)` where `n` is the size of the matrix.
- **Reverse each row**: Reversing each row takes `O(n)` time, and since there are `n` rows, this step also takes `O(n^2)`.

Thus, the overall time complexity of the algorithm is **O(n^2)**.

### Space Complexity

- Since the problem asks for an in-place rotation, we do not use any additional data structures other than the input matrix.
- The space complexity is **O(1)** because no extra space is used apart from the matrix itself.

### Test Cases

Let's test the solution with different inputs:

#### Test Case 1: 3x3 Matrix
```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
```

**Expected Output**:
```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

#### Test Case 2: 4x4 Matrix
```python
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

rotate_2d_matrix(matrix)
print(matrix)
```

**Expected Output**:
```python
[[13, 9, 5, 1],
 [14, 10, 6, 2],
 [15, 11, 7, 3],
 [16, 12, 8, 4]]
```

#### Test Case 3: 2x2 Matrix
```python
matrix = [[1, 2],
          [3, 4]]

rotate_2d_matrix(matrix)
print(matrix)
```

**Expected Output**:
```python
[[3, 1],
 [4, 2]]
```
