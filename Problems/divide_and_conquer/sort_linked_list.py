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
