from collections import deque
from typing import List
'''
Given an m x n 2D binary grid grid which represents
a map of '1's (land) and '0's (water), return the
number of islands.

An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
'''
The Core Idea: Scan and Explore

1. Scan the Map: You'll start at the top-left corner of
   the grid and scan through it, cell by cell, looking for
   land.

2. Find a New Island: The very first time you encounter a
   '1' (a piece of land), you know you've discovered the
   shoreline of an island. Since you haven't seen it before,
    you can say, "Okay, that's one island." So, you
    increment your island counter.

3. Explore and "Sink" the Island: Now, here's the crucial
   part. This piece of land might be a tiny island all by
   itself, or it could be part of a huge continent. Before
   you continue your scan, you need to find all the
   connected land squares that belong to this same island.

    Why? To make sure you don't count them again. If you just
    continued scanning, you'd hit the next piece of connected
    land and mistakenly call it a "new" island.

    So, once you find the first piece of a new island, you
    begin an exploration process from that point. You find
    all its adjacent land neighbors, then their neighbors,
    and so on, until you have mapped out the entire landmass.
    As you visit each piece of land belonging to this island,
    you need a way to mark it as "visited." A simple and
    effective way to do this is to change its value from
    `'1'` to `'0'`. You can think of this as "sinking" the
    island after you've counted it.

4. Continue Scanning: Once the entire island has been explored
   and "sunk," you return to your main scan. You continue from
   where you left off, looking for the next '1'.

5. Repeat: If you find another '1', it must belong to a
   completely new island, because if it were connected to the
   previous one, you would have already explored and sunk
   it. So, you increment your island counter again, explore
   and sink this new island, and continue.

You repeat this process until you've scanned the entire grid.

From Intuition to Algorithm

This "exploration" strategy is a classic graph traversal
algorithm. The two most common methods to implement it are:

* Depth-First Search (DFS): This is like exploring a cave
  system. You go as deep as you can down one path, and when
  you hit a dead end, you backtrack and try another path.
  It's often implemented with a simple recursive function.

* Breadth-First Search (BFS): This is like the ripples
  spreading out from a stone dropped in water. You explore
  all the immediate neighbors first, then their neighbors,
  and so on, layer by layer. It's usually implemented with
  a queue.

Both methods work perfectly for this problem.
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.grid = grid
        for row in range(self.rows):
            for column in range(self.columns):
                if grid[row][column] == "1":
                    num_islands += 1
                    self.explore_and_sink_island(row, column)
        return num_islands

    def explore_and_sink_island(self, row, column):
        directions = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]
        queue = deque([(row, column)])
        self.grid[row][column] = "0"
        while queue:
            row, column = queue.popleft()
            for ra, ca in directions:
                new_row = row + ra
                new_column = column + ca
                if new_row < self.rows\
                    and new_column < self.columns\
                        and self.grid[new_row][new_column] == "1":
                    queue.append((new_row, new_column))
                    self.grid[new_row][new_column] = "0"


def tests():
    sol = Solution()

    # Example 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    res1 = sol.numIslands(grid1)
    print(f"result 1 is {res1}")
    assert res1 == 1
    print("Test Case 1 Passed")

    # Example 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert sol.numIslands(grid2) == 3
    print("Test Case 2 Passed")


tests()
