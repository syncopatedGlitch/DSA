from typing import List
from collections import deque
'''
Given a n * n matrix grid of 0's and 1's only. We want to
represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal
node has exactly four children. Besides, each node has
two attributes:

val: True if the node represents a grid of 1's or False
if the node represents a grid of 0's. Notice that you can
assign the val to True or False when isLeaf is False, and
both are accepted in the answer.
isLeaf: True if the node is a leaf node on the tree or
False if the node has four children.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
We can construct a Quad-Tree from a two-dimensional area
using the following steps:

If the current grid has the same value (i.e all 1's or all
0's) set isLeaf True and set val to the value of the grid
and set the four children to Null and stop.
If the current grid has different values, set isLeaf to
False and set val to any value and divide the current grid
into four sub-grids as shown in the photo.
Recurse for each of the children with the proper sub-grid.

If you want to know more about the Quad-Tree, you can refer
to the wiki.

Quad-Tree format:

You don't need to read this section for solving the problem.
This is only if you want to understand the output format
here. The output represents the serialized format of a
Quad-Tree using level order traversal, where null signifies
a path terminator where no node exists below.

It is very similar to the serialization of the binary tree.
The only difference is that the node is represented as a
list [isLeaf, val].

If the value of isLeaf or val is True we represent it as 1
in the list [isLeaf, val] and if the value of isLeaf or val
is False we represent it as 0.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]

Explanation: The explanation of this example is shown below:
Notice that 0 represents False and 1 represents True in the
photo representing the Quad-Tree.

Example 2:

Input: grid = [
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0],
[1,1,1,1,0,0,0,0]]
Output: [
    [0,1],[1,1],[0,1],[1,1],[1,0],
    null,null,null,null,[1,0],[1,0],
    [1,1],[1,1]]
Explanation: All values in the grid are not the same. We
divide the grid into four sub-grids.
The topLeft, bottomLeft and bottomRight each has the same value.
The topRight have different values so we divide it into 4
sub-grids where each has the same value.

Constraints:

n == grid.length == grid[i].length
n == 2x where 0 <= x <= 6

'''

'''
The Core Problem: Checking the Grid

In your recursive function, you'll be looking at a subgrid
defined by its top-left corner (row, col) and its size.
You need to know if this size x size area is homogeneous
(all the same value).
                                                                                        
* Naive way: Loop from r = row to row + size and c = col
to col + size, checking if all elements are 0 or all are 1.
This takes O(size²) time for each check.
* Efficient way: Calculate the sum of all the 1s in that
  subgrid in O(1) time.
    * If the sum == 0, the subgrid is all 0s.
    * If the sum == size * size, the subgrid is all 1s.
    * Otherwise, the subgrid is mixed, and you must recurse.

The Solution: 2D Prefix Sums

A prefix sum array lets you find the sum of any rectangular
sub-region of a matrix in O(1) time, after an initial O(N²)
setup.

Step 1: Build the Prefix Sum Array

First, you create a new grid, let's call it prefix_sum, that
is one size larger in each dimension than the input grid
(i.e., (N+1) x (N+1)). This helps to avoid index-out-of-bounds
checks.

prefix_sum[r+1][c+1] will store the sum of all elements in
the rectangle from the origin (0, 0) to the corner (r, c)
in the original grid.

You can build it with a single pass over the grid using this
formula:

1 prefix_sum[r+1][c+1] = grid[r][c] + prefix_sum[r][c+1] +
  prefix_sum[r+1][c] - prefix_sum[r][c]

In Plain engligh:
Total Sum = grid[current] + Sum_Above + Sum_Left - Sum_Overlap

Is just a mathematical way of saying:

"To get the total sum for the big rectangle ending at the current
cell, take the sum of the rectangle above it, add the sum of the
rectangle to its left, subtract the overlapping corner you counted
twice, and finally, add the current cell's own value."

This works because to get the sum of the new, larger rectangle,
you take:
1. The sum of the rectangle above it (prefix_sum[r][c+1]).
2. The sum of the rectangle to its left (prefix_sum[r+1][c]).
3. This double-counts the top-left rectangle, so you subtract
   it (prefix_sum[r][c]).
4. Finally, you add the new current cell's value (grid[r][c]).

This entire setup takes O(N²) time, but you only do it once.

Step 2: Query the Sum of a Subgrid in O(1)

Now, with the prefix_sum array, you can get the sum of any
subgrid. Let's say you want the sum of the subgrid with
top-left corner (r1, c1) and bottom-right corner (r2, c2).

The formula is:

1 subgrid_sum = prefix_sum[r2+1][c2+1] - prefix_sum[r1][c2+1]
  - prefix_sum[r2+1][c1] + prefix_sum[r1][c1]

This is the inclusion-exclusion principle at work:
1. prefix_sum[r2+1][c2+1]: Sum of the large rectangle from
   (0,0) to (r2, c2).
2. - prefix_sum[r1][c2+1]: Subtract the part above the subgrid.
3. - prefix_sum[r2+1][c1]: Subtract the part to the left of the
   subgrid.
4. + prefix_sum[r1][c1]: You subtracted the top-left corner twice,
   so add it back once.                                                                              
                                                                                        
This calculation is always just four lookups, making it O(1).

Step 3: Putting It All Together in Recursion

Now, your recursive function, let's call it
build_tree(row, col, size), looks like this:

1. Calculate Subgrid Sum: Use the O(1) query from Step 2 to get
   the sum of the grid starting at (row, col) with dimension
   size x size.

2. Base Case (Leaf Node):
    * If sum == 0, all are zeros. Return new Node(False, True).
    * If sum == size * size, all are ones. Return new
      Node(True, True).

3. Recursive Step (Internal Node):
* If the sum is anything else, the grid is mixed.
* Create an internal node: node = new Node(True, False).
* The size of the children will be half_size = size // 2.
* Recursively call build_tree for the 4 subgrids:
    * node.topLeft = build_tree(row, col, half_size)
    * node.topRight = build_tree(row, col + half_size, half_size)
    * node.bottomLeft = build_tree(row + half_size, col, half_size)
    * node.bottomRight = build_tree(row + half_size, col
      + half_size, half_size)
    * Return the node.
Your main function will first build the prefix sum array and then
kick off the recursion with build_tree(0, 0, N).

This approach is highly efficient. The initial O(N²) setup is paid
for by the massive speedup of making every single recursive check
O(1) instead of O(size²).
'''
'''
How to find the sum of a sub grid using prefix grid:


  1. Original Grid (`grid`)

   1 grid = [

   2   [1, 1, 0, 1],
   3   [1, 1, 0, 0],
   4   [0, 0, 0, 0],
   5   [0, 0, 0, 0]
   6 ]

  2. Prefix Sum Array (`prefix_sum`)

   1 prefix_sum = [
   2   [0, 0, 0, 0, 0],
   3   [0, 1, 2, 2, 3],
   4   [0, 2, 4, 4, 5],
   5   [0, 2, 4, 4, 5],
   6   [0, 2, 4, 4, 5]
   7 ]

  The Goal

  This time, let's find the sum of the 2x2 subgrid in the middle, highlighted below:
                                                                                         ▄
   1 grid = [                                                                            █
                                                                                         █
   2   [1,  1,  0, 1],
   3   [1, |1,  0|, 0],
   4   [0, |0,  0|, 0],
   5   [0,  0,  0, 0]
   6 ]

This subgrid has a top-left corner at (r1, c1) = (1, 1) and a bottom-right corner at
  (r2, c2) = (2, 2).

  Manually, the sum is 1 + 0 + 0 + 0 = 1. Our goal is to get this result using the
  formula.

  The Formula Breakdown

  subgrid_sum = prefix_sum[r2+1][c2+1] - prefix_sum[r2+1][c1] - prefix_sum[r1][c2+1] +
  prefix_sum[r1][c1]

  Plugging in r1=1, c1=1, r2=2, c2=2:

  subgrid_sum = prefix_sum[3][3] - prefix_sum[3][1] - prefix_sum[1][3] + prefix_sum[1][1]

  Let's visualize each term.

  ---

  1. `prefix_sum[3][3]` = 4 (The "Total Area")

  This is the sum of the entire 3x3 rectangle from (0,0) to our subgrid's bottom-right
  corner (2,2).

   1 [ [1, 1, 0],  -> Sum = 2
   2   [1, 1, 0],  -> Sum = 2
   3   [0, 0, 0] ] -> Sum = 0
   4 ------------------
   5 Total Sum = 4
  This area contains our target subgrid plus extra regions on the top and left.

  ---

  2. `- prefix_sum[3][1]` = -2 (Subtract the "Left Area")

  Now we cut off the block to the left of our subgrid. The sum of this area is stored in
  prefix_sum[r2+1][c1] = prefix_sum[3][1].

  1 [ [1],  -> Sum = 1
   2   [1],  -> Sum = 1
   3   [0] ] -> Sum = 0
   4 ---------
   5 Total Sum = 2
  After this step, our running total is 4 - 2 = 2.

  ---

  3. `- prefix_sum[1][3]` = -2 (Subtract the "Top Area")

  This is where your question about point 3 becomes clear. We now cut off the block above
  our subgrid. The sum of this area is stored in prefix_sum[r1][c2+1] = prefix_sum[1][3].

   1 [ [1, 1, 0] ] -> Sum = 2
   2 ---------------
   3 Total Sum = 2
  Our running total is now 2 - 2 = 0.

  Wait a minute! The sum is 0, but we know the answer is 1. What went wrong? This brings
  us to the most important step.

  ---

  4. `+ prefix_sum[1][1]` = +1 (Add Back the "Overlap Area")

  Look at the two areas we subtracted:

   * The "Left Area" was the first column.
   * The "Top Area" was the first row.

  The cell at (0,0) was part of both of those areas. We subtracted it when we removed the
  "Left Area," and we subtracted it again when we removed the "Top Area." We've
  subtracted it one too many times!

  To fix this, we must add the value of that overlapping region back. The sum of this
  overlapping top-left corner is stored in prefix_sum[r1][c1] = prefix_sum[1][1].

   1 [ [1] ] -> Sum = 1                                                                  ▄
   2 ---------                                                                           █
   3 Total Sum = 1                                                                       █
  Our running total was 0. Now we add this back: 0 + 1 = 1.
'''


# Definition for a QuadTree node.
class Node:
    def __init__(
            self, val, isLeaf,
            topLeft=None,
            topRight=None,
            bottomLeft=None,
            bottomRight=None
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        if not grid:
            return None
        self.grid = grid
        n = len(grid)
        self.prefix_sum = [[0] * (n+1) for _ in range(n + 1)]

        for r in range(n):
            for c in range(n):
                self.prefix_sum[r+1][c+1] = grid[r][c]\
                                        + self.prefix_sum[r + 1][c]\
                                        + self.prefix_sum[r][c + 1]\
                                        - self.prefix_sum[r][c]
        result = self.construct_quad_tree(0, 0, n)
        return result

    def construct_quad_tree(self, row, column, size):
        # Calculate Subgrid Sum: Use the O(1) query into prefix_sum
        # matrix to get the sum of the grid.
        # starting at (row, col) with dimension size x size.
        r1, c1 = row, column
        r2, c2 = row + size - 1, column + size - 1
        sum_grid = self.prefix_sum[r2 + 1][c2 + 1]\
                    - self.prefix_sum[r2 + 1][c1]\
                    - self.prefix_sum[r1][c2 + 1]\
                    + self.prefix_sum[r1][c1]
        # if subgrid has all 1's, sum would be size squared
        if sum_grid == size**2:
            leaf_node = Node(val=True, isLeaf=True)
            return leaf_node
        elif sum_grid == 0:
            leaf_node = Node(val=False, isLeaf=True)
            return leaf_node
        else:
            # This is the "parent" for the next level down.
            # Create an internal node for this level.
            node = Node(val=False, isLeaf=False)
            half_size = size // 2
            # Make the recursive calls AND ASSIGN THE RETURNED NODES
            # The connection to parent node happens here
            node.topLeft = self.construct_quad_tree(
                row, column, half_size
            )
            node.topRight = self.construct_quad_tree(
                row, column + half_size, half_size)
            node.bottomLeft = self.construct_quad_tree(
                row + half_size, column, half_size
            )
            node.bottomRight = self.construct_quad_tree(
                row + half_size,
                column + half_size,
                half_size
            )
            return node


def serialize_quad_tree(root: 'Node') -> List:
    """
    Serializes a Quad-Tree into a list using level-order traversal,
    matching the format used in the problem description.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    # Continue as long as there is at least one non-None node in the queue
    while any(node is not None for node in queue):
        node = queue.popleft()

        if node:
            result.append([1 if node.isLeaf else 0, 1 if node.val else 0])
            # Always add children; for a leaf, its children are None.
            queue.append(node.topLeft)
            queue.append(node.topRight)
            queue.append(node.bottomLeft)
            queue.append(node.bottomRight)
        else:
            # This represents a terminated path from a parent's child
            result.append(None)

    # Trim trailing nulls for a clean comparison
    while result and result[-1] is None:
        result.pop()

    return result


def tests():
    sol = Solution()

    # Example 1
    grid1 = [[0, 1], [1, 0]]
    result1 = sol.construct(grid1)
    serialized_result1 = serialize_quad_tree(result1)
    # The `val` of an internal node can be True or False. We must accept both.
    expected1_val_true = [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
    expected1_val_false = [[0, 0], [1, 0], [1, 1], [1, 1], [1, 0]]
    assert serialized_result1 in [expected1_val_true, expected1_val_false], "Test Case 1 Failed"
    print("Test Case 1 (grid=[[0,1],[1,0]]) passed.")

    # # Example 2
    # grid2 = [
    #     [1, 1, 1, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 0, 0, 0, 0]
    # ]
    # result2 = sol.construct(grid2)
    # serialized_result2 = serialize_quad_tree(result2)
    # # The `val` of an internal node can be True or False. We must accept both.
    # expected2_val_true = [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
    # expected2_val_false = [[0, 0], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
    # assert serialized_result2 in [expected2_val_true, expected2_val_false], "Test Case 2 Failed"
    # print("Test Case 2 passed.")


if __name__ == "__main__":
    tests()
