'''
In an array-based heap:
• Elements are stored in a contiguous array
• Parent-child relationships are maintained through
  index calculations:
  • For element at index i (in zero based indexing):
    • Left child: 2i + 1
    • Right child: 2i + 2
    • Parent: (i-1)/2
• The root is always at index 0
• This creates an implicit binary tree structure without
  storing explicit pointers

Advantages of array implementation:
• Memory efficient (no pointer overhead)
• Better cache locality
• Simpler to implement
• O(1) access to parent/child relationships

Binary Tree Implementation (Less Common)
A heap can also be implemented as an explicit binary tree
with nodes containing:
• Data value
• Pointers to left and right children
• Sometimes a pointer to parent

Disadvantages of tree implementation:
• Higher memory overhead due to pointers
• Worse cache performance
• More complex implementation
• Potential memory fragmentation

This module has array based implementation for MIN HEAP
which is the most common implementation approach
'''


class Heap:
    def __init__(self, arr: list):
        self.min_heap = self.heapify(arr)

    def has_right_child(self, arr: list, index: int) -> tuple:
        '''
        Inputs: heap array and index of the element to find the
        right child for
        '''
        idx = (2*index) + 2
        return (True, idx) if idx < len(arr) else (False, None)

    def has_left_child(self, arr: list, index: int) -> tuple:
        '''
        Inputs: heap array and index of the element to find the
        left child for
        '''
        idx = (2*index) + 1
        return (True, idx) if idx < len(arr) else (False, None)

    def has_parent(self, arr: list, index: int) -> tuple:
        '''
        Inputs: heap array and index of the element to find the
        parent for
        '''
        if index == 0:  # Root has no parent
            return (False, None)
        idx = (index - 1) // 2
        return (True, idx)

    def heapify(self, arr: list) -> list:
        '''
        AI Description:
        Create a heap from an unsorted array by going bottom up
        and pushing the elements down.
        Start from the last non-leaf node and heapify each subtree.
        '''
        if not arr:
            return []
        # Start from the last non-leaf node (parent of last element)
        start_index = (len(arr) - 2) // 2
        # The start_index + 1 is needed because range() is exclusive
        # of the end value.
        # Example with your array (length 8):
        # start_index = (8 - 2) // 2 = 3
        # We want to iterate through indices: [3, 2, 1, 0]
        # Without +1:
        # range(3) = [0, 1, 2] (stops before 3)
        # reversed(range(3)) = [2, 1, 0] (missing index 3!)
        for i in reversed(range(start_index + 1)):
            self.sift_down(arr, i, len(arr) - 1)
        return arr

    def sift_down(self, arr: list, index: int, heap_size: int):
        '''
        push each element down recursively until it reaches its right place.
        '''
        current = index

        while True:
            right_present, right_index = self.has_right_child(arr, current)
            left_present, left_index = self.has_left_child(arr, current)
            # If no children, we're done.
            if not right_present and not left_present:
                print("Sift Down not possible, no children found")
                break
            if right_present and right_index >= heap_size:
                right_present = False
            if left_present and left_index >= heap_size:
                left_present = False

            # Find the largest among current and its children
            children = []
            if right_present:
                children.append(right_index)
            if left_present:
                children.append(left_index)
            if not children:
                print("Sift Down not possible, no children found")
                break
            min_child_index = min(children, key=lambda idx: arr[idx])
            # if current is already smaller than the min child, heap
            # property satisfied
            if arr[current] < arr[min_child_index]:
                break
            # swap and continue from the swapped position
            arr[current], arr[min_child_index] = arr[min_child_index], \
                arr[current]
            current = min_child_index

    def get_max(self):
        '''returns the max element from the heap without removing it'''
        return self.min_heap[0]

    def is_empty(self):
        if not self.min_heap:
            return True
        else:
            return False

    def extract_max_priority(self):
        '''
        Return the max item from the heap, removing it.
        The standard approach is to:
            Replace root with last element - O(1)
            Remove last element with pop() - O(1)
            Heapify down from root - O(log n)
        '''
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], \
            self.min_heap[0]
        max_item = self.min_heap.pop()
        self.sift_down(self.min_heap, 0, len(self.min_heap) - 1)
        return max_item

    def insert(self, val):
        '''
        Insert an element into a heap
        Add the element at the end of array and sift up to reach
        the right spot
        '''
        self.min_heap.append(val)
        self.sift_up(self.min_heap, (len(self.min_heap) - 1))

    def sift_up(self, arr, index):
        '''
        takes the index of the element from the heap and shifts
        it up until it reaches its right place
        '''
        while True:
            has_parent, parent_index = self.has_parent(arr, index)
            if not has_parent:
                break
            elif arr[parent_index] > arr[index]:
                arr[parent_index], arr[index] = arr[index], \
                    arr[parent_index]
                index = parent_index
            elif arr[parent_index] < arr[index]:
                break

    def remove(self, index):
        '''
        Remove an element at a given index from the heap.
        Principles for deletion:
        1. Replace the element to be deleted with the last element in
        the heap, then remove the last position.
        After replacement, the heap property might be violated in two
        possible directions:
        • **Upward violation**: New element is smaller than its parent
          (min-heap) or larger than parent (max-heap)
        • **Downward violation**: New element is larger than children
          (min-heap) or smaller than children (max-heap)
        2. If the new element is "better" than its parent (smaller in
           min-heap, larger in max-heap), bubble it up by repeatedly
           swapping with parent until heap property is restored.
        3. If the new element is "worse" than its children (larger in
           min-heap, smaller in max-heap), bubble it down by repeatedly
           swapping with the better child until heap property is restored.

        After replacement, you only need to fix in ONE direction:
        either up OR down, never both.
        Edge case handling:
            a. if deleting root, then always sift_down
            b. If deleting a leaf with no clildren, always sift up
            c. if deleting last element, just pop. Nothing else needed.
        '''
        if index < 0 or index >= len(self.min_heap):
            print("Index out of bounds")
            return
        elif index == 0:  # deleting root
            self.extract_max_priority()
            return
        # deleting last leaf or last item of the array
        elif index == len(self.min_heap) - 1:
            self.min_heap.pop()
            return
        # Replace last element with the element at index,
        # then remove last element
        self.min_heap[index] = self.min_heap[-1]
        self.min_heap.pop()

        # Now we need to restore heap property at the new position
        left_present, left_index = self.has_left_child(
            self.min_heap, index
        )
        right_present, right_index = self.has_right_child(
            self.min_heap, index
        )
        parent_present, parent_index = self.has_parent(
            self.min_heap, index
        )
        # leaf with no children, always sift up
        if not left_present and not right_present:
            self.sift_up(self.min_heap, index)
        else:
            # compare with parent and sift up if parent is worst
            # than current index
            if parent_present and (self.min_heap[index]
                                   < self.min_heap[parent_index]):
                self.sift_up(self.min_heap, index)
            else:
                # compare with both children and sift down if needed
                children = []
                if left_present:
                    children.append(left_index)
                if right_present:
                    children.append(right_index)
                if children:
                    min_child_index = min(children,
                                          key=lambda idx: self.min_heap[idx]
                                          )
                    if self.min_heap[index] > self.min_heap[min_child_index]:
                        self.sift_down(
                            self.min_heap, index, len(self.min_heap) - 1
                        )

    def heap_sort(self) -> list:
        '''
        Heap Sort Algorithm (Descending Order with Min Heap):
        1. Build min heap from input array
        2. For i from (n-1) down to 1:
            a. Swap root (minimum) with element at position i
            b. Reduce heap size to i (exclude sorted portion)
            c. Sift down from root to restore heap property
               in reduced heap
        3. Result: Array sorted in descending order

        Key insight: Extract minimum to end positions,
        heap shrinks from right to left.
        Time: O(n log n), Space: O(1) - sorts in place.
        '''
        heap_size = len(self.min_heap)
        for i in reversed(range(heap_size)):
            self.min_heap[0], self.min_heap[i] = self.min_heap[i], \
                self.min_heap[0]
            self.sift_down(self.min_heap, 0, i)
        return self.min_heap


def tests():
    arr = [23, 21, 44, 52, 66, 34, 79]
    h = Heap(arr)
    print(f"MIN HEAP array represenation is: {h.min_heap}")
    print(f"MIN element in heap is {h.get_max()}")
    min = h.extract_max_priority()
    print(f"MIN item extracted is {min}")
    print("MIN HEAP array represenation after extracting max",
          f"priority item is: {h.min_heap}")
    ins = 19
    h.insert(ins)
    print(f"MIN HEAP array represenation after inserting {ins}",
          f"is: {h.min_heap}")
    print(f"HEAP IS EMPTY: {h.is_empty()}")
    rem = 2
    h.remove(rem)
    print("MIN HEAP array represenation after removing index",
          f"{rem} is: {h.min_heap}")
    print(f"sorted heap is: {h.heap_sort()}")


if __name__ == '__main__':
    tests()
    print("All Tests passed")
