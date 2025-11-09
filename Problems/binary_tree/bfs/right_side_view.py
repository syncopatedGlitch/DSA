from collections import deque
from typing import Optional, List
'''
Given the root of a binary tree, imagine yourself
standing on the right side of it, return the values
of the nodes you can see ordered from top to bottom.


Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:

Input: root = [1,null,3]
Output: [1,3]

Example 4:

Input: root = []
Output: []
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


def tests():
    sol = Solution()
    null = None

    # Example 1
    root1_list = [1, 2, 3, null, 5, null, 4]
    root1 = build_tree(root1_list)
    result1 = sol.rightSideView(root1)
    expected1 = [1, 3, 4]
    assert result1 == expected1
    print("Test Case 1 Passed")

    # Example 2
    root2_list = [1, 2, 3, 4, null, null, null, 5]
    root2 = build_tree(root2_list)
    result2 = sol.rightSideView(root2)
    expected2 = [1, 3, 4, 5]
    assert result2 == expected2
    print("Test Case 2 Passed")

    # Example 3
    root3_list = [1, null, 3]
    root3 = build_tree(root3_list)
    result3 = sol.rightSideView(root3)
    expected3 = [1, 3]
    assert result3 == expected3
    print("Test Case 3 Passed")

    # Example 4
    root4_list = []
    root4 = build_tree(root4_list)
    result4 = sol.rightSideView(root4)
    expected4 = []
    assert result4 == expected4
    print("Test Case 4 Passed")


def build_tree(nodes: list) -> Optional[TreeNode]:
    """
    Helper function to build a tree from a list representation.
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


tests()
