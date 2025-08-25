"""Queue Implementation Using Python Collections.deque

This module demonstrates queue implementation using Python's built-in collections.deque,
which provides an optimized double-ended queue implementation. This approach leverages
Python's standard library for efficient queue operations.

collections.deque Features:
- Optimized for fast appends and pops from both ends
- Thread-safe for basic operations
- Memory efficient with no fixed size limit
- Implements queue operations with O(1) time complexity

Key Advantages:
- No need to implement low-level data structure details
- Highly optimized C implementation
- Built-in methods for common queue operations
- Automatic memory management

Queue Operations:
- enqueue: Add element to rear of queue
- dequeue: Remove element from front of queue
- peek: View front element without removing
- isEmpty: Check if queue is empty

Time Complexities:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Space: O(n)
"""

from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, item):
        self.buffer.append(item)

    def dequeue(self):
        if not self.buffer:
            raise IndexError("Queue is empty")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Output: 1
    print(q.dequeue())  # Output: 2
    print(q.is_empty())  # Output: False
    print(q.dequeue())  # Output: 3
    print(q.is_empty())  # Output: True
    try:
        q.dequeue()  # Should print "Queue Empty"
    except IndexError as e:
        print(e)
