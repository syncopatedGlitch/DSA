'''
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique
element appears at most twice. The relative order of the
elements should be kept the same.

Return k after placing the final result in the first k
slots of nums.

Do not allocate extra space for another array. You must do
this by modifying the input array in-place with O(1)
extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the
first five elements of nums being 1, 1, 2, 2 and 3
respectively.
It does not matter what you leave beyond the returned k
(hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the
first seven elements of nums being 0, 0, 1, 1, 2, 3 and
3 respectively.
It does not matter what you leave beyond the returned k
(hence they are underscores).
'''

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    # first two positions are always included
    # as there is nothing to compare them against
    ind = 2
    for i in range(2, len(nums)):
        if nums[i] == nums[ind - 2]:
            continue
        else:
            nums[ind] = nums[i]
            ind += 1
    return ind


def tests():
    inp = [1, 1, 1, 2, 2, 3]
    res = remove_duplicates(inp)
    assert res == 5


tests()
