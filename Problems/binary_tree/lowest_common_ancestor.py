from collections import deque
from typing import Optional
'''
Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant
of itself).”

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node
can be a descendant of itself according to the LCA
definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode'
    ) -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left or right:
            return left if left else right
        if not left and not right:
            return None


def build_tree(nodes: list) -> Optional[TreeNode]:
    """Helper function to build a tree from a list representation."""
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


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Helper function to find a node with a specific value in the tree."""
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


def tests():
    sol = Solution()
    null = None

    # Example 1
    root1_list = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    root1 = build_tree(root1_list)
    p1 = find_node(root1, 5)
    q1 = find_node(root1, 1)
    result1 = sol.lowestCommonAncestor(root1, p1, q1)
    print(f"result1 is {result1}")
    assert result1.val == 3
    print("Test Case 1 passed.")

    # Example 2
    # Using the same tree as Example 1
    p2 = find_node(root1, 5)
    q2 = find_node(root1, 4)
    result2 = sol.lowestCommonAncestor(root1, p2, q2)
    assert result2.val == 5
    print("Test Case 2 passed.")

    # Example 3
    root3_list = [1, 2]
    root3 = build_tree(root3_list)
    p3 = find_node(root3, 1)
    q3 = find_node(root3, 2)
    result3 = sol.lowestCommonAncestor(root3, p3, q3)
    assert result3.val == 1
    print("Test Case 3 passed.")

    print("All test cases passed.")


if __name__ == "__main__":
    tests()
