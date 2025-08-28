# MERGE SORT

def merge_sort(inp_arr: list, left=0, right=None) -> list:
    """
    Recursive merge sort using divide-and-conquer approach - splits array until base case, then merges back up.

    CONCEPT:
    Recursively divides the array into smaller halves until reaching single elements (base case),
    then merges the sorted halves back together. Uses the call stack to manage the division
    and merging process automatically.

    ALGORITHM FLOW:
    1. Check base case: if left >= right, array has 0-1 elements (already sorted)
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
        merge_sort(inp_arr, left, mid)
        merge_sort(inp_arr, mid + 1, right)
        merge(inp_arr, left, mid, right)
    return inp_arr


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
    print(f"sorted array is: {merge_sort(arr)}")
