"""
Subarrays with Given Sum and Bounded Maximum
Given an integer array nums and integers k and M,
count the number of contiguous subarrays whose
sum equals k and whose maximum element is at most M.

Example

Input

nums = [2, -1, 2, 1, -2, 3]
k = 3
M = 2
Output

2
Explanation

We need subarrays with sum = 3 and all elements ≤ 2.
Also, any subarray containing 3 is invalid because
3 > M. Check all starts:

- From index 0: [2, -1, 2] → sum = 3, max = 2 → valid (count = 1).
- From index 2: [2, 1] → sum = 3, max = 2 → valid (count = 2).
No other subarray qualifies. Thus the total count is 2.
"""
'''
The Combined O(n) Algorithm

  Putting it all together, here is the efficient, two-part algorithm:

   1. Split the Array:
      Iterate through the main nums array. Whenever you encounter a number > M, consider
  the block of numbers you've seen since the last "breaker". This gives you one or more
  smaller arrays to work on.

   2. Solve for Each Block:
      For each of these smaller blocks, apply the prefix sum algorithm:
       * Initialize count = 0, current_sum = 0.
       * Initialize a hash map prefix_sum_counts with {0: 1}. This is a crucial step to
         count subarrays that start from the beginning of the block.
       * Iterate through the numbers in the block:
           * Add the number to current_sum.
           * Calculate the needed_sum = current_sum - k.
           * If needed_sum exists in prefix_sum_counts, it means we've found
             prefix_sum_counts[needed_sum] new subarrays that end at the current position
             and sum to k. Add this to your count for the block.
           * Increment the count for the current_sum in the hash map.

   3. Sum the Results:
      The total answer is the sum of the counts from each independent block.

  This approach processes each element of the array a constant number of times, leading
  to an overall O(n) time complexity, which is efficient enough to pass the given
  constraints.

> lets walk through this with an example please. i got part of it, but didnt understand
  the relevance of hash map here

  Of course! It's a powerful technique, and walking through an example is the best way to
  see why the hash map is not just relevant, but the key to an efficient solution.

  Let's use a simple example.
   * nums = [3, 4, -1, 1, 7]
   * k = 7

  Our goal is to find subarrays that sum to 7. Manually, we can see them: [3, 4], [3, 4,
  -1, 1], [7], and [-1, 1, 7]. The answer should be 4.

  The Core Idea: Prefix Sums

  The sum of any subarray nums[j...i] can be found by taking the total sum up to i and
  subtracting the total sum up to j-1.

  sum(j..i) = (sum up to i) - (sum up to j-1)

  We want this to be equal to k:
  k = (sum up to i) - (sum up to j-1)

  If we rearrange this equation, we get the magic formula:
  (sum up to j-1) = (sum up to i) - k

  This tells us: as we iterate through the array and calculate our current_sum (the sum
  up to i), we just need to look back and see if we've ever encountered a previous prefix
  sum that equals our current_sum - k.

  Why a Hash Map? The "Memory" Problem

  As we iterate, how do we "look back" efficiently?

  Imagine we are at index i=3 (num = 1). Our current_sum is 3 + 4 - 1 + 1 = 7.
  The formula tells us to look for a previous prefix sum of current_sum - k = 7 - 7 = 0.
  Without a hash map, we'd have to loop through all previous prefix sums [3, 7, 6] to see
  if any of them are 0. This would be slow, leading to an O(n²) solution.                ▄
                                                                                         ▀
  The hash map solves this by acting as an instantaneous memory. It stores every prefix
  sum we've seen and how many times we've seen it. Instead of looping back, we just do a
  single, fast O(1) lookup in the map.

  Walkthrough with the Hash Map

  Let's trace our example.
  nums = [3, 4, -1, 1, 7], k = 7

  Initialization:
   * count = 0
   * current_sum = 0
   * prefix_map = {0: 1} (We initialize with a sum of 0 having occurred once, to account
     for subarrays that start from the very beginning).

  ---
  Step 1: `num = 3`
   * current_sum becomes 0 + 3 = 3.
   * We need to find a previous sum of current_sum - k = 3 - 7 = -4.
   * Is -4 in our prefix_map? No.
   * Add current_sum (3) to the map: prefix_map is now {0: 1, 3: 1}.

  ---
  Step 2: `num = 4`
   * current_sum becomes 3 + 4 = 7.
   * We need current_sum - k = 7 - 7 = 0.
   * Is 0 in our prefix_map? Yes! It occurred 1 time.
   * This means we found 1 subarray ending here that sums to 7. (It's [3, 4]).
   * count becomes 0 + 1 = 1.
   * Add current_sum (7) to the map: prefix_map is now {0: 1, 3: 1, 7: 1}.

  ---
  Step 3: `num = -1`
   * current_sum becomes 7 - 1 = 6.
   * We need current_sum - k = 6 - 7 = -1.
   * Is -1 in our prefix_map? No.
   * Add current_sum (6) to the map: prefix_map is now {0: 1, 3: 1, 7: 1, 6: 1}.

  ---
  Step 4: `num = 1`                                                                      ▄
   * current_sum becomes 6 + 1 = 7.                                                      ▀
   * We need current_sum - k = 7 - 7 = 0.
   * Is 0 in our prefix_map? Yes! It occurred 1 time.

   * This means we found 1 more subarray ending here that sums to 7. (It's [3, 4, -1,
     1]).
   * count becomes 1 + 1 = 2.
   * Add current_sum (7) to the map. We've seen 7 before, so we increment its count:
     prefix_map is now {0: 1, 3: 1, 7: 2, 6: 1}.

  ---
  Step 5: `num = 7`
   * current_sum becomes 7 + 7 = 14.
   * We need current_sum - k = 14 - 7 = 7.
   * Is 7 in our prefix_map? Yes! It occurred 2 times.
   * This means we found 2 more subarrays ending here that sum to 7. (They are [-1, 1, 7]
     and [7]).
   * count becomes 2 + 2 = 4.
   * Add current_sum (14) to the map.

  ---
  Final Result: The loop finishes, and we return count = 4.

  The hash map's relevance is that it provides an O(1) "lookup to the past," preventing
  an O(n) scan at every single step and making the entire algorithm run in O(n) time.

  
   what isthe relevance of starting the prefix_sum_map at {0:1} for subarrays starting at
  beginning of the block? Can you clarify that a bit more with a counter example that
  faces issue due to map not initialized with this value?

✦ Excellent question. This is a subtle but absolutely critical detail for the algorithm
  to work correctly. Getting this part right is what separates a working solution from a
  failing one.

  The initialization prefix_sum_map = {0: 1} serves as a base case or a "sentinel value."
  Its entire purpose is to correctly handle subarrays that start from the very beginning
  of the block (i.e., at index 0).

  Let's revisit the core formula we're using:
  sum_of_subarray(from j to i) = prefix_sum[i] - prefix_sum[j-1]

  We want the subarray sum to be k, so we are looking for cases where:
  prefix_sum[i] - k = prefix_sum[j-1]

  The Problem with Subarrays Starting at Index 0

  Now, consider a subarray that starts at index 0 and ends at index i. In this case, j=0.
  What is prefix_sum[j-1]? It would be prefix_sum[-1]. This doesn't exist in our array.

  However, what is the sum of elements before the start of the array? It's the sum of an
  empty set of numbers, which is conceptually 0.

  So, for a subarray starting at index 0 whose sum happens to be k, our current_sum at
  that point will be exactly k. The formula becomes:
  current_sum - k = k - k = 0

  The formula is telling us that to find a subarray starting at index 0 that sums to k,
  we need to look for a previous prefix sum of 0. By initializing our map with {0: 1}, we
  are telling our algorithm: "You have already seen a prefix sum of 0 one time (before
  the loop even started)."
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
        if prefix_sum_map.get(prefix_sum):
            total_count += 1
            prefix_sum_map[prefix_sum] += 1
        else:
            prefix_sum_map[prefix_sum] = 1
    return total_count


def tests():
    # Example 1
    nums1 = [2, -1, 2, 1, -2, 3]
    k1 = 3
    M1 = 2
    expected1 = 2
    result1 = countSubarraysWithSumAndMaxAtMost(nums1, k1, M1)
    assert result1 == expected1

    # Example 1
    nums2 = [5]
    k2 = 5
    M2 = 5
    expected2 = 1
    result2 = countSubarraysWithSumAndMaxAtMost(nums2, k2, M2)
    assert result2 == expected2

if __name__ == "__main__":
    tests()
