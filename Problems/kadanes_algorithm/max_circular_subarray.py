from typing import List
'''
Given a circular integer array nums of length n,
return the maximum possible sum of a non-empty
subarray of nums.

A circular array means the end of the array connects
to the beginning of the array. Formally, the next
element of nums[i] is nums[(i + 1) % n] and the
previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed
buffer nums at most once. Formally, for a subarray
nums[i], nums[i + 1], ..., nums[j], there does not
exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
'''
'''
The Core Idea: Two Competing Cases

In a circular array, the subarray with the maximum sum
can be one of two types:

Case 1: The subarray is non-wrapping (a standard
        contiguous block).
This is the simple case. The subarray lies somewhere
in the middle of the array, just like in a normal,
non-circular array.
* Example: In [1, -10, 5, 6, -2], the maximum subarray
is [5, 6] with a sum of 11.

Case 2: The subarray is "wrapping".

This is the new, tricky case. The subarray consists of
elements from the end of the array wrapped around to
connect with elements from the beginning.
* Example: In [10, -2, -3, 5], the maximum subarray is
[5, 10] with a sum of 15.

The final answer will be the larger of the results
from these two cases.

How to Solve Each Case

Solving Case 1: The Non-Wrapping Maximum

This is straightforward. We can find the maximum sum for
any non-wrapping subarray by simply running the standard
Kadane's algorithm on the array. Let's call this result
max_kadane_sum.

Solving Case 2: The Wrapping Maximum

This is where the clever insight comes in.

Think about what a wrapping subarray means. If the
maximum sum comes from a wrapping subarray
(elements at the end + elements at the start),
then the elements not included in this subarray form a
contiguous block in the middle.

As you can see from the diagram, the sum of the wrapping
subarray is:

Sum(Wrapping Subarray) = Total Sum of the Array
- Sum(Middle Non-Included Subarray)

To make the Sum(Wrapping Subarray) as large as possible,
we need to make the Sum(Middle Non-Included Subarray) as
small as possible.
So, the problem of finding the maximum wrapping sum
transforms into finding the minimum contiguous subarray
sum and subtracting it from the total sum of the array.

How do we find the minimum subarray sum using Kadane's?

Kadane's algorithm is designed to find the maximum
subarray sum. We can cleverly adapt it to find the minimum
by:
1. Inverting the sign of every number in the array.
2. Running the standard Kadane's algorithm on this new,
inverted array. This will give us the "maximum" sum of the
inverted numbers.
3. The minimum sum of the original array is simply the
negative of this result.

So, min_subarray_sum = - (Kadane's on the inverted array).

Once we have that, we can find the maximum wrapping sum:
max_wrapping_sum = total_sum - min_subarray_sum

Putting It All Together: The Full Algorithm

1. Calculate `max_kadane_sum`: Run the standard Kadane's
algorithm on the original array.

2. Calculate `max_wrapping_sum`:
    a. Calculate the total_sum of the array.
    b. Find the min_subarray_sum by inverting the array's
       signs and running Kadane's.(or just use min instead of max
       in the same algo)
    c. Calculate max_wrapping_sum = total_sum - min_subarray_sum.

3. Handle the Edge Case: There's one special case. What if
   all the numbers in the array are negative (e.g., [-1, -2, -3])?
    * max_kadane_sum will correctly be -1.
    * total_sum will be -6.
    * min_subarray_sum will be the entire array, which is -6.
    * max_wrapping_sum would be total_sum - min_subarray_sum
      = -6 - (-6) = 0.
    * The final answer would be max(-1, 0) = 0. This is wrong!
      The answer should be -1. The 0 represents an empty subarray,
      which isn't allowed. This edge case happens only when the
      minimum subarray is the entire array itself (i.e., when
      all numbers are negative).
    * The Fix: If max_kadane_sum is less than 0, it means all
      numbers are negative. In this situation, the wrapping
      case is irrelevant, and the answer must be max_kadane_sum
4. Final Result:
    * If max_kadane_sum < 0, return max_kadane_sum.
    * Otherwise, return max(max_kadane_sum, max_wrapping_sum).

Optimization:
Current solution iterates through the array three separate times:
   1. Once in max_kadane() to find the max subarray sum.
   2. Once in min_kadane() to find the min subarray sum.
   3. Once implicitly with sum(nums) to get the total sum.

  The optimization is to combine all three of these passes into a single pass.
'''


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        self.nums = nums
        max_kadane_sum = self.max_kadane()
        total_sum = sum(nums)
        min_subarray_sum = self.min_kadane()
        max_wrapping_sum = total_sum - min_subarray_sum

        if max_kadane_sum < 0:
            return max_kadane_sum
        return max(max_wrapping_sum, max_kadane_sum)

    def max_kadane(self):
        current_max = self.nums[0]
        global_max = self.nums[0]
        for i in range(1, len(self.nums)):
            current_max = max(self.nums[i], current_max + self.nums[i])
            global_max = max(current_max, global_max)
        return global_max

    def min_kadane(self):
        current_min = self.nums[0]
        global_min = self.nums[0]
        for i in range(1, len(self.nums)):
            current_min = min(self.nums[i], current_min + self.nums[i])
            global_min = min(current_min, global_min)
        return global_min


class OptimizedSolution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = nums[0]
        current_max, global_max = nums[0], nums[0]
        current_min, global_min = nums[0], nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            global_max = max(current_max, global_max)
            current_min = min(nums[i], current_min + nums[i])
            global_min = min(current_min, global_min)
            total_sum += nums[i]
        max_wrapping_sum = total_sum - global_min
        if global_max < 0:
            return global_max
        return max(max_wrapping_sum, global_max)

def tests():
    sol = Solution()

    # Example 1
    nums1 = [1, -2, 3, -2]
    expected1 = 3
    result1 = sol.maxSubarraySumCircular(nums1)
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, got {result1}"
    print("Test Case 1 Passed.")

    # Example 2
    nums2 = [5, -3, 5]
    expected2 = 10
    result2 = sol.maxSubarraySumCircular(nums2)
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, got {result2}"
    print("Test Case 2 Passed.")

    # Example 3
    nums3 = [-3, -2, -3]
    expected3 = -2
    result3 = sol.maxSubarraySumCircular(nums3)
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, got {result3}"
    print("Test Case 3 Passed.")
    pass


if __name__ == "__main__":
    tests()
