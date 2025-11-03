from typing import Optional
from collections import deque

"""
Given the root of a binary tree,
return its maximum depth.

A binary tree's maximum depth is the number of
nodes along the longest path from the root node
down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # store (node, depth) tuple in the stack
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     left_height = self.maxDepth(root.left)
    #     right_height = self.maxDepth(root.right)

    #     return 1 + max(left_height, right_height)


def build_tree(nodes: list) -> Optional[TreeNode]:
    """Helper function to build a tree from a list representation."""
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        current_node = queue.popleft()

        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1

        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1

    return root


def tests():
    sol = Solution()
    null = None  # To make the input list readable

    # Test Case 1
    root1_list = [3, 9, 20, null, null, 15, 7]
    root1 = build_tree(root1_list)
    assert sol.maxDepth(root1) == 3
    print(f"Test Case 1 Passed: Input={root1_list}, Output=3")

    # Test Case 2
    root2_list = [1, null, 2]
    root2 = build_tree(root2_list)
    assert sol.maxDepth(root2) == 2
    print(f"Test Case 2 Passed: Input={root2_list}, Output=2")


tests()
