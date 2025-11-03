from typing import Optional
from collections import deque

"""
Given the roots of two binary trees p and q, write a
function to check if they are the same or not.

Two binary trees are considered the same if they are
structurally identical, and the nodes have the
same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the
range [0, 100].
-104 <= Node.val <= 104
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        left_result = self.isSameTree(p.left, q.left)
        right_result = self.isSameTree(p.right, q.right)
        return left_result and right_result


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
    null = None  # To make the input lists readable

    # Example 1
    p1_list = [1, 2, 3]
    q1_list = [1, 2, 3]
    p1 = build_tree(p1_list)
    q1 = build_tree(q1_list)
    res1 = sol.isSameTree(p1, q1)
    assert res1 is True
    print(f"Test Case 1 Passed: p={p1_list}, q={q1_list}, Expected=True")

    # Example 2
    p2_list = [1, 2]
    q2_list = [1, null, 2]
    p2 = build_tree(p2_list)
    q2 = build_tree(q2_list)
    res = sol.isSameTree(p2, q2)
    assert res is False
    print(f"Test Case 2 Passed: p={p2_list}, q={q2_list}, Expected=False")

    # Example 3
    p3_list = [1, 2, 1]
    q3_list = [1, 1, 2]
    p3 = build_tree(p3_list)
    q3 = build_tree(q3_list)
    assert sol.isSameTree(p3, q3) is False
    print(f"Test Case 3 Passed: p={p3_list}, q={q3_list}, Expected=False")


tests()
