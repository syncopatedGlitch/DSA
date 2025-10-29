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
