'''
55. Jump Game
Medium

You are given an integer array nums. You are initially positioned
at the array's first index, and each element in the array represents
your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to
reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''


def jump_game(arr) -> bool:
    '''
    greedy algorithm. Get max reach at each step and see if you can reach
    the end just by that
    '''
    max_reach = 0
    last_index = len(arr) - 1

    for i, jump_length in enumerate(arr):
        #  If the current index `i` is
        # greater than the farthest we could have possibly reached,
        # it means we are stuck and cant proceed
        if i > max_reach:
            return False
        # Update the maximum reach if the current position offers
        # a better jump. The reach from the current position is
        # `i + jump_length`.
        max_reach = max(max_reach, i + jump_length)

        if max_reach >= last_index:
            return True

    return max_reach >= last_index


def tests():
    arr = [2, 3, 1, 1, 4]
    res = jump_game(arr)
    assert res is True
    arr = [3, 2, 1, 0, 4]
    res = jump_game(arr)
    assert res is False


tests()
