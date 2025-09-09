'''
169. Majority Element
Easy
Topics
premium lock icon
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
'''
Intuition:
The problem in 1.py is to find the "majority element" in an array,
which is the element that appears more than half the time.

A clever and efficient way to solve this is to use a voting-based approach.
Imagine you're holding an election to find a candidate who has more than
half the votes.

Think of it like this: you pick a candidate from the array and start a
counter for them at 1. As you go through the rest of the array, if you
see the same candidate, you increment their vote count.
If you see a different candidate, you decrement the count.

If the counter ever drops to zero, it means the current candidate has been
"outvoted" by other elements. At that point, you switch your support to
the new element you're looking at and reset the counter to 1.

You continue this process through the entire array. Because the majority
element appears more than half the time, it will always end up as the final
candidate with a positive vote count, no matter how the votes fluctuate.
The element that remains as your candidate at the very end
is the majority element.
'''


def majority_element(arr: list) -> int:
    count = 1
    element = arr[0]
    for item in arr[1:len(arr)]:
        if item == element:
            count += 1
        if item != element:
            count -= 1
        if count == 0:
            element = item
            count = 1
    print(f"count for majority element is {count}")
    return element


if __name__ == '__main__':
    arr = [3, 2, 3]
    print(f"majority element is: {majority_element(arr)}")
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(f"majority element is: {majority_element(arr)}")
    arr = [4, 3, 3, 1, 4, 4, 4, 4]
    print(f"majority element is: {majority_element(arr)}")
    arr = [42, 45, 42, 45, 42, 45, 45]
    print(f"majority element is: {majority_element(arr)}")
