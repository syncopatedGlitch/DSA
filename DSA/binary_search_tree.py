"""Binary Search Tree (BST) Implementation

This module implements a Binary Search Tree, a hierarchical data structure that maintains
sorted data and allows efficient searching, insertion, and deletion operations.

Binary Search Tree Properties:
1. Each node has at most two children (left and right)
2. For any node N:
   - All values in the left subtree are less than N's value
   - All values in the right subtree are greater than N's value
3. Both left and right subtrees are also binary search trees (recursive property)

Tree Traversal Methods:
- Pre-order: Root → Left → Right (useful for copying/serializing tree)
- In-order: Left → Root → Right (produces sorted sequence)
- Post-order: Left → Right → Root (useful for deletion/cleanup)
- Level-order: Breadth-first traversal using queue

Key Operations:
- Insert: Add new nodes while maintaining BST property
- Search: Find nodes efficiently using BST property
- Delete: Remove nodes with three cases (leaf, one child, two children)
- Traversals: Multiple ways to visit all nodes
- Min/Max: Find minimum/maximum values efficiently

Time Complexities:
- Average Case: O(log n) for search, insert, delete
- Worst Case: O(n) when tree becomes skewed (like a linked list)
- Best Case: O(log n) when tree is balanced
- Space Complexity: O(n) for storage, O(h) for recursion where h is height

Implementation Features:
- Parent pointers for efficient navigation
- Support for duplicate handling
- Multiple traversal implementations
- Iterative and recursive approaches

Applications:
- Maintaining sorted data with dynamic insertions/deletions
- Database indexing
- Expression parsing
- File system organization
- Priority queues (when balanced)
"""

'''
Pre-order: Root -> Left -> Right
In-order: Left -> Root -> Right
Post-order: Left -> Right -> Root

'''
from collections import deque


class Node:
    ''' Represents the node of a binary search tree'''
    def __init__(self, val, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = val


class BinarySearchTree:
    '''Binary search tree data structure'''
    def __init__(self):
        self.root = None

    def add(self, val):
        '''Add a new node to the binary search tree'''
        # if the tree is empty
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            new_node.parent = None  # parent would be None for root node
            print(f"Added new value {val} as the root of the tree")
            return
        current = self.root
        while True:
            # if the value is lesser, go left
            if val < current.val:
                # if no left node, insert the new value there
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    print(f"Added new value {val} to the left of existing value {current.val}")
                    break
                current = current.left
            # if the value is greater, go right
            elif val > current.val:
                # if no right node, insert the new value there
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    print(f"Added new value {val} to the right of existing value {current.val}")
                    break
                current = current.right
            else:
                # if the value is equal, do nothing
                print(f"Value {val} already exists in the tree. Duplicates not allowed")
                break

    def delete(self, val):
        '''
        Delete a node with given value from a binary tree
        Three types of cases to handle.
        1. Delete a leaf node (easy, just delete it and cut the link with parent)
        2. Delete a Node with only one child (also ok, just link the only child to node's parent)
        3. Delete a Node with 2 children (complex). Approach is:
            a. find the minimum in the node's right subtree, or inorder successor
            (or max in the left subtree, or inorder predecessor)
            b. Copy the min (or max) value found into the node.
            c. Delete the duplicate from right subtree (or left subtree)
        '''
        present, node = self.is_in_tree(val)
        if not present:
            print(f"Value {val} doesn't exist in the tree.")
            return
        # case 1: node to delete is a leaf node
        if not node.left and not node.right:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                # only root node in binary tree
                self.root = None
            print(f"Deleted leaf node {val}")
        # case 2: node to delete has only one child.
        elif not node.left or not node.right:
            # find out the one that is present, left or right
            child = node.left if node.left else node.right
            if node.parent:
                # connect the child to node's parent
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
                    child.parent = node.parent
            else:
                # deleting root node with only one child.
                self.root = child
                child.parent = None
            print(f"Deleted node {val} with only one child")
        # case 3: node to delete has two children
        else:
            # find the in order successor (or the min in the node's right subtree)
            successor = node.right
            while successor.left:
                successor = successor.left
            # copy the value of successor to the node
            successor_val = successor.val
            node.val = successor_val
            # Delete the successor (which has at most one child - right child)
            if successor.parent.left == successor:
                successor.parent.left = successor.right  # successor.right could be None, but thats ok
            else:
                successor.parent.right = successor.right
            # update the parent pointer of successor.right if it exists
            if successor.right:
                successor.right.parent = successor.parent
            print(f"Deleted node {val} with two children, replaced with successor {successor_val}")

    def in_order_traversal(self):
        '''
        Type of DFS
        perform in order traversal to display a sorted list of values from a binary tree.
        Practical application: create a sorted list from a binary tree as
        an input for binary search algorithm.
        In-order: Left -> Root -> Right
        '''
        result = []

        def in_order(node):
            if node:
                # traverse left subtree
                in_order(node.left)
                # print current node value
                # print(node.val, end=' ')
                result.append(node.val)
                # Traverse right subtree
                in_order(node.right)
        if self.root is None:
            print("Tree is empty")
        else:
            in_order(self.root)
            return result

    def pre_order_traversal(self):
        '''
        Type of DFS
        perform pre order traversal to display a list of values from Binary tree
        Practical application: Search for a largest file in a directory.
        We want to process/examine each file as soon as we encounter it,
        then continue searching in subdirectories.

        Traversal Flow:
        1. Check current node (is it a large file?)
        2. If directory, recursively search each child
        3. Process results as we find them
        Pre-order: Root -> Left -> Right
        '''
        result = []

        def pre_order(node):
            if node:
                # print current node value
                # print(node.val, end=' ')
                result.append(node.val)
                # traverse the left subtree
                pre_order(node.left)
                # traverse the right subtree
                pre_order(node.right)
        if self.root is None:
            print("Tree is empty")
        else:
            pre_order(self.root)
            return result

    def post_order_traversal(self):
        '''
        Type of DFS
        Perform post order traversal to display a list of values from a binary tree.
        Practical application: Calculate the size of a given directory.
        We need to calculate children sizes first before we can determine the parent directory's total size.
        Traversal Flow:
        Directory A
        ├── File1.txt (5KB)
        ├── Directory B
        │   ├── File2.txt (10KB)
        │   └── File3.txt (15KB)
        └── File4.txt (20KB)

        Post-Order Processing:
        1. Process File1.txt → return 5KB
        2. Process File2.txt → return 10KB
        3. Process File3.txt → return 15KB
        4. Process Directory B → return 25KB (10KB + 15KB)
        5. Process File4.txt → return 20KB
        6. Process Directory A → return 50KB (5KB + 25KB + 20KB)
        Post-order: Left -> Right -> Root
        '''
        result = []

        def post_order(node):
            if node:
                # traverse the left subtree
                post_order(node.left)
                # traverse the right subtree
                post_order(node.right)
                # print current node value
                # print(node.val, end=' ')
                result.append(node.val)
        if self.root is None:
            print("Tree is empty")
        else:
            post_order(self.root)
            return result

    def level_order_traversal(self):
        '''
        Type of BFS
        perform a level order traversal to display a binary tree level by level.
        Practical applications: #### 1. Social Media - Finding Connections
        BFS explores connections level by level, starting with direct connections (1st degree),
        then their connections (2nd degree), and so on. When LinkedIn shows "You're connected
        to John through 3 mutual connections," it's using BFS to find the shortest chain. The
        algorithm maintains a queue of people to explore and tracks the path
        taken to reach each person, guaranteeing the first path found is the shortest.
        '''

        if self.root is None:
            print("Tree is empty")

        queue = deque([self.root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.val)
            # print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def in_order_trav_iterative(self):
        '''
        perform inorder traversal using explicit stack
        In-order: Left -> Root -> Right
        We must visit the left subtree completely before processing the root, but we need to
        remember the root to come back to it later.
        '''
        if not self.root:
            print("Tree is empty")
            return

        stack = []  # can use array here as we need a stack (LIFO) and append and pop are O(1) operations
        result = []
        current = self.root
        while stack or current:
            # go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            # if no more left children, pop the item from stack and process it
            last = stack.pop()
            result.append(last.val)
            # move to the right subtree
            current = last.right
        return result

    def pre_order_trav_iterative(self):
        '''
        Perform in order traversal with explicit stack management
        Pre-order: Root -> Left -> Right
        We can process a node immediately when we encounter it, then explore its children
        '''
        if not self.root:
            print("Tree is empty")
            return
        stack = [self.root]
        result = []
        while stack:
            # Stack is LIFO. Process the last entry in the stack
            current = stack.pop()
            result.append(current.val)
            # Add right node first and then left, so that left gets processed first.
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

    def post_order_trav_iterative(self):
        '''
        Perform post order traversal using explicit stack
        All the children must be processed before parent is processed
        Post-order: Left -> Right -> Root
        '''
        if not self.root:
            print("Tree is empty")
            return
        stack = []
        result = []
        current = self.root
        last_processed = None
        while stack or current:
            # go to the leftmost node
            if current:
                stack.append(current)
                current = current.left
            else:
                # process nodes from stack
                peek_node = stack[-1]
                # if a right node is present and its not visited, go there
                if peek_node.right and last_processed != peek_node.right:
                    current = peek_node.right
                else:
                    # right subtree is visited, left has already been visited in the first "if" block.
                    # so process the node
                    result.append(peek_node.val)
                    last_processed = stack.pop()
        return result

    def get_node_count(self):
        return len(self.in_order_trav_iterative())

    def is_in_tree(self, val):
        current = self.root
        if not current:
            print("Can not search in an empty tree")
            return
        while current:
            if val == current.val:
                return (True, current)
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return (False, None)

    def get_min(self):
        '''Returns minimum value stored in a tree'''
        current = self.root
        if current is None:
            print("Tree is empty")
            return
        while current.left:
            current = current.left
        return current.val

    def get_max(self):
        '''Returns max value stored in a tree'''
        current = self.root
        if current is None:
            print("Tree is empty")
            return
        while current.right:
            current = current.right
        return current.val

    def get_successor(self, val):
        '''
        Get the in-order successor from a binary tree for a given value
        Case 1: Node has a right subtree:
            Go to the leftmost node in the right subtree, OR
            find the minimum in the right subtree
        Case 2: No right subtree on the node:
            Go to the nearest ancestor for which given node would be in
            the left subtree. Or go to the first un-visited ancestor
        '''
        current = self.root
        if current is None:
            print("Tree is empty, No successor possible")
            return -1
        # find the node in the tree. If not present, break
        while current:
            if val == current.val:
                break
            elif val < current.val:
                # if value is smaller, go left
                current = current.left
            else:
                # if value is greater, go right
                current = current.right

        # only continue if node containing the required value is found, else break
        if not current:
            print("Given value not present in tree.")
        # if node has a right subtree, successor would be the minimum value in the right subtree
        if current.right:
            current = current.right
            # go left to find the leftmost node
            while current.left:
                current = current.left
            return current.val
        else:
            # if node has no right subtree:
            # The successor is the lowest ancestor for which the current node is in the left subtree
            # If no such ancestor exists, then this node is the maximum value in the tree and has no successor
            while current:
                if current.parent and current.parent.left == current:
                    return current.parent.val
                current = current.parent
            print("No successor of this node as it is the maximum value")
            return None

    def get_height_recursively(self, val):
        '''
        Get the height of the node containing the given val in the binary tree using recursion.
        The height of a node is max(height of left subtree, height of right subtree) + 1
        '''
        present, node = self.is_in_tree(val)
        if present:
            def height(node):
                if node is None:
                    return -1
                lheight = height(node.left)
                rheight = height(node.right)
                return max(lheight, rheight) + 1
            return height(node)

    def get_height_bfs(self, val):
        '''
        get the height of a binary tree using BFS.
        maintain a level_size variable to store the number of nodes at a level
        iterate over all the elements in the level and increment height by 1
        space complexity O(w), where w is the max width at any level, so better
        memory management than recursion.
        for balanced trees, w ~= n/2, where n = number of nodes in the tree
        '''
        present, node = self.is_in_tree(val)
        if present:
            queue = deque([node])
            height = -1
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    current = queue.popleft()
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                height += 1
            return height


def is_binary_search_tree(node):
    # In-order: Left -> Root -> Right
    import math
    p_infinity = math.inf
    n_infinity = -math.inf
    return is_bst_util(node, n_infinity, p_infinity)


def is_bst_util(node, min, max):
    if node is None:
        # In BST validation, a None node (empty subtree) is considered valid.
        # So it should return True.
        return True
    if node.val < min or node.val > max:
        return False

    return (is_bst_util(node.left, min, node.val)
            and is_bst_util(node.right, node.val, max))


def tests():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(10)
    tree.add(63)
    tree.add(7)
    tree.add(20)
    tree.add(56)
    tree.add(72)
    tree.add(4)
    tree.add(14)
    tree.add(16)
    tree.add(25)
    tree.add(60)
    print(f"IN ORDER: {tree.in_order_traversal()}")
    print(f"IN ORDER-ITERATIVE: {tree.in_order_trav_iterative()}")
    print(f"PRE ORDER: {tree.pre_order_traversal()}")
    print(f"PRE ORDER-ITERATIVE: {tree.pre_order_trav_iterative()}")
    print(f"POST ORDER: {tree.post_order_traversal()}")
    print(f"POST ORDER-ITERATIVE: {tree.post_order_trav_iterative()}")
    print(f"LEVEL ORDER: {tree.level_order_traversal()}")
    print(f"NODE COUNT IS: {tree.get_node_count()}")
    print(f"Value 50 present in tree: {tree.is_in_tree(50)}")
    print(f"Value 33 present in tree: {tree.is_in_tree(33)}")
    print(f"Minimum value stored in tree is {tree.get_min()}")
    print(f"Maximum value stored in tree is {tree.get_max()}")
    vals = [4, 7, 10, 14, 20, 25, 50, 56, 60, 63, 72]
    for val in vals:
        print(f"Successor of {val} in the tree is {tree.get_successor(val)}")
    print(f"Height of the tree using recursion is {tree.get_height_recursively(50)}")
    print(f"Height of the tree using BFS is {tree.get_height_bfs(50)}")
    tree.delete(4)
    tree.delete(56)
    tree.delete(10)
    print(f"IN ORDER TRAVERSAL AFTER DELETIONS: {tree.in_order_trav_iterative()}")
    print(f"Is valid Binary search tree: {is_binary_search_tree(tree.root)}")
    # create an invalid binary tree
    root = Node(100)
    root.left = Node(50)
    root.right = Node(150)
    root.right.left = Node(120)
    root.right.right = Node(90)  # Invalid: 90 < 100, but it's in right subtree
    print(f"Is valid Binary search tree: {is_binary_search_tree(root)}")


if __name__ == '__main__':
    tests()
