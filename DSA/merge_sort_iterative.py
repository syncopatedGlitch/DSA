
def merge_sort_iterative(arr: list):
    """
    Iterative merge sort using bottom-up approach - builds sorted subarrays from smallest to largest.

    CONCEPT:
    Instead of recursively dividing the array, this approach starts with the smallest possible
    sorted subarrays (size 1) and progressively merges them into larger sorted subarrays.
    Each iteration doubles the subarray size until the entire array is sorted.

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
    # Start with subarray of size 1 and then double at the end of each iteration.
    size = 1
    while size < n:
        left = 0
        # The n - 1 is essentially asking: "Is there room for at least one more element after the current position?"
        # If yes, we might have a pair to merge. If no, we're done with this level.
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
            # This gives us right = 2, which means we'd try to include index 2 in our second chunk. But our second chunk
            # should only be index 1!
            right = min(left + (2 * size) - 1, n - 1)  # min with n-1 keeps within array bounds
            mid = min(left + size - 1, n - 1)

            if mid < right:
                merge(arr, left, mid, right)
            left += size * 2
        size *= 2
    return arr


def merge(arr, left, mid, right):
    """
    Merges two adjacent sorted subarrays within the main array.

    Takes array indices defining two sorted subarrays:
    - First subarray: arr[left:mid+1]
    - Second subarray: arr[mid+1:right+1]

    Creates temporary copies, compares elements from front of each subarray,
    places smaller element back into original array position.
    Handles remaining elements when one subarray is exhausted.

    This is the same merge logic used in recursive merge sort.
    """
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0  # set pointers for left and right arrays
    k = left  # pointer for the main array

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
    arr = [23, 56, 10, 32, 16, 8, 11]
    print(f"sorted array is: {merge_sort_iterative(arr)}")
