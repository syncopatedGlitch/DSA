'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

Example 1:

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
'''

'''
Here's the intuition for an in-place approach:

  The problem is that when you update a cell, you "erase" its original state, which is
  needed to correctly calculate the fate of its neighbors.

  The solution is to not erase it. Instead, we can encode both the original state and
  the next state into a single cell on the board. We can achieve this by using new,
  temporary state values that represent a transition.

  Think of it as a two-pass process:

  Pass 1: Mark the Cells for Their Future State

   1. Iterate through every cell on the board, just as you would normally.
   2. For each cell, count its live neighbors. The crucial part here is how you count.
      Since you might be overwriting cells as you go, you need a rule to determine a
      neighbor's original state.
   3. Instead of immediately changing a cell to 0 or 1, you update it to a special,
      intermediate state. For example:
       * If a live cell (1) is supposed to die, change its value to a new state, let's
         say -1. This tells us, "This cell was 1, but it will be 0."
       * If a dead cell (0) is supposed to become live, change its value to another new
         state, like 2. This tells us, "This cell was 0, but it will be 1."

  Now, when you are counting the neighbors for any given cell, you can correctly deduce
   their original state. If a neighbor's value is 1 (it was live and will stay live) or
   -1 (it was live and will die), you count it as a live neighbor. Otherwise, its
  original state was dead.

  Pass 2: Finalize the Board

  After you have iterated through the entire board and marked all the changes using
  these new states, the first pass is complete. The board is now a mix of 0, 1, -1, and
   2.

  Now, you simply iterate through the board one more time to clean up and set the final
   states:

   * Any cell with a value of -1 (was live, now dead) becomes 0.
   * Any cell with a value of 2 (was dead, now live) becomes 1.

  This method allows you to perform all your calculations based on the original states
  while modifying the board in-place, because you never truly lose the original
  information until after all calculations are done.
'''

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        State Management:
        1. if a dead cell (0) is to become alive, value would be
            updated to 2.
        2. if a live cell (1) is supposed to die, value would be
            updated to -1
        """
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])
        # update the state
        for row in range(self.rows):
            for column in range(self.columns):
                cell = board[row][column]
                count = self.neighbour_count(row, column)
                if cell == 0 and count[1] == 3:
                    board[row][column] = 2
                elif cell == 1:
                    if count[1] > 3 or count[1] < 2:
                        board[row][column] = -1
        print(f"board after state updates is {self.board}")
        # change to correct values
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column] == -1:
                    self.board[row][column] = 0
                elif self.board[row][column] == 2:
                    self.board[row][column] = 1
        return board

    # returns count for 1 and 0 in a dict
    # from the entire neighbour set
    def neighbour_count(self, row, column) -> dict:
        neighbours = [(-1, -1), (-1 ,0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        count = {1: 0, 0: 0 }
        for neighbour in neighbours:
            _r, _c = neighbour
            if 0 <= row + _r < self.rows and 0 <= column + _c < self.columns:
                val = self.board[row + _r][column + _c]
                if val == 1 or val == -1:
                    count[1] = count.get(1) + 1
                else:
                    count[0] = count.get(0) + 1
        return count


def tests():
    c = Solution()
    board = [[0, 1, 0],[0,0,1],[1,1,1],[0,0,0]]
    res = c.gameOfLife(board)
    print(f"res is {res}")
    assert res == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    board = [[1,1],[1,0]]
    res = c.gameOfLife(board)
    assert res == [[1,1],[1,1]]


tests()
