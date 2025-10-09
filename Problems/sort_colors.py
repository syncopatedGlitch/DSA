'''
Given an array nums with n objects colored red, white,
or blue, sort them in-place so that objects of the
same color are adjacent, with the colors in the order
red, white, and blue.

We will use the integers 0, 1, and 2 to represent the
color red, white, and blue, respectively.

You must solve this problem without using the library's
sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

'''


def sort_colours(arr: list, left=0, right=None) -> list:
    if right is None:
        right = len(arr) - 1
    if left < right:
        mid = (left + right) // 2
        sort_colours(arr, left, mid)
        sort_colours(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr


def merge(arr, left, mid, right):
    left_arr = arr[left: mid + 1]
    right_arr = arr[mid + 1: right + 1]
    print(f"arr is {arr}, left arr is {left_arr}, right arr is {right_arr}")

    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
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


def sort_colors_bubblesort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def tests():
    arr = [2, 0, 2, 1, 1, 0]
    res = sort_colours(arr)
    print(f"color sorting is {res}")
    assert res == [0, 0, 1, 1, 2, 2]
    arr = [2, 0, 1]
    res = sort_colours(arr)
    print(f"color sorting for array {arr} is {res}")
    assert res == [0, 1, 2]
    arr = [2, 0, 2, 1, 1, 0]
    res = sort_colors_bubblesort(arr)
    print(f"color sorting via bubblesort is {res}")
    assert res == [0, 0, 1, 1, 2, 2]
    arr = [2, 0, 1]
    res = sort_colors_bubblesort(arr)
    print(f"color sorting via bubblesort is {res}")
    assert res == [0, 1, 2]

tests()
