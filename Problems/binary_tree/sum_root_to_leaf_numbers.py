from typing import Optional
from collections import deque
'''
You are given the root of a binary tree containing
digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a
number.

For example, the root-to-leaf path 1 -> 2 -> 3
represents the number 123.
Return the total sum of all root-to-leaf numbers.
Test cases are generated so that the answer will
fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        node = root
        result = self.find_sum(node, 0)
        return result

    def find_sum(self, node, number_so_far):
        number_so_far = (number_so_far * 10) + node.val
        if node.left:
            left_sum = self.find_sum(node.left, number_so_far)
        if node.right:
            right_sum = self.find_sum(node.right, number_so_far)
        if not node.right and not node.left:
            return number_so_far
        return left_sum + right_sum


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

    # Example 1
    root1_list = [1, 2, 3]
    root1 = build_tree(root1_list)
    res1 = sol.sumNumbers(root1)
    print(f"result of 1st test case is {res1}")
    assert res1 == 25, "Test Case 1 Failed"

    # Example 2
    root2_list = [4, 9, 0, 5, 1]
    root2 = build_tree(root2_list)
    assert sol.sumNumbers(root2) == 1026, "Test Case 2 Failed"


tests()
