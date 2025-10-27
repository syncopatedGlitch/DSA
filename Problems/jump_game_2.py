from typing import List

'''
You are given a 0-indexed array of integers nums of
length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a
forward jump from index i. In other words, if you are at
index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1.
The test cases are generated such that you can
reach index n - 1.


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the
last index is 2. Jump 1 step from index 0 to 1, then 3
steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
'''


def jump(nums: List[int]) -> int:
    last_index = len(nums) - 1
    if last_index == 0:
        return 0
    jumps = 0
    # farthest you can get with current number of jumps
    current_end = 0
    # farthest you can get from any position within
    # current jump window
    farthest = 0
    # We only need to iterate up to the second to last element.
    # If we are at the last element, we don't need to jump anymore.
    for i in range(last_index):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


def tests():
    nums = [1, 2, 1, 1, 1]
    res = jump(nums)
    assert res == 3
    nums = [2, 3, 1, 1, 4]
    res = jump(nums)
    assert res == 2
    nums = [2, 1]
    res = jump(nums)
    assert res == 1
    nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
    res = jump(nums)
    print(f"res is {res}")
    assert res == 2


tests()
