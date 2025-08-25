"""Linked List Data Structure Implementation

This module implements a singly linked list, a fundamental linear data structure where
elements (nodes) are stored in sequence, with each node containing data and a reference
to the next node.

Key Features:
- Dynamic size allocation
- Efficient insertion and deletion at the beginning (O(1))
- Sequential access to elements
- Memory efficient for sparse data

Operations included:
- Insert at beginning, end, or specific position
- Delete by value or position
- Search for elements
- Display and traverse the list

Time Complexities:
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at head, O(n) at arbitrary position
- Deletion: O(1) at head, O(n) at arbitrary position
"""

# Linked list implementation

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        vals = []
        while current:
            vals.append(str(current.val))
            current = current.next
        return str(vals)

    def push_back(self, val):
        '''Add a new node at the end'''
        new_node = Node(val)
        # if the list is empty, point the head to new node
        if self.head is None:
            self.head = new_node
            return
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next

            # Add new node at the end
            current.next = new_node

    def push_front(self, val):
        '''Add a new node at the front'''
        new_node = Node(val)
        first = self.head
        self.head = new_node
        new_node.next = first

    def size(self):
        """get the length of the linked list"""
        len = 0
        current = self.head
        while current:
            len += 1
            current = current.next
        return len

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def value_at(self, index):
        '''returns the value at the given index, starting from 0'''
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val
            count += 1
            current = current.next

    def _node_at(self, index):
        '''returns the node at a given index, starting from 0'''
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next

    def pop_front(self):
        '''remove the front item and return its value'''
        current = self.head
        next_node = current.next
        self.head = next_node
        return current.val

    def pop_back(self):
        '''removes end item and returns its value'''
        current = self.head
        # if empty, return None
        if current is None:
            return None

        # if only 1 node, return the value and reset head
        if current.next is None:
            val = current.val
            self.head = None
            return val

        # traverse to the second last eleemnt of the list
        while current.next.next:
            current = current.next

        val = current.next.val  # store the value of the last node
        current.next = None  # remove the last node
        return val  # return the value

    def front(self):
        '''get the value of the front item'''
        return self.head.val

    def back(self):
        '''get the value from the end'''
        current = self.head
        while current.next:
            current = current.next

        return current.val

    def insert(self, index, val):
        '''inserts the value at index, so current item at that index is pointed to by new item at index'''
        new_node = Node(val)
        if index == 0:
            self.push_front(val)
            return
        node_before_index = self._node_at(index-1)
        node_at_index = node_before_index.next
        node_before_index.next = new_node
        new_node.next = node_at_index

    def erase(self, index):
        '''removes node at given index'''
        if index == 0:
            self.pop_front()
            return
        node_before_index = self._node_at(index-1)
        node_at_index = node_before_index.next
        if node_at_index.next is None:
            node_before_index.next = None
            return
        node_before_index.next = node_at_index.next

    def reverse(self):
        '''reverse the linked list'''
        # TODO implement this.
        pass


if __name__ == '__main__':
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    llist.push_back(5)
    llist.push_front(0)
    print(f"size is {llist.size()}")
    print(f"List Empty: {llist.is_empty()}")
    print(f"Valur at index 3 is {llist.value_at(index=3)}")
    print(f"list is {repr(llist)}")
    print(f"popped the value from the front and returned value was {llist.pop_front()}.")
    print(f"Now list is {repr(llist)}")
    print(f"popped the value from the end and returned value was {llist.pop_back()}.")
    print(f"Now list is {repr(llist)}")
    print(f"front value is {llist.front()}")
    print(f"last value is {llist.back()}")
    llist.insert(3, 8)
    print(f"after inserting new value 8 at index 3, list is {repr(llist)}")
    llist.erase(3)
    print(f"after erasing the index 3 value, the list is {repr(llist)}")
