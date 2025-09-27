"""
Insertion Sort Algorithm

Insertion sort builds the final sorted array one element at a time by
repeatedly taking an element from the unsorted portion and inserting
it into its correct position within the already sorted portion.

Algorithm Intuition:
- Similar to how you sort playing cards in your hand
- Start with the second element (assume first is already "sorted")
- Compare current element with elements to its left
- Shift larger elements one position right to make space
- Insert current element in the correct position
- Repeat until all elements are processed

Time Complexity:
- Best Case: O(n) - when array is already sorted
- Average Case: O(n²) - random order
- Worst Case: O(n²) - when array is reverse sorted

Space Complexity: O(1) - sorts in-place

Key Characteristics:
- Stable: maintains relative order of equal elements
- In-place: requires only O(1) additional memory
- Adaptive: performs better on partially sorted arrays
- Online: can sort elements as they arrive

Best suited for:
- Small datasets (typically n < 50)
- Nearly sorted arrays
- As a subroutine in hybrid algorithms (e.g., Timsort)

Example (step-by-step sorting):

Given array: [5, 2, 4, 6, 1, 3]

Step 1: [5, 2, 4, 6, 1, 3]  # 5 is sorted
Step 2: [2, 5, 4, 6, 1, 3]  # Insert 2 before 5
Step 3: [2, 4, 5, 6, 1, 3]  # Insert 4 between 2 and 5
Step 4: [2, 4, 5, 6, 1, 3]  # 6 is already in correct position
Step 5: [1, 2, 4, 5, 6, 3]  # Insert 1 at the beginning
Step 6: [1, 2, 3, 4, 5, 6]  # Insert 3 between 2 and 4

Final sorted array: [1, 2, 3, 4, 5, 6]
"""


def binary_search_insertion_pos(arr, key, end):
    """Find the correct insertion position using binary search"""
    left, right = 0, end

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > key:
            right = mid
        else:
            left = mid + 1

    return left


def insertion_sort(inp_list: list) -> list:
    # range starts from 1 because 0th position (single) element
    # is already sorted by defintion
    for i in range(1, len(inp_list)):
        key = inp_list[i]

        # Find insertion position using binary search
        pos = binary_search_insertion_pos(inp_list, key, i)

        # Shift elements from pos to i-1 one position right
        for j in range(i, pos, -1):
            inp_list[j] = inp_list[j - 1]

        # Insert the key at its correct position
        inp_list[pos] = key
    print(inp_list)
    return inp_list


if __name__ == '__main__':
    insertion_sort([4, 1, 23, 45, 32, 21, 9])
    # Test with more examples
    insertion_sort([64, 34, 25, 12, 22, 11, 90])
    insertion_sort([5, 2, 4, 6, 1, 3])
