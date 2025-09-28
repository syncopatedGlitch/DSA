'''
Quicksort is based on the "divide and conquer" strategy with a
brilliant insight: if you can place one element in its correct
final position, you can split the problem into two smaller,
independent subproblems.

The Core Insight: Partitioning
Pick any element (called the "pivot") and rearrange the array so that:
• All elements smaller than the pivot are to its left
• All elements larger than the pivot are to its right
• The pivot is now in its correct final sorted position

Why This Works:
Once you've partitioned around a pivot, you know that pivot will never
need to move again. Everything to its left belongs there, everything to
its right belongs there. Now you have two smaller sorting problems
that are completely independent.

The Partitioning Process:
Think of it like organizing a classroom by height, but you only know
one person's height (the pivot). You ask everyone shorter to move to
the left side, everyone taller to the right side. That person is now in
their correct position, and you can organize each side separately.

Key Advantages:
1. In-place: Unlike merge sort, you don't need extra memory for merging
2. Cache-friendly: Works on contiguous memory segments
3. Average case efficiency: O(n log n) because each level of recursion
processes all n elements, and there are typically log n levels
'''


def quick_sort_recursive(arr: list, low=0, high=None) -> list:
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_recursive(arr, low, pivot_index - 1)
        quick_sort_recursive(arr, pivot_index + 1, high)
    return arr


def partition(arr, i, j):
    '''
    Choses a pivot and partitions the array such that the elements
    on the left of pivot are smaller and elements on the right of
    pivot are greater than the pivot.
    '''
    '''
    The Problem with i < j:

    In the broken version i < j:
    1. Start with [10, 40, 80, 30], pivot = 10, i = 1, j = 3
    2. The inner while loop while i < j and arr[j] >= pivot tries to
       find an element smaller than 10
    3. It checks j=3 (30 >= 10), j=2 (80 >= 10), but stops at j=1
       because now i == j (both are 1)
    4. Critical issue: It never checks if arr[1] = 40 should be moved!
    5. The pivot (10) gets swapped with arr[1] = 40, putting 40 in the
       wrong position

    Why i <= j fixes it:

    In the fixed version, i <= j:
    1. Same start, but when i=1 and j=1, the condition i <= j allows
       one more iteration.
    2. It properly checks arr[1] = 40, sees that 40 >= 10, so j
       decrements to 0
    3. Now j points to the correct position (index 0) where the pivot belongs
    4. The pivot stays in its correct position

    The key insight: When i == j, you still need to check that position
    to see if it belongs on the left or
    right side of the pivot. The i < j condition stops too early and misses
    this crucial check.
    '''
    low = i
    pivot = arr[i]
    while i <= j:
        # increment i and skip over elements until
        # we find an element larger than pivot
        while i <= j and arr[i] <= pivot:
            i += 1
        # decrement j and skip over elements until
        # we find an element smaller than pivot
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # loop will end when i > j
    arr[low], arr[j] = arr[j], arr[low]
    return j


if __name__ == '__main__':
    arr = [10, 40, 80, 30, 50, 70, 90]
    print(f"sorted array is: {quick_sort_recursive(arr)}")
    arr = [1, 1, 2, 3, 2, 1, 2, 1]
    print(f"sorted array is: {quick_sort_recursive(arr)}")
