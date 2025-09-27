# MERGE SORT

def merge_sort_recursion(inp_arr: list, left=0, right=None) -> list:
    """
    Recursive merge sort using divide-and-conquer approach - splits
    array until base case, then merges back up.

    CONCEPT:
    Recursively divides the array into smaller halves until reaching
    single elements (base case), then merges the sorted halves back
    together. Uses the call stack to manage the division and merging
    process automatically.

    ALGORITHM FLOW:
    1. Check base case: if left >= right, array has 0-1 elements
       (already sorted)
    2. Find midpoint and divide array into left and right halves
    3. Recursively sort the left half completely
    4. Recursively sort the right half completely
    5. Merge the two sorted halves back together

    EXAMPLE with [38, 27, 43, 3]:
    Call Stack Visualization:
    merge_sort([38,27,43,3], 0, 3)
    ├── merge_sort([38,27], 0, 1)
    │   ├── merge_sort([38], 0, 0) → base case
    │   ├── merge_sort([27], 1, 1) → base case
    │   └── merge([38],[27]) → [27,38]
    ├── merge_sort([43,3], 2, 3)
    │   ├── merge_sort([43], 2, 2) → base case
    │   ├── merge_sort([3], 3, 3) → base case
    │   └── merge([43],[3]) → [3,43]
    └── merge([27,38],[3,43]) → [3,27,38,43]

    RECURSION PATTERN:
    - Divide phase: Split array until single elements
    - Conquer phase: Base case (single elements are sorted)
    - Combine phase: Merge sorted subarrays back up the call stack

    PARAMETERS:
    - arr: The array being sorted (modified in-place)
    - left: Starting index of current subarray (default 0)
    - right: Ending index of current subarray (default len(arr)-1)
    - mid: Calculated midpoint for splitting (left + right) // 2

    ADVANTAGES:
    - Intuitive divide-and-conquer logic
    - Clean recursive structure matches algorithm description
    - Call stack automatically manages subarray coordination

    LIMITATIONS:
    - Stack overflow risk with very large arrays
    - Recursive overhead in function calls
    """
    if right is None:
        right = len(inp_arr) - 1

    if left < right:
        mid = (left + right) // 2
        merge_sort_recursion(inp_arr, left, mid)
        merge_sort_recursion(inp_arr, mid + 1, right)
        merge(inp_arr, left, mid, right)
    return inp_arr


def merge_sort_iterative(arr: list):
    """
    Iterative merge sort using bottom-up approach - builds sorted
    subarrays from smallest to largest.
    ### The Systematic Growth Pattern

    The key insight is that you can control the growth systematically
    by doubling the size of what you're working with at each level:

    Level 1: Work with chunks of size 1 (individual elements)
    • Every single element is already a "sorted array"
    • Merge adjacent pairs: element 0 with element 1, element 2 with
      element 3, etc.
    • Result: You now have sorted chunks of size 2

    Level 2: Work with chunks of size 2
    • Take the sorted pairs from Level 1
    • Merge adjacent pairs of these 2-element sorted chunks
    • Result: You now have sorted chunks of size 4

    Level 3: Work with chunks of size 4
    • Take the sorted 4-element chunks from Level 2
    • Merge adjacent pairs of these chunks
    • Result: You now have sorted chunks of size 8

    Continue this pattern until your chunk size equals or
    exceeds the array length.

    ALGORITHM FLOW:
    1. Start with subarray size = 1 (every single element is "sorted")
    2. Merge adjacent pairs of subarrays of current size
    3. Double the subarray size for next iteration
    4. Repeat until subarray size >= array length

    EXAMPLE with [38, 27, 43, 3]:
    - Size 1: Merge [38],[27] → [27,38] and [43],[3] → [3,43]
    Result: [27, 38, 3, 43]
    - Size 2: Merge [27,38],[3,43] → [3,27,38,43]
    Result: [3, 27, 38, 43] - DONE

    ADVANTAGES:
    - No recursion depth limits (no stack overflow)
    - Same O(n log n) time complexity as recursive version
    - More predictable memory usage pattern
    - Easier to understand the merge progression visually

    VARIABLES:
    - size: Current subarray size being merged (1, 2, 4, 8, ...)
    - left: Starting index of current merge operation
    - mid: End of first subarray (left + size - 1)
    - right: End of second subarray (left + 2*size - 1)
    """
    n = len(arr)
    if n <= 1:
        return arr
    # Start with subarray of size 1 and then double at the end of
    # each iteration.
    size = 1
    while size < n:
        left = 0
        # The n - 1 is essentially asking: "Is there room for at
        # least one more element after the current position?"
        # If yes, we might have a pair to merge. If no, we're done
        # with this level.
        while left < n - 1:
            # why right is left + (2 * size) - 1 and not left + (2 * size).
            # Example
            # Array: [64, 34, 25, 12, 22, 11] (indices 0, 1, 2, 3, 4, 5)
            # Level 1 (size = 1), left = 0:
            # What we want:
            # • First chunk: 1 element starting at index 0 → index 0 only
            # • Second chunk: 1 element starting at index 1 → index 1 only
            # • So right should be 1 (the last index of second chunk)
            # With left + 2 * size:
            # right = left + 2 * size
            #     = 0 + 2 * 1
            #     = 2
            # This gives us right = 2, which means we'd try to include index 2
            # in our second chunk. But our second chunk
            # should only be index 1!
            right = min(left + (2 * size) - 1, n - 1)
            # min with n-1 keeps within array bounds
            mid = min(left + size - 1, n - 1)

            if mid < right:
                merge(arr, left, mid, right)
            left += size * 2
        size *= 2
    return arr


def merge(arr, left, mid, right) -> list:
    """
    Merges two adjacent sorted subarrays back into the original array.

    Called after both left and right subarrays have been recursively sorted.
    Creates temporary arrays for the two sorted halves, then merges them back
    into the original array positions by comparing front elements.

    PARAMETERS:
    - arr: Original array being modified
    - left: Start index of first sorted subarray
    - mid: End index of first subarray (start of second is mid+1)
    - right: End index of second sorted subarray

    The two subarrays being merged are:
    - Left: arr[left:mid+1] (already sorted by recursion)
    - Right: arr[mid+1:right+1] (already sorted by recursion)
    """
    # Create temp arrays for left and right subarray
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0  # Pointers for left_arr and right_arr
    k = left   # Pointer for main array

    # Merge the two arrays
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # copy remaining elements
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr = [38, 27, 43, 3]
    print(f"sorted array is: {merge_sort_recursion(arr)}")
    arr = [23, 56, 10, 32, 16, 8, 11]
    print(f"sorted array is: {merge_sort_iterative(arr)}")
