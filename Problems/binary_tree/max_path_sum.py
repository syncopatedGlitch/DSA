from typing import Optional
from collections import deque
'''
A path in a binary tree is a sequence of nodes where
each pair of adjacent nodes in the sequence has an
edge connecting them. A node can only appear in the
sequence at most once. Note that the path does not
need to pass through the root.

The path sum of a path is the sum of the node's values
in the path.

Given the root of a binary tree, return the maximum
path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3
with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7
with a path sum of 15 + 20 + 7 = 42.
'''
'''
Imagine a recursive function that you call on each node.
For any given node, what information do we need to
compute? And what information do we need to pass up to
its parent?

1. Information to Pass Up: A parent node can only extend
   a path that comes from one of its children's subtrees.
   It can't use a path that involves both the left and
   right children of a node below it (because that would
   mean visiting the child node twice). So, for any node,
   we need to calculate the maximum possible path sum that
   starts at that node and goes straight down into only one
   of its subtrees. This is the value we return to the
   parent.

2. Information to Decide the Overall Max: The maximum path
   in the entire tree might actually "turn" at the current
   node, using its left child, the node itself, and its
   right child. This path cannot be extended upwards to the
   parent. So, at each node, we also calculate this
   "turning" path's sum. We don't return this value, but
   we compare it against a global maximum we're tracking,
   updating it if we've found a new best path.

So, the intuition is to use a depth-first search (DFS)
that, for each node:
* First, recursively finds the best "straight-down" path
  sums from its left and right children. (A small but
  crucial detail: if a child's path sum is negative, we
  should ignore it, as we're better off not including
  that path at all).
* Then, it uses these values to see if a new overall
  maximum path can be formed by "turning" at the current
  node.
* Finally, it returns the best "straight-down" path sum
  for itself up to its caller.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")

        def max_sum(node):
            # find the max sum for left and right subtrees
            if not node:
                return 0
            left_sum = max_sum(node.left)
            right_sum = max_sum(node.right)
            if left_sum < 0:
                left_sum = 0
            if right_sum < 0:
                right_sum = 0
            self.max = max(self.max, left_sum + node.val + right_sum)
            return node.val + max(left_sum, right_sum)
        max_sum(root)
        return self.max


def build_tree(nodes: list) -> Optional[TreeNode]:
    """
    Helper function to build a tree from
    a list representation.
    """
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        current_node = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root


def tests():
    sol = Solution()
    null = None

    # Example 1
    root1_list = [1, 2, 3]
    root1 = build_tree(root1_list)
    res1 = sol.maxPathSum(root1)
    print(f"Result for test case 1: {res1}")
    assert res1 == 6, f"Test Case 1 Failed: Expected 6, got {res1}"
    print("Test Case 1 Passed.")

    # Example 2
    # Re-instantiate Solution to reset the result for the next test
    sol = Solution()
    root2_list = [-10, 9, 20, null, null, 15, 7]
    root2 = build_tree(root2_list)
    res2 = sol.maxPathSum(root2)
    print(f"Result for test case 2: {res2}")
    assert res2 == 42, f"Test Case 2 Failed: Expected 42, got {res2}"
    print("Test Case 2 Passed.")


tests()
