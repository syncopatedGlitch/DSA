'''
Given an integer array nums and integers k and M, count the number of contiguous subarrays whose sum equals k and whose maximum element is at most M.

Example

Input

nums = [2, -1, 2, 1, -2, 3]
k = 3
M = 2
Output

2
Explanation

We need subarrays with sum = 3 and all elements ≤ 2. 
Also, any subarray containing 3 is invalid because 3 > M. Check all starts:

- From index 0: [2, -1, 2] → sum = 3, max = 2 → valid (count = 1).
- From index 2: [2, 1] → sum = 3, max = 2 → valid (count = 2). No other subarray qualifies. Thus the total count is 2.
'''

'''
1. Prefix Sum for Subarray Sum Problem

The classic problem: "Find subarrays with sum = k"
Key Insight: If we have:

    - prefix_sum[j] = sum from index 0 to j
    - prefix_sum[i] = sum from index 0 to i (where i < j)

Then: subarray sum from (i+1) to j = prefix_sum[j] - prefix_sum[i]

So if we want subarray sum = k:

    prefix_sum[j] - prefix_sum[i] = k
    prefix_sum[i] = prefix_sum[j] - k

Strategy: As we iterate, for each position j:

    - Calculate current_sum (prefix sum up to j)
    - Check if (current_sum - k) exists in our map
    - If yes, we found subarray(s) with sum = k ending at position j

2. Handling Maximum Constraint (M)

Any element > M breaks the validity of all subarrays containing it.

Strategy: Treat elements > M as "reset points"

    - When we hit nums[i] > M, reset everything
    - This ensures we only count subarrays between reset points
'''


def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    # overall count
    total_count = 0
    # subarray sum problem specific variables.
    current_sum = 0
    prefix_sum_map = {0: 1}
    for i in range(len(nums)):
        # if current element is greater than upper
        # bound, its a breaker point and can never be
        # part of a valid subarray, so reset the
        # subarray sum problem variables completely
        # and start from next element after this one.
        if nums[i] > M:
            current_sum = 0
            prefix_sum_map = {0: 1}
            continue
        current_sum += nums[i]
        prefix_sum = current_sum - k
        if prefix_sum in prefix_sum_map:
            total_count += prefix_sum_map[prefix_sum]  # Add the count

        # Then update the current_sum in map
        if current_sum in prefix_sum_map:
            prefix_sum_map[current_sum] += 1
        else:
            prefix_sum_map[current_sum] = 1
    return total_count

