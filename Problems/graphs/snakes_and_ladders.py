from typing import List, Tuple
from collections import deque
'''
You are given an n x n integer matrix board where
the cells are labeled from 1 to n2 in a
Boustrophedon style starting from the bottom left
of the board (i.e. board[n - 1][0]) and alternating
direction each row.

You start on square 1 of the board. In each move,
starting from square curr, do the following:

Choose a destination square next with a label in
the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard
6-sided die roll: i.e., there are always at most
6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the
destination of that snake or ladder. Otherwise, you
move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or
ladder if board[r][c] != -1. The destination of that
snake or ladder is board[r][c]. Squares 1 and n2 are
not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most
once per dice roll. If the destination to a snake or
ladder is the start of another snake or ladder, you
do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]],
and on the first move, your destination square is 2.
You follow the ladder to square 3, but do not follow
the subsequent ladder to 4.
Return the least number of dice rolls required to
reach the square n2. If it is not possible to reach
the square, return -1.

Example 1:

Input: board = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ]
Output: 4
Explanation:
In the beginning, you start at square 1(at row 5, column 0).
You decide to move to square 2 and must take the ladder
to square 15.
You then decide to move to square 17 and must take the
snake to square 13.
You then decide to move to square 14 and must take the
ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the
last square, so return 4.

Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1

Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 are not the starting points
of any snake or ladder.
'''
'''
Key Insight: Shortest Path Problem

Whenever you see "minimum number of moves,", "shortest
path" or "fewest steps" in a problem where all steps
have an equal cost (in this case, each die roll counts
as one move), it's a strong signal to use Breadth-First
Search (BFS).

Think of the game board as a graph:
* Nodes (Vertices): Each square on the board
(from 1 to n*n) is a node.
* Edges: A directed edge exists from square u to square
v if you can move from u to v in a single turn.

BFS is the perfect algorithm for this because it explores
the graph layer by layer. It will find all squares
reachable in 1 move, then all squares reachable in 2 moves,
and so on. The very first time it reaches the destination
square, it is guaranteed to have found the path with the
minimum number of moves.

The BFS Strategy

1. Queue: We'll use a queue to manage the squares to
   visit. We'll store tuples of (square, moves).
2. Visited Set: To avoid getting into cycles (e.g.,
   going down a snake and up a ladder back to where you
   were) and to prevent redundant work, we need to keep
   track of the squares we've already processed. A set
   is perfect for this.

The Algorithm Steps

1. Initialization:
    * Start a queue and add the starting position:
      (square=1, moves=0).
    * Create a visited set and add square 1 to it.

2. Process the Queue:
    * Loop as long as the queue is not empty.
    * In each iteration, dequeue the current state:
      (current_square, current_moves).

3. Explore Next Moves:
    * From current_square, simulate a die roll. Iterate
      through all possible next squares (from
      current_square + 1 to current_square + 6).
    * For each potential next_square:
        * Check for Snakes/Ladders: Look at the board
          at the position of next_square. If it contains
          a snake or a ladder, your actual destination is
          the value on the board. Otherwise, your
          destination is just next_square.
        * Check if Visited: If this actual_destination
          is already in our visited set, we've found a
          path to it that was either shorter or just as short.
          We can ignore it and continue.
        * Enqueue and Mark Visited: If we haven't visited it,
          add the actual_destination to the visited set and
          enqueue the new state:
          (actual_destination, current_moves + 1).

4. Goal and Termination:
    * If at any point the actual_destination is the final
      square (n*n), we have found the shortest path. We can
      immediately return current_moves + 1.
    * If the queue becomes empty and we have not reached
      the final square, it means the destination is
      unreachable. In this case, we return -1.

A Tricky Detail: Board Coordinates

The most common stumbling block is the board's "boustrophedon"
(alternating direction) numbering. A square's number doesn't
map to a simple (row, col) index.

You'll need a helper function that can take a square number
and convert it into the correct (row, col) coordinates so
you can look up its value in the input board. This function
handles the logic of figuring out which row you're on and
whether that row is read left-to-right or right-to-left.

So, the complete intuition is: Use BFS to find the shortest
path, and create a helper function to translate between
square numbers and board coordinates.
'''


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.board = board
        self.n = len(board)
        start_num = 1
        final_num = self.n**2
        moves = 0
        queue = deque([(start_num, moves)])
        visited = {start_num}
        while queue:
            curr, moves = queue.popleft()
            for i in range(curr + 1, min(curr + 6, self.n**2) + 1):
                row, column = self.find_board_position(i)
                destination = self.board[row][column]
                if self.board[row][column] == -1:
                    destination = i
                if destination == final_num:
                    return moves + 1
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))
        return -1

    def find_board_position(self, square_number: int) -> Tuple[int, int]:
        # convert to zero based repreentation for easy computation
        sq_zero = square_number - 1

        # row from the bottom would be remainder for number / column
        row_from_bottom = sq_zero // self.n
        # so row number from top is (n - 1) - row_from_bottom
        # because we are considering row zero indexed
        # hence n - 1
        row = (self.n - 1) - row_from_bottom
        # square_number modulo n would give us the position
        # of the number in the row
        column = sq_zero % self.n
        # since numbers alternate every other row as it is
        # Boustrophedon style, even lines would be left to right
        # and odd would be right to left
        if row_from_bottom % 2 == 0:
            return (row, column)
        else:
            column = (self.n-1) - column
            return (row, column)


def tests():
    sol = Solution()

    # Example 1
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    res1 = sol.snakesAndLadders(board1)
    assert res1 == 4
    print("Test Case 1 passed")

    # Example 2
    board2 = [[-1, -1], [-1, 3]]
    assert sol.snakesAndLadders(board2) == 1
    print("Test Case 2 passed")


if __name__ == "__main__":
    tests()
