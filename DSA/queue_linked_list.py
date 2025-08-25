"""Queue implementation using linked list data structure.

This module implements a FIFO (First In, First Out) queue using a singly linked list.
The queue maintains head and tail pointers for O(1) enqueue and dequeue operations.
Enqueue adds elements at the tail, dequeue removes from the head.
"""


class Node:
    '''Linked list node definition'''
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        vals = []
        while current:
            vals.append(str(current.val))
            current = current.next
        return str(vals)

    def empty(self) -> bool:
        if not self.head:
            print("Queue empty!")
            return True
        else:
            print(f"Queue has messages!. queue is {repr(self)}")
            return False

    def enqueue(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f"First message enqueued. Queue is : {repr(self)}")
            return
        last = self.tail
        last.next = new_node
        self.tail = new_node
        print(f"message queued at tail. Queue is: {repr(self)}")

    def dequeue(self):
        if self.empty():
            print("Queue Empty")
            return None
        front = self.head
        if front.next:
            next_to_front = front.next
            self.head = next_to_front
            print(f"message dequeued from front. Queue is: {repr(self)}")
            return front.val
        self.head = None
        print(f"Only message dequeued from front. Queue is empty: {repr(self)}")
        return front.val


def test_queue():
    # Initialize queue
    q = Queue()

    # Test empty queue
    assert q.empty() is True, "Empty queue should return True"

    # Test enqueue
    q.enqueue(1)
    assert q.head.val == 1, "Head should be 1"
    assert q.tail.val == 1, "Tail should be 1"

    # Test multiple enqueues
    q.enqueue(2)
    q.enqueue(3)
    assert q.head.val == 1, "Head should still be 1"
    assert q.tail.val == 3, "Tail should be 3"

    # Test dequeue
    val = q.dequeue()
    assert val == 1, "Dequeued value should be 1"
    assert q.head.val == 2, "New head should be 2"

    # Test dequeue until empty
    val = q.dequeue()
    assert val == 2, "Dequeued value should be 2"
    val = q.dequeue()
    assert val == 3, "Dequeued value should be 3"

    # Test dequeue empty queue
    q.dequeue()  # Should print "Queue Empty"


if __name__ == "__main__":
    test_queue()
    print("All tests passed!")
