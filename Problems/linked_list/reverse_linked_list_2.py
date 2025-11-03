"""
Given the head of a singly linked list and two integers
left and right where left <= right, reverse the nodes
of the list from position left to position right, and
return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""

from DSA.linked_lists import LinkedList, Node


def reverse_liinked_list(ll: LinkedList, left: int, right: int) -> LinkedList:
    if left == right:
        return ll
    # this will be universal dummy node that acts as protection
    # when head is the left node to be reversed.
    dummy = Node(None)
    dummy.next = ll.head
    current = ll.head
    previous = dummy
    index = 1
    start_break = None
    left_node = None
    start = False
    while current:
        next = current.next
        if index == left:
            start = True
            left_node = current
            start_break = previous
        elif index == right:
            start = False
            current.next = previous
            start_break.next = current
            left_node.next = next
        if start:
            current.next = previous
        previous = current
        current = next
        index += 1
    ll.head = dummy.next
    return ll


def tests():
    l1 = [1, 2, 3, 4, 5]
    li = LinkedList()
    for i in l1:
        li.push_back(i)
    left = 2
    right = 4
    res = reverse_liinked_list(li, left, right)
    print(
        f"output for {l1}, left {left} and right {right} is {res.return_list()}"
    )
    assert res.return_list() == [1, 4, 3, 2, 5]
    l2 = [5]
    ls = LinkedList()
    for i in l2:
        ls.push_back(i)
    left = 1
    right = 1
    res1 = reverse_liinked_list(ls, left, right)
    print(
        f"output for {l2}, left {left} and right {right} is {res1.return_list()}"
    )
    assert res1.return_list() == [5]
    l3 = [3, 5]
    ls3 = LinkedList()
    for i in l3:
        ls3.push_back(i)
    left = 1
    right = 2
    res3 = reverse_liinked_list(ls3, left, right)
    print(
        f"output for {l3}, left {left} and right {right} is {res3.return_list()}"
    )
    assert res3.return_list() == [5, 3]


tests()
