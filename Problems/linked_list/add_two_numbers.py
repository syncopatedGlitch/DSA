"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in
reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum
as a linked list.

You may assume the two numbers do not contain any
leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from DSA.linked_lists import LinkedList


def add_two_numbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
    first_pointer = l1.head
    second_pointer = l2.head
    carry = 0
    result = LinkedList()
    while first_pointer or second_pointer or carry:
        val1 = first_pointer.val if first_pointer else 0
        val2 = second_pointer.val if second_pointer else 0
        res = val1 + val2 + carry
        digit = res % 10
        result.push_back(digit)
        carry = res // 10
        first_pointer = first_pointer.next if first_pointer else None
        second_pointer = second_pointer.next if second_pointer else None
    return result


def tests():
    list1 = [2, 4, 3]
    l1 = LinkedList()
    for item in list1:
        l1.push_back(item)
    list2 = [5, 6, 4]
    l2 = LinkedList()
    for item in list2:
        l2.push_back(item)
    res = add_two_numbers(l1, l2)
    output = res.return_list()
    print(f"output for {list1} and {list2} is {output}")
    assert output == [7, 0, 8]
    list1 = [0]
    l1 = LinkedList()
    for item in list1:
        l1.push_back(item)
    list2 = [0]
    l2 = LinkedList()
    for item in list2:
        l2.push_back(item)
    res = add_two_numbers(l1, l2)
    output = res.return_list()
    print(f"output for {list1} and {list2} is {output}")
    assert output == [0]
    list1 = [9, 9, 9, 9, 9, 9, 9]
    l1 = LinkedList()
    for item in list1:
        l1.push_back(item)
    list2 = [9, 9, 9, 9]
    l2 = LinkedList()
    for item in list2:
        l2.push_back(item)
    res = add_two_numbers(l1, l2)
    output = res.return_list()
    print(f"output for {list1} and {list2} is {output}")
    assert output == [8, 9, 9, 9, 0, 0, 0, 1]


tests()
