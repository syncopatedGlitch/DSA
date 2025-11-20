from typing import List, Optional
'''
Given the head of a linked list, return the list
after sorting it in ascending order.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []
'''
'''
Intuition for Bottom-Up Merge Sort (O(1) space complexity):
Instead of splitting the list from the top down, you build
the solution from the bottom up.

1. Start with sublists of size 1: Every node is already a
   sorted list of size 1.
2. Merge pairs of size 1: Go through the list and merge
   adjacent lists of size 1 to create sorted lists of size 2.
3. Merge pairs of size 2: Now, go through the list again and
   merge adjacent sorted lists of size 2 to create sorted
   lists of size 4.
4. Merge pairs of size 4: Repeat the process to create sorted
   lists of size 8.
5. Continue this process, doubling the sublist size
   (1, 2, 4, 8, ...) until you've merged the entire list.

This approach is iterative (done in a for loop that
increases the size), so it doesn't use any recursion stack
space, achieving true O(1) space complexity.

Summary of Intuition

1. The O(n log n) time constraint points directly to Merge Sort.
2. The "divide" step can be solved efficiently using the fast
   and slow pointer trick to find the middle.
3. The "merge" step is a standard algorithm for combining two
   sorted lists.
4. This leads to a natural recursive (top-down) solution which
   is O(log n) space.
5. To achieve true O(1) space, you can implement an iterative
   (bottom-up) Merge Sort, which builds the solution by
   merging progressively larger sorted sublists.
'''
'''
Iterative O(1) approach

The Pointers (The "Cast of Characters")

For a true O(1) space bottom-up merge sort, you need these
key pointers:

1. `dummy_head`: A fixed, unchanging node that exists outside
   the list. Its next pointer will always point to the head of
   the list we are currently building.
   * Purpose: It solves the problem of "what if the original
     head of the list is no longer the head after a merge?"
     By using a dummy node, we never have to worry about
     updating the main head variable in a special if case.
     We just build off the dummy, and at the end, dummy_head.next
     is our new head.

2. `tail`: The "builder" pointer. It always points to the last
   node of the sorted portion we have built so far.
    * Purpose: We use this to append the next merged sublist.
      After merging list1 and list2, we'll do tail.next = merged_list
      to hook it onto our result.

3. `current`: The "traversal" pointer. It walks along the list,
   marking the beginning of the next section that needs to be
   processed.
    * Purpose: It keeps track of where we are in the overall list.

The Loops

You'll have two nested while loops:

* Outer `while` loop: Controls the size of the sublists you are
  merging (1, 2, 4, 8...).
It continues as long as size is less than the total length of the list.
* Inner `while` loop: This is where the pointers do their dance. It
  walks through the entire list, merging adjacent pairs of sublists
  of the current size. It continues as long as current is not null.


Detailed Pointer Use in the Inner Loop

Let's walk through one iteration of the inner while loop.
Assume size = 2. Our list is conceptually [1, 5], [2, 8], [3, 4].

Initial State before this iteration:
* dummy_head points to the head of our sorted result so far.
* tail points to the last node of that result.
* current points to the node 3 (the start of the next section
  to process).

Here are the steps:
The Setup

* Our List: 4 -> 3 -> 2 -> 1 -> null
* Our Context: We are starting the very first pass of the
  sort. The size for this pass is 1.
* Main Pointers:
    * dummy = TreeNode(0) (A placeholder node)
    * tail = dummy (The end of our sorted list, starts at the dummy)
    * current = 4 (The head of the portion we still need to process)

Visual State before the iteration:

 List to be processed:
 current
   |
   v
   4  ->  3  ->  2  ->  1  -> null

 Our sorted result (so far):
 dummy -> null
    ^
   |
  tail

---

The Inner Loop: A Single Iteration

We are now inside the while current: loop.

Step 1 & 2: Define `left` and `right` using `split`

The code to execute is:
left = current
right = split(left, 1)

1. left is assigned the value of current. So, left now points
   to node 4.
2. Now we call `split(head=left, size=1)`. Let's go inside
   this function.

* Inside `split(head=4, size=1)`:
    * The function receives a pointer to node 4.
    * Goal: Find the 1st node, break the link after it, and
      return the rest.
    * A temporary pointer, let's call it split_ptr, is
      created and points to head (node 4).
    * The function needs to traverse size - 1 (which is 1 - 1 = 0)
      times. So, the traversal loop doesn't run at all. split_ptr
      remains pointing at node 4.
    * split_ptr is now at the last node of the sublist we want
      to keep.
    * Before breaking the link, we save the next part. A new
      variable rest_of_list is created. rest_of_list = split_ptr.next.
      The next of node 4 is node 3. So, rest_of_list now points to
      node 3.
    * Now, we cut the link. split_ptr.next = null. The next pointer
      of node 4, which was pointing to 3, is now set to null.
    * The function returns rest_of_list. It returns the pointer to
      node 3.

3. Back in our main loop, the returned pointer to node 3 is assigned
   to the right variable.

Visual State after Step 2:

We now have two separate list segments:
left -> 4 -> null
right -> 3 -> 2 -> 1 -> null

Step 3: Define `remaining` using `split`

The code to execute is: remaining = split(right, 1)

1. Now we call `split(head=right, size=1)`. Let's go inside this
   function again.
    * Inside `split(head=3, size=1)`:
        * The function receives a pointer to node 3.
        * The traversal loop runs 0 times. The split_ptr
          stays at node 3.
        * Save the next part: rest_of_list = split_ptr.next.
          The next of node 3 is node 2. So, rest_of_list now
          points to node 2.
        * Cut the link: split_ptr.next = null. The next pointer
          of node 3 is set to null.
        * The function returns rest_of_list. It returns the pointer
          to node 2.

2. Back in our main loop, the returned pointer to node 2 is assigned
   to the remaining variable.

Visual State after Step 3:

We now have three separate list segments:
left      -> 4 -> null
right     -> 3 -> null
remaining -> 2 -> 1 -> null

Step 4, 5, 6: Merge and Append

1. Merge: merged = merge(left, right) is called. Merging [4] and [3]
   returns a new sorted list: 3 -> 4 -> null.

2. Append: tail.next = merged.
    * Our tail pointer is still pointing at dummy.
    * So, dummy.next is set to the head of the merged list (node 3).

3. Update `tail`: The tail must be moved to the end of the newly
   added section.
    * The code walks the tail pointer forward: tail moves to 3, then
      tail.next is 4, so tail moves to 4. tail.next is now null, so
      the update stops.
    * tail now points to node 4.

Visual State after Step 6:

List to be processed:
remaining -> 2 -> 1 -> null
Our sorted result:
dummy -> 3 -> 4 -> null
             ^
             |
            tail

Step 7: Advance `current`

The code is: current = remaining.
* current now points to node 2.

End of Iteration Summary

The first iteration of the inner loop is complete.

* The dummy node now anchors our partially sorted list (3 -> 4).
* The tail pointer is correctly positioned at the end of this
  sorted section (at node 4), ready to append the next merged chunk.
* The current pointer is correctly positioned at the start of the
  next section of the list that needs to be processed (2 -> 1).

The loop will now repeat this entire process starting from
current = 2.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''Iterative Solution O(1) space'''
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        print(f"length of linked list is {length}")
        dummy = ListNode()
        dummy.next = head
        size = 1

        while size < length:
            tail = dummy
            current = tail.next
            print(f"size is {size}")
            print(f"linked list at start is {linked_list_to_list(dummy.next)}")
            while current:
                # split the list by size into left and right chunks
                left = current
                print(f"left is {left.val}")
                # returns the pointer to start of right half after
                # snipping the left
                right = self.split(left, size)
                print(f"right is {right.val if right else None}")
                # returns the pointer to start of remaining list after
                # snipping the right
                remaining = self.split(right, size)
                print(f"remaining is {remaining.val if remaining else None}")
                # merge the left and right halves and return the head
                # of the sorted merged list
                merged = self.merge(left, right)
                print(f"merged is {merged.val}")
                # tail points to the end of the sorted part of list
                # it points to dummy at the beginning, so tail.next
                # really means dummy.next for 1st iteration.
                # after that, it just connects the merged part to the
                # end of sorted list
                tail.next = merged
                # after merging the newly sorted part with existing,
                # tail moves to the end of the newly sorted and merged
                # list
                while tail.next:
                    tail = tail.next
                # move the current pointer to the head of remaining
                # list to be sorted. This is where we start from in the
                # next iteration.
                current = remaining
            size *= 2
            print(f"linked list at end is {linked_list_to_list(dummy.next)}")
            print(f"size incremented to {size}")
        return dummy.next

    def split(self, node: ListNode, size: int) -> Optional[ListNode]:
        for _ in range(size-1):
            if node:
                node = node.next
        if node:
            rest_of_list = node.next
            node.next = None
        else:
            rest_of_list = None
        return rest_of_list

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        print("merge called")
        dummy = ListNode()
        current = dummy
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            elif right.val < left.val:
                current.next = right
                right = right.next
            current = current.next
        if left:
            current.next = left
        elif right:
            current.next = right
        return dummy.next


class RecursionSolution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort(node):
            if not node or not node.next:
                return node
            slow, fast = node, node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            right = slow.next
            slow.next = None
            l = sort(node)
            r = sort(right)

            dummy = ListNode()
            curr = dummy
            while l and r:
                if l.val <= r.val:
                    curr.next = l
                    l = l.next
                else:
                    curr.next = r
                    r = r.next
                curr = curr.next
            if l:
                curr.next = l
            elif r:
                curr.next = r
            return dummy.next
        return sort(head)


def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert a linked list back to a list
    for assertion."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def tests():
    sol = Solution()
    solrec = RecursionSolution()

    # Example 1
    head1 = create_linked_list([4, 2, 1, 3])
    h1 = create_linked_list([4, 2, 1, 3])
    expected1 = [1, 2, 3, 4]
    result1 = sol.sortList(head1)
    res1 = solrec.sortList(h1)
    print(f"res1 is {linked_list_to_list(res1)}")
    assert linked_list_to_list(result1) == expected1
    assert linked_list_to_list(res1) == expected1
    print("Test Case 1 (head=[4,2,1,3]) passed.")

    # Example 2
    head2 = create_linked_list([-1, 5, 3, 4, 0])
    h2 = create_linked_list([-1, 5, 3, 4, 0])
    expected2 = [-1, 0, 3, 4, 5]
    result2 = sol.sortList(head2)
    res2 = solrec.sortList(h2)
    assert linked_list_to_list(result2) == expected2
    assert linked_list_to_list(res2) == expected2
    print("Test Case 2 (head=[-1,5,3,4,0]) passed.")

    # Example 3
    head3 = create_linked_list([])
    h3 = create_linked_list([])
    expected3 = []
    result3 = sol.sortList(head3)
    res3 = solrec.sortList(h3)
    assert linked_list_to_list(result3) == expected3
    assert linked_list_to_list(res3) == expected3
    print("Test Case 3 (head=[]) passed.")


if __name__ == "__main__":
    tests()
