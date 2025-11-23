from typing import List
'''
What It Is

Kadane's Algorithm is an efficient dynamic programming
algorithm that solves the Maximum Subarray Problem -
finding the contiguous subarray within a one-dimensional
numeric array that has the largest sum.

Time Complexity: O(n) - single pass through the array
Space Complexity: O(1) - only uses a few variables

---------------------------------------------------------

Use Cases

    - Financial Analysis: Finding the best time period
      for maximum profit/revenue
    - Image Processing: Identifying regions with maximum
      brightness or contrast
    - Data Analysis: Finding time windows with maximum
      activity or growth
    - Interview Questions: One of the most common
      array-based coding problems
    - Foundation for 2D problems: Maximum sum rectangle
      in a matrix

---------------------------------------------------------

Core Intuition

The algorithm is built on a simple but powerful insight:

    At each position, you face a choice: Should I extend
    the existing subarray or start fresh from here?

Key Principle:

    - If adding the current element to the previous
      subarray gives a negative or worse result, it's
      better to start a new subarray from the current
      position.
    - Otherwise, extend the existing subarray.

The Magic Question at Each Step:

    current_sum + arr[i]  vs  arr[i]
        ^                      ^
    (extend)              (start fresh)

If the running sum becomes negative, it will only drag
down future elements, so we reset.
'''

'''
Given an integer array nums, find the subarray with the
largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        global_max = nums[0]
        current_start, global_start, global_end = 0, 0, 0
        for i in range(1, len(nums)):
            if nums[i] > current_max + nums[i]:
                current_max = nums[i]
                current_start = i
            else:
                current_max = current_max + nums[i]
            if current_max > global_max:
                global_max = current_max
                global_start = current_start
                global_end = i
        max_subarray = nums[global_start:global_end + 1]
        print(f"max subarray is {max_subarray}")
        return global_max


def tests():
    sol = Solution()

    # Example 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6
    result1 = sol.maxSubArray(nums1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Test Case 1 Passed.")

    # Example 2
    nums2 = [1]
    expected2 = 1
    result2 = sol.maxSubArray(nums2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Test Case 2 Passed.")

    # Example 3
    nums3 = [5, 4, -1, 7, 8]
    expected3 = 23
    result3 = sol.maxSubArray(nums3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Test Case 3 Passed.")


if __name__ == "__main__":
    tests()
