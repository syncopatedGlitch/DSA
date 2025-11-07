from typing import Optional
from collections import deque
'''
Given the root of a binary tree, flatten the tree
into a "linked list":

The "linked list" should use the same TreeNode
class where the right child pointer points to the
next node in the list and the left child pointer
is always null.
The "linked list" should be in the same order as
a pre-order traversal of the binary tree.

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

Constraints:
Number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if not node.left:
                if not node.right:
                    break
                node = node.right
                continue
            left = node.left
            predecessor = left
            while predecessor.right:
                predecessor = predecessor.right
            right = node.right
            node.right = left
            predecessor.right = right
            node.left = None
            node = node.right
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
    """
    Helper function to convert a tree to a list using level-order
    traversal, including nulls for empty children. This is needed
    to match the problem's output format.
    """
    if not root:
        return []
    result = []
    queue = deque([root])
    # We need to traverse until we are sure no deeper nodes exist.
    # A simple queue check isn't enough if the tree is sparse.
    # We'll add nodes to the queue and stop when all appended nodes are None.
    while any(queue):
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Trim trailing nulls for clean comparison
    while result and result[-1] is None:
        result.pop()
    return result


def tests():
    sol = Solution()
    null = None

    # Example 1
    root1_list = [1, 2, 5, 3, 4, null, 6]
    root1 = build_tree(root1_list)
    sol.flatten(root1)
    result1 = tree_to_list(root1)
    print(f"result1 is {result1}")
    expected1 = [1, null, 2, null, 3, null, 4, null, 5, null, 6]
    assert result1 == expected1
    print(f"Test 1 Failed: Expected {expected1}, Got {result1}")
    print("Test Case 1 Passed")

    # Example 2
    root2 = build_tree([])
    sol.flatten(root2)
    assert tree_to_list(root2) == [], "Test 2 Failed"
    print("Test Case 2 Passed")

    # Example 3
    root3 = build_tree([0])
    sol.flatten(root3)
    assert tree_to_list(root3) == [0], "Test 3 Failed"
    print("Test Case 3 Passed")


tests()
