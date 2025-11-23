from typing import List, Optional
import heapq
'''
You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted
linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''

'''
Intuition 3: Divide and Conquer (like Merge Sort)

* Idea: The problem with the one-by-one approach was the
  unbalanced merges. This is the exact problem Merge Sort
  solves! Instead of merging (list1+list2) with list3,
  why not merge (list1+list2) with (list3+list4)?
* Process:
    1. Pair up the k lists and merge each pair. This gives
       you k/2 sorted lists.
    2. Now you have a new, smaller problem. Pair up those
       k/2 lists and merge them. This gives you k/4 sorted lists.
    3. Repeat this process until you are left with only one list.
* Analysis:
    * Pro: This is much more efficient because the merges are
      always between lists of roughly similar size.
    * Complexity: You are merging a total of N elements at
      each "level" of pairing. The number of levels it takes to
      go from k lists down to 1 is log k. This gives a time
      complexity of O(N log k). This is a very good solution!

Intuition 4: The Optimal Approach (Using a Min-Heap)

This is the most elegant intuition. Let's go back to our core
question: "What is the absolute smallest element available
right now?"

The candidates for the next smallest element are always the
front elements of each of the k lists.

* Idea: What if we had a machine that could hold just the
  front element from each of the k lists and could instantly
  tell us which one is the smallest? This is exactly
  what a Min-Heap (also called a Priority Queue) does.

* Process:
    1. Create a Min-Heap.
    2. Take the very first element from each of the k lists
       and put them all into the heap.
    3. Now, the smallest element in the entire system is at
       the top of the heap.
    4. Loop until the heap is empty:
        a. Extract: Pop the smallest element from the heap.
           This is the next element for our final sorted list.
           Add it to the result.
        b. Replenish: The element you just popped came from
           one of the k lists. Take the next element from that
           same list and add it to the heap.
* Why this works: By always extracting the minimum and
  immediately replenishing the heap with the next candidate
  from the same list, you ensure the heap always holds
  the k best candidates for the next overall smallest element.
  You are efficiently outsourcing the "find the minimum" job
  to the heap.

* Analysis:
    * Pro: This is a direct and very efficient model of
      the problem.
    * Complexity:
        * The heap will hold at most k elements.
        * Every add and extract-min operation on the heap
          takes O(log k) time.
        * You have to do this for all N elements in total.
        * This gives a final time complexity of O(N log k).
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
            self,
            lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        unique_id = 0
        my_heap = []
        num_lists = len(lists)
        for i in range(num_lists):
            node = lists[i]
            if node:
                heapq.heappush(my_heap, (node.val, unique_id, node))
                unique_id += 1
        dummy = ListNode()
        current = dummy
        while my_heap:
            val, _, node = heapq.heappop(my_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(my_heap, (node.next.val, unique_id, node.next))
                unique_id += 1
        return dummy.next


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
    """
    Helper function to convert a linked list back to a
    list for assertion.
    """
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def tests():
    sol = Solution()

    # Example 1
    lists1_input = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists1 = [create_linked_list(lis) for lis in lists1_input]
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]
    result1 = sol.mergeKLists(lists1)
    assert linked_list_to_list(result1) == expected1
    print("Test Case 1 (lists=[[1,4,5],[1,3,4],[2,6]]) passed.")

    # Example 2
    lists2 = []
    expected2 = []
    result2 = sol.mergeKLists(lists2)
    assert linked_list_to_list(result2) == expected2
    print("Test Case 2 (lists=[]) passed.")

    # Example 3
    lists3 = [create_linked_list([])]
    expected3 = []
    result3 = sol.mergeKLists(lists3)
    assert linked_list_to_list(result3) == expected3
    print("Test Case 3 (lists=[[]]) passed.")


if __name__ == "__main__":
    tests()
