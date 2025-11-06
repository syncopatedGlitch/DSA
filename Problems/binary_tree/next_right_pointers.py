'''
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its
next right node. If there is no next right
node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree
(Figure A), your function should populate
each next pointer to point to its next right
node, just like in Figure B. The serialized
output is in level order as connected by the
next pointers, with '#' signifying the end
of each level.

Example 2:

Input: root = []
Output: []
'''
'''
High-Level Algorithm:

   1. Establish a "dummy" head node that will always point
      to the start of the next level you are about to
      connect. Let's call it dummy_head.
   2. Use a tail pointer, initially pointing to dummy_head,
   to build the linked list for the next level.
   3. Use a current pointer to iterate through the nodes of
      the level you are currently on.
   4. Loop as long as current is not null:
      a. While iterating through the current level
         (using current = current.next), look at the children
         of the current node.
      b. If current.left exists, this is the next node in the
         level below, so you connect it: tail.next = current.left,
         and then advance the tail: tail = tail.next.
      c. Do the same for current.right.
      d. When the inner loop finishes, you have visited every
         node on the current level.
  The next level is now fully connected, and dummy_head.next
  is its starting node.
      e. To start the next major iteration, set
         current = dummy_head.next, and reset the dummy_head and\
         tail to prepare for connecting the next level.

  This approach only requires a few pointers for bookkeeping,
  giving it O(1) space complexity while maintaining the optimal
  O(V) time complexity.
'''


class Node:
    def __init__(
            self,
            val: int = 0,
            left: 'Node' = None,
            right: 'Node' = None,
            next: 'Node' = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level_head = root
        dummy = Node(0)
        tail = dummy
        while level_head is not None:
            current = level_head
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next
            level_head = dummy.next
            dummy = Node(0)
            tail = dummy
        return root
