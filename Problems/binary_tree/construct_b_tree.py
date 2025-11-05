from typing import List, Optional
from collections import deque

"""
Given two integer arrays preorder and inorder
where preorder is the preorder traversal of a
binary tree and inorder is the inorder
traversal of the same tree, construct and
return the binary tree.

Example 1:

Input: preorder = [3,9,20,15,7],
       inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
            self, inorder: List[int], preorder: List[int]
            ) -> Optional[TreeNode]:
        # base case
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        subtree_size = root_index
        # create slices for left subtree
        preorder_left = preorder[1: 1 + subtree_size]
        inorder_left = inorder[:root_index]
        left = self.buildTree(inorder_left, preorder_left)
        # slices for right subtree
        preorder_right = preorder[1 + subtree_size:]
        inorder_right = inorder[root_index + 1:]
        right = self.buildTree(inorder_right, preorder_right)
        root.left = left
        root.right = right
        return root

    def build_tree_optimised(
            self, inorder: List[int], preorder: List[int]
            ) -> Optional[TreeNode]:
        self.inorder_map = {
            node: index for index, node in enumerate(inorder)
        }
        self.inorder = inorder
        self.preorder = preorder
        self.preorder_index = 0
        root = self.build(0, len(inorder) - 1)
        return root

    def build(self, left, right):
        if self.preorder_index > len(self.preorder) - 1:
            return None
        if left > right:
            return None
        root_val = self.preorder[self.preorder_index]
        self.preorder_index += 1
        root = TreeNode(root_val)
        inorder_index = self.inorder_map[root_val]
        # we must build the left subtree first,
        # because the left nodes come first in preorder
        # traversal before right
        left = self.build(left, inorder_index - 1)
        right = self.build(inorder_index + 1, right)
        root.left = left
        root.right = right
        return root


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Helper function to convert a tree back to a list for assertion."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
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
    inorder1 = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]
    expected1 = [3, 9, 20, null, null, 15, 7]
    result_tree1 = sol.build_tree_optimised(inorder1, preorder)
    result_list1 = tree_to_list(result_tree1)
    assert result_list1 == expected1
    print(f"Test Case 1 Passed: Output={result_list1}")

    # Example 2
    inorder2 = [-1]
    preorder = [-1]
    expected2 = [-1]
    result_tree2 = sol.build_tree_optimised(inorder2, preorder)
    result_list2 = tree_to_list(result_tree2)
    assert result_list2 == expected2
    print(f"Test Case 2 Passed: Output={result_list2}")


tests()
