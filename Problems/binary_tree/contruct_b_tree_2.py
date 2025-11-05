from typing import List, Optional
from collections import deque

"""
Given two integer arrays inorder and postorder
where inorder is the inorder traversal of a
binary tree and postorder is the postorder
traversal of the same tree, construct and
return the binary tree.

Example 1:

Input: inorder = [9,3,15,20,7]
       postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(
            self, inorder: List[int], postorder: List[int]
            ) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        inorder_root_index = inorder.index(root_val)
        # slice to create left subtree
        postorder_left = postorder[0: inorder_root_index]
        inorder_left = inorder[0: inorder_root_index]
        left = self.build_tree(inorder_left, postorder_left)
        # slice to create right subtree
        postorder_right = postorder[inorder_root_index: -1]
        inorder_right = inorder[inorder_root_index + 1:]
        right = self.build_tree(inorder_right, postorder_right)
        root.left, root.right = left, right
        return root

    def build_tree_optimised(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        self.inorder_map = {
            node: index for index, node in enumerate(inorder)
        }
        self.postorder = postorder
        self.inorder = inorder
        self.postorder_root_index = len(postorder) - 1
        root = self._build(0, len(inorder) - 1)
        return root

    def _build(self, left, right):
        if left > right:
            return None
        root_val = self.postorder[self.postorder_root_index]
        self.postorder_root_index -= 1
        root = TreeNode(root_val)
        inorder_index = self.inorder_map[root_val]
        # build right subtree first as its postorder so
        # right subtree comes before left going from right to left
        # in the postorder array
        right = self._build(inorder_index + 1, right)
        # build left subtree
        left = self._build(left, inorder_index - 1)
        root.left, root.right = left, right
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
    null = None
    c = Solution()

    # Example 1
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    expected1 = [3, 9, 20, null, null, 15, 7]
    result_tree1 = c.build_tree_optimised(inorder1, postorder1)
    result_list1 = tree_to_list(result_tree1)
    assert result_list1 == expected1
    print(f"Test Case 1 Passed: Output={result_list1}")

    # Example 2
    inorder2 = [-1]
    postorder2 = [-1]
    expected2 = [-1]
    result_tree2 = c.build_tree_optimised(inorder2, postorder2)
    result_list2 = tree_to_list(result_tree2)
    assert result_list2 == expected2
    print(f"Test Case 2 Passed: Output={result_list2}")


tests()
