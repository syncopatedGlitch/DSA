'''
189. Rotate Array
Medium

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:

Try to come up with as many solutions as you can.
There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''


def rotate_array(arr: list, k: int) -> list:
    iteration_number = 0
    if k > len(arr):  # handle k larger than length cases.
        k = k % len(arr)
        print(f"k is {k}")
    while iteration_number < k:
        # import ipdb; ipdb.set_trace()
        var_to_move = arr[-1]
        for ind in range(len(arr) - 1, 0, -1):
            arr[ind] = arr[ind - 1]
        arr[0] = var_to_move
        iteration_number += 1
    return arr


def __reverse(arr, start, end) -> list:
    while start < end:
        arr[end], arr[start] = arr[start], arr[end]
        start += 1
        end -= 1
    return arr


def rotate_array_optimized(arr: list, k: int) -> list:
    '''
    Reverse the entire array.
    Reverse the first k elements.
    Reverse the remaining n - k elements.
    '''
    length_arr = len(arr)
    if length_arr == 0:
        return arr

    k = k % length_arr  # Normalize k

    step_1 = __reverse(arr, 0, len(arr) - 1)
    step_2 = __reverse(step_1, 0, k - 1)
    final_arr = __reverse(step_2, k, length_arr - 1)

    return final_arr


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotated_array = rotate_array(arr, k)
    print(f"rotated array is {rotated_array}")
    assert rotated_array == [5, 6, 7, 1, 2, 3, 4]
    arr = [-1, -100, 3, 99]
    k = 2
    rotated_array = rotate_array(arr, k)
    print(f"rotated array is {rotated_array}")
    assert rotated_array == [3, 99, -1, -100]

    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotated_array = rotate_array_optimized(arr, k)
    print(f"rotated array is {rotated_array}")
    assert rotated_array == [5, 6, 7, 1, 2, 3, 4]
    arr = [-1, -100, 3, 99]
    k = 2
    rotated_array = rotate_array_optimized(arr, k)
    print(f"rotated array is {rotated_array}")
    assert rotated_array == [3, 99, -1, -100]
    arr = [-1]
    k = 2
    rotated_array = rotate_array_optimized(arr, k)
    print(f"rotated array is {rotated_array}")
    assert rotated_array == [-1]
    print("All tests passed")
