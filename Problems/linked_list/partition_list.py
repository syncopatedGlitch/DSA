from typing import Optional
'''
https://leetcode.com/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150
Given the head of a linked list and a value x,
partition it such that all nodes less than x
come before nodes greater than or equal to x.

You should preserve the original relative order
of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
'''
'''
the core intuition is: Don't rearrange the existing list.
Instead, build two brand new lists and then connect them.

Here's the step-by-step thinking:

1. Create Two New Lists: Imagine you have two empty lists.
    * One list will hold all the nodes with values less
      than `x`. Let's call it the less_list.
    * The other list will hold all the nodes with values
      greater than or equal to `x`. Let's call it the
      greater_equal_list.

2. Iterate and Distribute:
    * Walk through the original linked list from the head,
      one node at a time.
    * For each node you visit, check its value:
        * If node.val < x, append it to the end of your
          less_list.
        * If node.val >= x, append it to the end of your
          greater_equal_list.

3. Preserving Order: Because you are iterating through the
   original list in order and simply appending to the end
   of your new lists, the original relative order within
   each group is naturally preserved. For example, the
   first node you see that's < x will be the first node in
   your less_list. The second one you see will be the second,
   and so on.

4. Stitch Them Together:
    * After you've processed all the nodes from the original
      list, you'll have two separate, correctly ordered lists.
    * The final step is to connect the tail of the less_list
      to the head of the greater_equal_list.

5. A Small but Important Detail: You also need to make sure
   the tail of the greater_equal_list points to None to
   properly terminate the newly combined list.

This "two-pointer" or "two-list" approach is much simpler
and cleaner than trying to perform complex swaps in place.
To implement it, you'll typically use four pointers: a head
and a tail for each of the two new lists you're building.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(
            self,
            head: Optional[ListNode],
            x: int
    ) -> Optional[ListNode]:
        dummy_less = ListNode(0)
        dummy_greater = ListNode(0) 

        less_current = dummy_less
        greater_current = dummy_greater

        node = head
        while node:
            if node.val < x:
                less_current.next = node
                less_current = less_current.next
            else:
                greater_current.next = node
                greater_current = greater_current.next
            node = node.next
        greater_current.next = None
        less_current.next = dummy_greater.next
        return dummy_less.next


def create_linked_list(values: list) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Helper function to convert a linked list back to a list."""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def tests():
    sol = Solution()

    # Example 1
    head1 = create_linked_list([1, 4, 3, 2, 5, 2])
    x1 = 3
    expected1 = [1, 2, 2, 4, 3, 5]
    result_head1 = sol.partition(head1, x1)
    res1 = linked_list_to_list(result_head1)
    print(f"res1 is {res1}")
    assert res1 == expected1
    print("Test Case 1 Passed")

    # Example 2
    head2 = create_linked_list([2, 1])
    x2 = 2
    expected2 = [1, 2]
    result_head2 = sol.partition(head2, x2)
    assert linked_list_to_list(result_head2) == expected2
    print("Test Case 2 Passed")


if __name__ == "__main__":
    tests()
