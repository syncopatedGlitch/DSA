from typing import List
import math
'''
Given an array of positive integers nums and
a positive integer target, return the minimal
length of a subarray whose sum is greater than
or equal to target. If there is no such subarray,
return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal
length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''


def min_subarray(arr: List, target: int):
    left = 0
    current_sum = 0
    length = math.inf

    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum >= target:
            length = min(length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    return length if length != math.inf else 0


def tests():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    res = min_subarray(nums, target)
    print(f"min subarray length for arr {nums}",
          f"and target {target} is {res}")
    assert res == 2
    nums = [1, 4, 4]
    target = 4
    res = min_subarray(nums, target)
    print(f"min subarray length for arr {nums}",
          f"and target {target} is {res}")
    assert res == 1
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    target = 11
    res = min_subarray(nums, target)
    print(f"min subarray length for arr {nums}",
          f"and target {target} is {res}")
    assert res == 0


tests()
