from typing import List
from collections import deque

"""
You are given an m x n matrix board containing letters
'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells
        horizontally or vertically.
Region: To form a region connect every 'O' cell.

Surround: The region is surrounded with 'X' cells if
you can connect the region with 'X' cells and none of
the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with
'X's in-place within the original board. You do not
need to return anything.

Example 1:

Input: board = [
                    ["X","X","X","X"],
                    ["X","O","O","X"],
                    ["X","X","O","X"],
                    ["X","O","X","X"]
               ]
Output: [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]

Explanation:
In the above diagram, the bottom region is not
captured because it is on the edge of the board
and cannot be surrounded.

Example 2:

Input: board = [["X"]]
Output: [["X"]]
"""


class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        # scan the edges and find any zeros there
        # once edges are scanned and if zeros are found
        # find all the connected zeros to those edge zeros
        # to find the safe connections
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])
        if self.rows == 1:
            return
        for i in range(self.columns):
            if self.board[0][i] == "O":
                self.find_edge_connected_zeros(row=0, column=i)
            if self.board[self.rows - 1][i] == "O":
                self.find_edge_connected_zeros(row=self.rows - 1, column=i)
        for k in range(1, self.rows - 1):
            if self.board[k][0] == "O":
                self.find_edge_connected_zeros(row=k, column=0)
            if self.board[k][self.columns - 1] == "O":
                self.find_edge_connected_zeros(row=k, column=self.columns - 1)
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column] == "S":
                    self.board[row][column] = "O"
                elif self.board[row][column] == "O":
                    self.board[row][column] = "X"
        return self.board

    def find_edge_connected_zeros(self, row, column):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(row, column)])
        self.board[row][column] = "S"
        while queue:
            row, column = queue.popleft()
            for ra, ca in directions:
                new_row = row + ra
                new_column = column + ca
                if (
                    0 <= new_row < self.rows
                    and 0 <= new_column < self.columns
                    and self.board[new_row][new_column] == "O"
                ):
                    self.board[new_row][new_column] = "S"
                    queue.append((new_row, new_column))


def tests():
    sol = Solution()

    # Example 1
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    expected1 = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]
    result = sol.solve(board1)
    assert result == expected1
    print("Test Case 1 Passed")

    # Example 2
    board2 = [["X"]]
    expected2 = [["X"]]
    sol.solve(board2)
    assert board2 == expected2
    print("Test Case 2 Passed")

    # Example 3
    board3 = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
    expected3 = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
    result3 = sol.solve(board3)
    print(f"board3 is {result3}")
    assert result3 == expected3
    print("Test Case 3 Passed")

    # Example 4
    board4 = [
        ["X", "O", "X", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "X"],
        ["X", "O", "X", "O", "X", "O"],
        ["O", "X", "O", "X", "O", "X"],
    ]
    expected4 = [
        ["X", "O", "X", "O", "X", "O"],
        ["O", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "X", "X", "O"],
        ["O", "X", "O", "X", "O", "X"],
    ]
    result4 = sol.solve(board4)
    print(f"board4 is {result4}")
    assert board4 == expected4


tests()
