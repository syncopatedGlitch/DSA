"""Queue Implementation Using Circular Array

This module implements a queue data structure using a fixed-size circular array.
The circular approach efficiently reuses array space by wrapping indices around
when they reach the array boundary.

Key Features:
- FIFO (First In, First Out) ordering
- Fixed capacity with overflow protection
- O(1) enqueue and dequeue operations
- Circular buffer prevents memory waste
- Uses front/rear pointers with modular arithmetic

Implementation Details:
- Array size = capacity + 1 (one extra slot to distinguish full vs empty)
- front: points to first element to be dequeued
- rear: points to next position for enqueue
- Circular increment: (index + 1) % capacity
- Empty condition: front == rear
- Full condition: (rear + 1) % capacity == front
"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity + 1
        self.data = [None] * (self.capacity + 1)  # Initialize the fixed size array
        self.front = 0
        self.rear = 0
        self.size = 0  # Currently empty

    def __repr__(self):
        """String representation of the queue for debugging."""
        if self.empty():
            return "Queue([])"
        elements = []
        index = self.front
        for _ in range(self.size):
            elements.append(str(self.data[index]))
            index = (index + 1) % self.capacity
        return f"[{', '.join(elements)}]"

    def enqueue(self, val):
        # always check if within capacity before adding
        if self.full():
            raise IndexError("Queue is full")
        self.data[self.rear] = val
        self.rear = (self.rear + 1) % self.capacity  # Circular Increment
        self.size += 1
        print(f"Value {val} enqueued. Queue is {repr(self)}. Size is {self.size}")

    def dequeue(self):
        """
            Returns value and removes least recently added element.
            Returns:
                The value of the front element
            Raises:
                IndexError: If the queue is empty
        """
        if self.front == self.rear:
            raise IndexError("Queue is empty")
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Value Dequeued is {val}. Queue is {repr(self)}. Size is {self.size}")
        return val

    def empty(self):
        '''
        Returns True if Queue is empty, else returns False
        They can only collide in a circular world when they are empty
        '''
        return self.size == 0

    def full(self):
        '''
        Return True if the Queue is full, else returns False
        Considers the buffer of 1 so that the front and rear do not collide
        while enque. They should only collide when the queue is empty.
        '''
        return (self.rear + 1) % self.capacity == self.front


def test_queue():
    q = Queue(3)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.full(), "Queue should be full"
    assert q.dequeue() == 1, "Dequeued value should be 1"
    q.enqueue(4)
    assert q.dequeue() == 2, "Dequeued value should be 2"
    assert q.dequeue() == 3, "Dequeued value should be 3"
    assert q.dequeue() == 4, "Dequeued value should be 4"
    assert q.empty(), "Queue should be empty"
    try:
        q.dequeue()
    except Exception as e:
        print(f"Dequeue on empty queue. exception raised: {str(e)}")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    try:
        q.enqueue(1)
    except Exception as e:
        print(f"enqueue on a full queue. Exception raised: {str(e)}")


if __name__ == '__main__':
    test_queue()
    print("All tests passed!")
