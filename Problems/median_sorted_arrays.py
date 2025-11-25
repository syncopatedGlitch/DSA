'''
4. Median of Two Sorted Arrays
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n
respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is
(2 + 3) / 2 = 2.5.
'''


import math


def find_median_sorted_arrays(arr1: list, arr2: list) -> float:
    '''
    merge the two sorted arrays and return the median
    '''
    # merge two sorted arrays using two pointer approach
    final_array = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            final_array.append(arr1[i])
            i += 1
        else:
            final_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        final_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        final_array.append(arr2[j])
        j += 1

    print(f"final merged array is {final_array}")
    mid = len(final_array) // 2
    if (len(final_array) % 2) == 0:
        # if length of array is even
        median = (final_array[mid - 1] + final_array[mid]) / 2
        print(f"median of {final_array} is {median}")
        return median
    else:
        # if length of array is odd
        median = float(final_array[mid])
        print(f"median of {final_array} is {median}")
        return median


def find_median_sorted_array_optimised(arr1, arr2) -> float:
    '''
    Imagine the final merged array. The median is the element
    (or average of two elements) that splits the array into
    two equal halves. Our goal is to find this split without
    actually creating the merged array.
    We can do this by partitioning both arrays (arr1 and arr2)
    such that:
        . The total number of elements in the left parts of
        both partitions equals the total number of elements
        in the right parts.
        . Every element in the combined left part is less than
        or equal to every element in the combined right part.
    If we find such a partition, the median can be calculated
    directly from the boundary elements.

    Let's say we partition arr1 at index partitionX and arr2 at
    index partitionY.

    . maxLeftX: The largest element in the left part of arr1.
    . minRightX: The smallest element in the right part of arr1.
    . maxLeftY: The largest element in the left part of arr2.
    . minRightY: The smallest element in the right part of arr2.
    The perfect partition is found when:
    maxLeftX <= minRightY and maxLeftY <= minRightX.
    Instead of searching for two partitions, we can binary search
    for the partition in the smaller array (let's say arr1).
    Once we choose a partition in arr1, the corresponding
    partition in arr2 is automatically determined to keep
    the halves equal.

    Ensure arr1 is the smaller array to optimize the search space.
    Use binary search on arr1 (from low = 0 to high = len(arr1)).
    In each step, pick a partitionX for arr1. Calculate the
    corresponding partitionY for arr2.
    Check if the boundary elements satisfy the median condition
    (maxLeftX <= minRightY).
    If they do, we've found our median.
    If the total length is even, the median is
    (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.
    If the total length is odd, the median is
    max(maxLeftX, maxLeftY).
    If maxLeftX > minRightY, our partition in arr1 is too far
    to the right. We need to search in the left half
    (high = partitionX - 1).
    If maxLeftX < minRightY, our partition in arr1 is too far
    to the left. We need to search in the right half
    (low = partitionX + 1).
    Repeat until the correct partition is found.
    '''
    if len(arr1) > len(arr2):
        arr2, arr1 = arr1, arr2

    m, n = len(arr1), len(arr2)
    # The search space for the partition is the
    # inclusive range [0, m].
    # `high` is set to `m`, not `m-1`.
    low, high = 0, m

    while low <= high:
        partition_x = (low + high) // 2
        # partition on the second array would be:
        # total length of combined array divided by 2, minus
        # the number of elements already in left partition of arr1
        partition_y = (m + n + 1) // 2 - partition_x

        max_left_x = arr1[partition_x - 1] if partition_x != 0 else -math.inf
        min_right_x = arr1[partition_x] if partition_x != m else math.inf
        max_left_y = arr2[partition_y - 1] if partition_y != 0 else -math.inf
        min_right_y = arr2[partition_y] if partition_y != n else math.inf

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (m + n) % 2 == 0:
                return (
                    max(max_left_x, max_left_y)
                    + min(min_right_x, min_right_y)
                    ) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1
    raise ValueError("Input arrays are not sorted")


def tests():
    nums1 = [1, 3]
    nums2 = [2]
    res = find_median_sorted_array_optimised(nums1, nums2)
    print(f"result for arrays {nums1} and {nums2} is {res}")
    assert res == float(2)
    nums1 = [1, 2]
    nums2 = [3, 4]
    res = find_median_sorted_array_optimised(nums1, nums2)
    print(f"result for arrays {nums1} and {nums2} is {res}")
    assert res == float((3 + 2) / 2)
    nums1 = [1, 5, 7, 9]
    nums2 = [2, 3, 4, 6, 8, 10]
    res = find_median_sorted_array_optimised(nums1, nums2)
    print(f"result for arrays {nums1} and {nums2} is {res}")
    assert res == float((5 + 6) / 2)


tests()
