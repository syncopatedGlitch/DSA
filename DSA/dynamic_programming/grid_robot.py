'''
The Problem:
A robot starts at the top-left corner of an m x n grid. The robot can only
move right or down. How many unique paths are there for the robot to travel
from the top-left corner to the bottom-right corner?

Example:
For a 3 x 2 grid, there are 3 unique paths:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Thinking Through the Problem

1. Identify DP Properties:
* Goal: Find the number of paths to the cell (m-1, n-1).

* Choices: To arrive at any cell (row, col), where could the robot have come
from? Since it can only move right or down, it must have come from the cell
directly above, (row-1, col), or the cell directly to the left, (row, col-1).

* Optimal Substructure: The total number of unique paths to (row, col) is the
sum of the unique paths to the cell above it and the unique paths to the cell
to its left.
paths(row, col) = paths(row-1, col) + paths(row, col-1)

* Overlapping Subproblems: This recurrence will naturally result in
re-calculating the paths to the same cells multiple times, making it a perfect
fit for DP.
'''


def robot_grid(rows, cols):
    # only 1 way to reach all cells in row 1, by going right
    # so initialize all columns on start_row to 1
    prev_row = [1] * cols
    # start iterating from the second row, index 1
    for i in range(1, rows):
        # first column in each row will have value 1 since
        # there is only 1 way to reach all cells in 1st column
        # by going down
        current_row = [1] * cols
        # itreate from the second column
        for j in range(1, cols):
            # apply the sum as mentioned in intuition
            # path to reach every cell in current row would be the sum of
            # number of paths leading to the cell above it i.e in prev_row
            # and the cell to its left
            current_row[j] = prev_row[j] + current_row[j-1]
        prev_row = current_row
    # answer is the last element in the last calculated row
    return prev_row[-1]


def tests():
    m = 3
    n = 2
    res = robot_grid(m, n)
    print(f"Output for a {m} X {n} grid is {res}")
    assert res == 3
    m = 3
    n = 7
    res = robot_grid(m, n)
    print(f"Output for a {m} X {n} grid is {res}")
    assert res == 28
    m = 1
    n = 1
    res = robot_grid(m, n)
    print(f"Output for a {m} X {n} grid is {res}")
    assert res == 1
    m = 2
    n = 2
    res = robot_grid(m, n)
    print(f"Output for a {m} X {n} grid is {res}")
    assert res == 2


tests()
