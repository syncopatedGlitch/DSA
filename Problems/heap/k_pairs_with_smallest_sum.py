from typing import List
import heapq
'''
You are given two integer arrays nums1 and nums2 sorted
in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from
the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk)
with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the
sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
'''
'''
A very effective way to think about this problem is to imagine
you have m sorted lists of sums (where m is the length of nums1).

* List 1: [nums1[0]+nums2[0], nums1[0]+nums2[1], nums1[0]+nums2[2], ...]
* List 2: [nums1[1]+nums2[0], nums1[1]+nums2[1], nums1[1]+nums2[2], ...]
* List 3: [nums1[2]+nums2[0], nums1[2]+nums2[1], nums1[2]+nums2[2], ...]
* ...and so on.
Your goal is to find the k smallest numbers from all these lists
combined. This is a classic problem that can be solved efficiently
with a min-heap (or priority queue).

Here is the intuition for the heap-based approach:

1. Initialization: The smallest possible sums must come from
   pairing elements from nums1 with nums2[0]. To start, let's put
   the first element of the first few "lists" into a min-heap.
   Specifically, we can add the pairs (nums1[0], nums2[0]),
   (nums1[1], nums2[0]), ..., up to (nums1[k-1], nums2[0]) into
   the heap. We store them as (sum, index1, index2).

2. Extraction: The heap will automatically place the pair with
   the absolute smallest sum at the top. We can pull this pair
   out—it's the first of our k pairs.

3. Expansion: Here's the clever part. When we extract a pair
   (nums1[i], nums2[j]), we've exhausted that specific pair.
   What's the next candidate from the list it came from? It's
   (nums1[i], nums2[j+1]). We add this new candidate pair to
   the heap.

4. Repeat: The heap now contains our new candidate and all the
   previous candidates. It again tells us which pair has the
   overall smallest sum among all active candidates. We just
   repeat this process of extracting the minimum and adding
   the next candidate from the same nums1 element k times.

This way, we are always considering the frontier of the smallest
sums and efficiently picking the next smallest one at each step,
without ever having to generate all m*n pairs. The complexity
will be roughly O(k log k), which is very efficient given the
problem constraints.
'''


class Solution:
    def kSmallestPairs(
            self,
            nums1: List[int],
            nums2: List[int],
            k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        all_pairs = []
        for n1 in nums1:
            for n2 in nums2:
                all_pairs.append([n1, n2])
        all_pairs.sort(key=lambda x: x[0] + x[1])
        return all_pairs[:k]


class OptimizedSolution:
    def kSmallestPairs(
            self,
            nums1: List[int],
            nums2: List[int],
            k: int
    ) -> List[List[int]]:
        min_heap = []
        result_pairs = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(result_pairs) < k:
            _, i, j = heapq.heappop(min_heap)
            result_pairs.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return result_pairs


def tests():
    sol = OptimizedSolution()

    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    result1 = sol.kSmallestPairs(nums1, nums2, k)
    print(f"result is {result1}")
    assert result1 == [[1, 2], [1, 4], [1, 6]]

    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    result1 = sol.kSmallestPairs(nums1, nums2, k)
    print(f"result is {result1}")
    assert result1 == [[1, 1], [1, 1]]


if __name__ == '__main__':
    tests()
