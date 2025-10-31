from typing import List
'''
Given an integer array nums and an integer k,
return true if there are two distinct indices
i and j in the array such that nums[i] == nums[j]
and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

'''
Strategy 1: Using a Hash Map to Store Indices

Instead of just remembering if you've seen a number,
you need to remember where you last saw it. A hash
map is perfect for this.

The Intuition:

1. Initialize an empty hash map (a dict) to store the
   most recent index of each number you encounter.
   Let's call it last_seen_at. The mapping will be
   number -> index.
2. Iterate through the nums array, keeping track of the
   current index i and the number num.
3. For each number, check if it's already a key in your
   last_seen_at map.
    * If it is, you've found a duplicate. Now, check the
      distance. Get its last seen index,
      last_index = last_seen_at[num]. If the distance
      i - last_index is less than or equal to k, you
      have met both conditions. You can immediately
      return true.
    * Whether a duplicate was found or not, you must
      update the map with the current index:
      last_seen_at[num] = i. This is crucial because you
      always want to compare against the most recent
      occurrence to get the smallest possible distance.
4. If you finish the loop without returning, it means
   no such pair exists, so you return false.

This approach is very efficient with O(n) time complexity,
but its space complexity can be O(n) in the worst case
(if all elements are unique).

Strategy 2 (The Best Strategy): A Sliding Window of k Elements

This is a more optimized approach that realizes you only
care about a "window" of k elements at any given time.
If a duplicate exists, its partner must be within the
last k positions. Anything seen before that is irrelevant.

The Intuition:

1. Initialize an empty hash set, which will represent
   your "sliding window" of recent elements. Let's call
   it window.
2. Iterate through the nums array with index i and
   number num.
3. For each number, first check if it's already in
   the window set.
    * If it is, you've found a number that also appeared
      within the last k elements. You can immediately
      return true.
4. If it's not a duplicate, add the current number to
   the window set.
5. Now, maintain the size of the window. If the index
   i is greater than or equal to k, it means the window
   is now "full" and you need to slide it forward. You
   do this by removing the oldest element from the set,
   which is the element at index i - k.
6. If you complete the loop, return false.

This sliding window approach is generally considered the
best strategy because it's just as fast (O(n) time),
but it optimizes space. The window set will never contain
more than k elements, giving it an O(k) space complexity,
which is better than O(n) when k is smaller than n.
'''


def contains_nearby_duplicates(nums: List[int], k: int) -> bool:
    last_seen_at = {}

    for i, val in enumerate(nums):
        seen = last_seen_at.get(val, False)
        if seen is not False:
            if abs(i - seen) <= k:
                return True
        last_seen_at[val] = i
    return False


def contains_nearby_duplicates_sw(nums: List[int], k: int) -> bool:
    left = 0
    last_seen = set()
    for right, val in enumerate(nums):
        if val in last_seen:
            return True
        last_seen.add(val)
        while right - left >= k:
            last_seen.remove(nums[left])
            left += 1
    return False


def tests():
    nums = [1, 2, 3, 1]
    k = 3
    res = contains_nearby_duplicates(nums, k)
    assert res is True
    nums = [1, 0, 1, 1]
    k = 1
    res = contains_nearby_duplicates(nums, k)
    assert res is True
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    res = contains_nearby_duplicates(nums, k)
    assert res is False
    nums = [1, 2, 3, 1]
    k = 3
    res = contains_nearby_duplicates_sw(nums, k)
    assert res is True
    nums = [1, 0, 1, 1]
    k = 1
    res = contains_nearby_duplicates_sw(nums, k)
    assert res is True
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    res = contains_nearby_duplicates_sw(nums, k)
    assert res is False


tests()
