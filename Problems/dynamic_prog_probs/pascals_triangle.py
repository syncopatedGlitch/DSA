'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly
above it

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
'''
from typing import List


def pascals_triangle(num_rows: int) -> List[list]:
    triangle = []
    if num_rows <= 0:
        return []
    # start from the root node that we know is 1.
    triangle.append([1])
    for i in range(1, num_rows):
        current_row = [1]
        prev_row = triangle[i - 1]
        # number of elements you need to compute for each row.
        # Ex. for row 2 (index 1), we need to compute 1 element
        # for row 3 (index 2), we need to compute 2 elements
        # for row 4 (index 3). we need to compute 3 elements
        # j = i - 1
        # while j > 0:
        #     element = prev_row[j - 1] + prev_row[j]
        #     current_row.append(element)
        #     j -= 1
        # current_row.append(1)
        # triangle.append(current_row)
        # loop forward approach
        elements_to_find = len(prev_row) - 1
        for k in range(0, elements_to_find):
            element = prev_row[k] + prev_row[k + 1]
            current_row.append(element)
        current_row.append(1)
        triangle.append(current_row)
    return triangle


def tests():
    num_rows = 5
    res = pascals_triangle(num_rows)
    print(f"pascals triangle for {num_rows} rows is {res}")
    assert res == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    num_rows = 1
    res = pascals_triangle(num_rows)
    print(f"pascals triangle for {num_rows} rows is {res}")
    assert res == [[1]]
    num_rows = 0
    res = pascals_triangle(num_rows)
    print(f"pascals triangle for {num_rows} rows is {res}")
    assert res == []


tests()
