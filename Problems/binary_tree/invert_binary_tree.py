from typing import Optional
from collections import deque

"""
Given the root of a binary tree, invert the tree,
and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Helper function to convert a tree back to a list (level-order)."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def tests():
    sol = Solution()
    # Example 1
    root1_list = [4, 2, 7, 1, 3, 6, 9]
    root1 = build_tree(root1_list)
    inverted_root1 = sol.invertTree(root1)
    result1 = tree_to_list(inverted_root1)
    assert result1 == [4, 7, 2, 9, 6, 3, 1]
    print(f"Test Case 1 Passed: Input={root1_list}, Output={result1}")

    # Example 2
    root2_list = [2, 1, 3]
    root2 = build_tree(root2_list)
    inverted_root2 = sol.invertTree(root2)
    result2 = tree_to_list(inverted_root2)
    assert result2 == [2, 3, 1]
    print(f"Test Case 2 Passed: Input={root2_list}, Output={result2}")

    # Example 3
    root3_list = []
    root3 = build_tree(root3_list)
    inverted_root3 = sol.invertTree(root3)
    result3 = tree_to_list(inverted_root3)
    assert result3 == []
    print(f"Test Case 3 Passed: Input={root3_list}, Output={result3}")


tests()
