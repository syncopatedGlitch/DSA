from typing import List
'''
Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9
without repetition.
Each of the nine 3 x 3 sub-boxes of the grid
must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but
is not necessarily solvable.
Only the filled cells need to be validated according
to the mentioned rules.

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5
in the top left corner being modified to 8. Since
there are two 8's in the top left 3x3 sub-box,
it is invalid.
'''

'''
*********  INTUITION BEHIND SOLVING THE PROBLEM   **********
The "Three Notebooks" Analogy

Think of it like having three separate notebooks to
keep track of things:
1. A "Rows" Notebook: It has 9 pages, one for each row.
2. A "Columns" Notebook: It has 9 pages, one for each column.
3. A "Boxes" Notebook: It has 9 pages, one for
   each 3x3 sub-grid.

Now, you iterate through the Sudoku board, from top-left
to bottom-right. Let's say you're at row `r` and column `c`,
and you find a number N.

1. You flip to page r in your "Rows" notebook. Is the number
   N already written on this page?
    * If yes, you shout "Invalid!" and you're done.
    * If no, you write N on that page.

2. You flip to page c in your "Columns" notebook. Is the
   number N already written on this page?
    * If yes, "Invalid!"
    * If no, you write N on that page.

3. You figure out which of the nine 3x3 boxes you're in.
   Let's say it's box `b`. You flip to page b in your
   "Boxes" notebook. Is N on that page?
    * If yes, "Invalid!"
    * If no, you write N on that page.

If you get through the entire board without ever shouting
"Invalid!", it means the board is valid.
'''

'''
********** INTUITION BEHING IDENTIFYING THE SUB-GRID FOR A ROW, COLUMN ***********
How do we arrive at formula:
box_index = (r // 3) * 3 + (c // 3)
Our goal is to assign a unique ID, from 0 to 8,
to each of the nine 3x3 sub-boxes on the board.

Let's visualize the box IDs we want to generate:

1 (row 0, col 0) -> Box 0 | (row 0, col 3) -> Box 1 | (row 0, col 6) -> Box 2
2 -----------------------+-----------------------+-----------------------
3 (row 3, col 0) -> Box 3 | (row 3, col 3) -> Box 4 | (row 3, col 6) -> Box 5
4 -----------------------+-----------------------+-----------------------
5 (row 6, col 0) -> Box 6 | (row 6, col 3) -> Box 7 | (row 6, col 6) -> Box 8

The formula (r // 3) * 3 + (c // 3) is essentially a
coordinate system conversion. It converts a 2D
coordinate (r, c) from the main 9x9 grid into a
1D index (0-8) for the boxes.

Let's break the formula into its two parts.

Part 1: The Grouping Principle (// 3)

The // operator in Python is for integer division.
It divides and then throws away the remainder. This
makes it a perfect tool for grouping things. We have
9 rows and 9 columns that we want to lump
into 3 groups each.

* `r // 3` (The "Box Row"): This tells you which row
   of boxes you are in.
    * If your cell's row r is 0, 1, or 2, then r // 3
      will be 0. (You're in the top row of boxes).
    * If your cell's row r is 3, 4, or 5, then r // 3
      will be 1. (You're in the middle row of boxes).
    * If your cell's row r is 6, 7, or 8, then r // 3
      will be 2. (You're in the bottom row of boxes).

* `c // 3` (The "Box Column"): This tells you which
   column of boxes you are in.
    * If your cell's column c is 0, 1, or 2, then c // 3
      will be 0. (You're in the left column of boxes).
    * If your cell's column c is 3, 4, or 5, then c // 3
      will be 1. (You're in the middle column of boxes).
    * If your cell's column c is 6, 7, or 8, then c // 3
      will be 2. (You're in the right column of boxes).

So, after this step, we have successfully identified the
location of our box in a 3x3 grid. For a cell at
(r, c) = (4, 8), we get (r//3, c//3) = (1, 2), which means
we are in the box at "box row 1" and "box column 2".

Part 2: The 2D-to-1D Conversion (* 3 + ...)

Now we have a 2D coordinate for the box (box_row, box_col)
and we need to convert it to a single number from 0 to 8.
This is a classic programming pattern for converting
a 2D array index into a 1D one.

The general formula is index = row * (number_of_columns) + col.

In our case, we are navigating a 3x3 grid of boxes,
so number_of_columns is 3.

* The (r // 3) * 3 part calculates how many full rows of
  boxes are "above" you. If you're in box row 0, this is
  0. If you're in box row 1, it means you've skipped the
  first 3 boxes (0, 1, 2), so this term is 1 * 3 = 3.
  If you're in box row 2, you've skipped 6 boxes, so this
  term is 2 * 3 = 6.
* The + (c // 3) part then adds the column offset. After
  jumping down to the correct row of boxes, this moves you
  across to the correct box in that row.

Example Walkthrough

Let's take the cell at (r=7, c=5):

1. `r // 3`: 7 // 3 = 2. We are in the bottom row of boxes
   (boxes 6, 7, 8).
2. `c // 3`: 5 // 3 = 1. We are in the middle column of
   boxes (boxes 1, 4, 7).
3. Combine:
    * The (r // 3) * 3 part becomes 2 * 3 = 6. This term makes
      us "jump" past the first two rows of boxes (0-2 and 3-5)
      to the start of the third row, which is Box 6.
    * The + (c // 3) part becomes + 1. This moves us one step
      to the right from Box 6.
    * Result: 6 + 1 = 7.

The cell at (7, 5) is correctly identified as being in Box 7.
'''


def valid_sudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(0, 9)]
    columns = [set() for _ in range(0, 9)]
    grids = [set() for _ in range(0, 9)]
    for row in range(9):
        for column in range(9):
            char = board[row][column]
            if char == ".":
                continue
            # row check
            if char in rows[row]:
                return False
            else:
                rows[row].add(char)
            # column check
            if char in columns[column]:
                return False
            else:
                columns[column].add(char)
            # grid check
            grid_number = (row // 3) * 3 + (column // 3)
            if char in grids[grid_number]:
                return False
            else:
                grids[grid_number].add(char)
    return True


def tests():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    res = valid_sudoku(board)
    assert res is True
    print("Executing 2nd test case")
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    res = valid_sudoku(board)
    assert res is False


tests()
