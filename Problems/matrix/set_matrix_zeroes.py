from typing import List
'''
Given an m x n integer matrix matrix, if an element is 0,
set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

'''
The Core Intuition for the In-Place Solution

The previous approach is logically sound. The question is,
how can we get that O(m + n) space for "free"?

The key insight is to realize that we can use a part of the
matrix itself as our memory.

What if we use the very first row of the matrix to track
which columns need to be zeroed, and the very first column
to track which rows need to be zeroed?

* If col j needs to be zeroed, we'll set matrix[0][j] = 0.
* If row i needs to be zeroed, we'll set matrix[i][0] = 0.

This is almost perfect, but it creates one critical ambiguity:
the cell matrix[0][0]. If matrix[0][0] becomes 0, does it mean
row 0 needs to be zeroed, or column 0? Or both?

To solve this, we treat the first row and first column as
special. We use two simple boolean flags (O(1) space) to
track their state, and then use the rest of the first
row/column as our markers for the rest of the matrix.

The Optimal In-Place Algorithm

This leads to a 4-step, in-place process:

Step 1: Check if the first row and first column have any
original zeros.
Before we start overwriting them, we need to know if they
were destined to be zeroed anyway. We use two boolean flags,
first_row_has_zero and first_col_has_zero, to record this.

Step 2: Use the first row/column to mark zeros for the rest
of the matrix. Iterate through the matrix, but skip the
first row and column (i.e., from i=1 to m-1 and j=1 to n-1).
If you find matrix[i][j] == 0, you don't change it yet.
Instead, you record this fact by setting its corresponding
markers: matrix[i][0] = 0 and matrix[0][j] = 0.

Step 3: Zero out the inner matrix based on the markers.
Iterate through the inner matrix again (from i=1, j=1).
For each cell matrix[i][j], look at its markers. If
matrix[i][0] == 0 or matrix[0][j] == 0, then this cell
must become zero. So, set matrix[i][j] = 0.

Step 4: Zero out the first row and column, if necessary.
This must be the final step. If we did it earlier, we would
have destroyed our markers. Now, we consult our flags from Step 1.
* If first_row_has_zero is true, set the entire first row to 0.
* If first_col_has_zero is true, set the entire first column to 0.
'''


def set_zeroes(matrix: List[List[int]]):
    """
    Do not return anything, modify matrix in-place instead.
    """
    first_row_has_zeros = False
    first_column_has_zeros = False
    num_rows, num_columns = len(matrix), len(matrix[0])
    # scan first row and first column to set flags.
    if 0 in matrix[0]:
        first_row_has_zeros = True
    for i in range(num_rows):
        if matrix[i][0] == 0:
            first_column_has_zeros = True
            break
    # scan the inner matrix, leaving the first row and
    # first column
    for r in range(1, num_rows):
        for c in range(1, num_columns):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    # zero out the inner matrix based on markers
    for r in range(1, num_rows):
        for c in range(1, num_columns):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    # zero out first row and column if necessary
    if first_row_has_zeros:
        for i in range(num_columns):
            matrix[0][i] = 0
    if first_column_has_zeros:
        for i in range(num_rows):
            matrix[i][0] = 0
    return matrix


def tests():
    inp = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    res = set_zeroes(inp)
    print(f"output for input {inp} is {res}")
    assert res == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    inp = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    res = set_zeroes(inp)
    print(f"output for input {inp} is {res}")
    assert res == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


tests()
