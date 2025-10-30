from typing import List
'''
You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you
have to modify the input 2D matrix directly. DO NOT
allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],
                [13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],
        [16,7,10,11]]
'''
'''
The key to this problem is figuring out how to
move all the numbers to their new spots without
using a second matrix to temporarily store them.
While you could try to rotate it shell by shell
(like an onion), there's a much more elegant and
easier-to-implement two-step trick.

The "Transpose and Reverse" Method

A 90-degree clockwise rotation is the same as
performing two simpler operations, one after
the other:

1. Transpose the matrix.
2. Reverse each row of the transposed matrix.

Let's walk through this with an example:
[[1,2,3],[4,5,6],[7,8,9]]

---

Step 1: Transpose the Matrix

Transposing means flipping the matrix along its
main diagonal (the one from top-left to
bottom-right). In simple terms, the element at
(row, column) swaps places with the element at
(column, row).

* The first row [1, 2, 3] becomes the first column.
* The second row [4, 5, 6] becomes the second column.
* The third row [7, 8, 9] becomes the third column.

1 Original Matrix          After Transposing
2 +-------+                +-------+
3 | 1 2 3 |                | 1 4 7 |
4 | 4 5 6 |      -->       | 2 5 8 |
5 | 7 8 9 |                | 3 6 9 |
6 +-------+                +-------+
This operation can be done in-place by just swapping
the elements in the upper triangle of the matrix with
their counterparts in the lower triangle.

---

Step 2: Reverse Each Row

Now, take the matrix you got from Step 1 and simply
reverse each individual row.

* The first row [1, 4, 7] becomes [7, 4, 1].
* The second row [2, 5, 8] becomes [8, 5, 2].
* The third row [3, 6, 9] becomes [9, 6, 3].

1 Transposed Matrix        After Reversing Each Row
2 +-------+                +-------+
3 | 1 4 7 |                | 7 4 1 |
4 | 2 5 8 |      -->       | 8 5 2 |
5 | 3 6 9 |                | 9 6 3 |
6 +-------+                +-------+

This final matrix is the correctly rotated result.
Reversing each row is also a simple in-place
operation using two pointers per row.

By breaking the complex problem of "rotation" into
two much simpler, well-known operations ("transpose"
and "reverse"), the in-place solution becomes much
easier to visualize and implement.
'''


def rotate_image(matrix: List[List[int]]) -> List[List[int]]:
    # transpose the matrix
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if column >= row:
                matrix[row][column], matrix[column][row]\
                    = matrix[column][row], matrix[row][column]
            else:
                continue
    # reverse the rows:
    for row in range(len(matrix)):
        matrix[row].reverse()
    return matrix


def tests():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = rotate_image(matrix)
    print(f"result for matrix {matrix} is {res}")
    assert res == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10],
              [13, 3, 6, 7], [15, 14, 12, 16]]
    res = rotate_image(matrix)
    print(f"result for matrix {matrix} is {res}")
    assert res == [[15, 13, 2, 5], [14, 3, 4, 1],
                   [12, 6, 8, 9], [16, 7, 10, 11]]


tests()
