from typing import List
'''
Given an m x n matrix, return all elements of the
matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
'''
Intuition to solve

The "Four Boundaries" Approach

Imagine your matrix is a rectangular field. To walk
its perimeter, you need to know where its four
boundaries are. Let's define them with four variables:

* top: The index of the topmost row you need to read.
* bottom: The index of the bottommost row.
* left: The index of the leftmost column.
* right: The index of the rightmost column.

Initially, these four boundaries represent the full
dimensions of the matrix.

The Peeling Process

The process is a loop that repeats four simple steps
to peel one full outer layer:

1. Go Right →: Traverse the top row from the left
   boundary to the right boundary. Once you've read
   this entire row, you're done with it. You can
   now shrink your boundaries by moving the top
   boundary down by one.

2. Go Down ↓: Now, traverse the right column from
   the new top boundary down to the bottom boundary.
   This column is now fully read. Shrink your
   boundaries by moving the right boundary one step
   to the left.

3. Go Left ←: Traverse the bottom row, but this time
   in reverse, from the new right boundary back to
   the left boundary. This row is now peeled. Shrink
   your boundaries by moving the bottom boundary up
   by one.

4. Go Up ↑: Finally, traverse the left column in
   reverse, from the new bottom boundary up to the
   top boundary. This last part of the outer layer
   is complete. Shrink your boundaries by moving the
   left boundary one step to the right.

Repeat Until You're Done

After these four steps, you have successfully "peeled"
the outermost layer of the matrix. Your four boundary
variables (top, bottom, left, right) now define a new,
smaller rectangle inside the original one.

You simply repeat the exact same four-step process on
this new, smaller rectangle.

The entire process stops when the boundaries cross
each other (i.e., when top becomes greater than bottom,
or left becomes greater than right). At that point,
you know you have visited every element.

This method works for any size of matrix because the
boundary-shrinking logic naturally handles rectangular
shapes, squares, and even single rows or columns. For
a single row, for instance, you would complete Step 1
(Go Right), and then the top boundary would move past
the bottom boundary, causing the process to terminate
correctly.
'''


def spiral_matrix(matrix: List[List[int]]) -> List:
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    result = []
    while top <= bottom and left <= right:
        # peel the top layer, go right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        # peel the right side, go down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        # peel the bottom layer, go left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        # peel the leftmost side, go up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result


def tests():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = spiral_matrix(matrix)
    print(f"spiral output for matrix {matrix} is {res}")
    assert res == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    res = spiral_matrix(matrix)
    print(f"spiral output for matrix {matrix} is {res}")
    assert res == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


tests()
