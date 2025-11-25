import heapq
from typing import List, Optional
import random
'''
Given an integer array nums and an integer k,
return the kth largest element in the array.

Note that it is the kth largest element in the
sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> Optional[int]:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        result = None
        for _ in range(k):
            result = heapq.heappop(nums)
        return -result if result else None


class SolutionOptimized:
    def findKthLargest(self, nums: List[int], k: int) -> Optional[int]:
        '''
        1. The Heap-based Optimization (More Efficient Heap Method)
        Instead of a max-heap of size n, you can use a min-heap of
        size `k`. This is often a better approach.

        Intuition:
        The goal is to maintain a "container" that holds the k
        largest elements seen so far. A min-heap is perfect for
        this. The smallest of these k largest elements will
        always be at the top of the min-heap.

        Algorithm:
        1. Create an empty min-heap.
        2. Iterate through the input array nums.
        3. For each number, push it onto the heap.
        4. If the heap's size grows larger than k, pop the smallest
           element (the root of the min-heap).
        5. After iterating through all the numbers, the heap
           contains exactly the k largest elements from the array.
           The root of the heap is the k-th largest element.

        Complexity:
        * Time: O(n log k). You process n elements, and each heap
          operation (push/pop) takes O(log k) time because the
          heap size never exceeds k.
        * Space: O(k) to store the elements in the heap.

        This is generally more efficient than the max-heap
        approach, especially if k is much smaller than n.
        '''
        length = len(nums)
        min_heap = []
        min_heap_size = 0
        for i in range(length):
            heapq.heappush(min_heap, nums[i])
            min_heap_size += 1
            if min_heap_size > k:
                heapq.heappop(min_heap)
                min_heap_size -= 1
        return min_heap[0]


class MostEfficientSolution:
    def findKthLargest(self, nums: List[int], k: int) -> Optional[int]:
        '''
        2. Quickselect (The "Optimal" Approach)

        This is the classic, most time-efficient algorithm for
        this type of problem. It's a modification of the
        QuickSort algorithm.

        Intuition:
        Instead of fully sorting the array, you just need to
        find the single position where the k-th largest element
        would end up.
        1. Pick a random pivot element and partition the array
           around it. All elements smaller than the pivot go to
           one side, and all larger elements go to the other.
        2. After partitioning, the pivot is in its final,
           sorted position. Let's say this is index p.
        3. Compare p with the index we're looking for
           (which is n - k for the k-th largest element).
            * If p is our target index, we've found the element!
            * If p is greater than our target, we know the element
              must be in the left subarray. We can ignore the right
              side and repeat the process on the left.
            * If p is less than our target, the element must be in
              the right subarray. We ignore the left and repeat on
              the right.

        Complexity:
        * Time: O(n) on average. By discarding half of the array
          at each step, it avoids the full O(n log n) work of a
          complete sort. (The worst-case is O(n²), but it's very
          rare with a good pivot strategy).
        * Space: O(1), as it can be done in-place.
        '''
        self.nums = nums
        self.k = k
        n = len(nums)
        self.n = n
        low, high = 0, n - 1
        ind = self.partition(low, high)
        return self.nums[ind]

    def partition(self, low, high):
        random_idx = random.randint(low, high)
        self.nums[low], self.nums[random_idx]\
            = self.nums[random_idx], self.nums[low]
        pivot = self.nums[low]
        i, j = low + 1, high
        while i <= j:
            # increment i till it finds an element larger than pivot
            while i <= j and self.nums[i] < pivot:
                i += 1
            # decrement j until it finds an element smaller
            # than pivot
            while i <= j and self.nums[j] >= pivot:
                j -= 1
            if i < j:
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        self.nums[low], self.nums[j] = self.nums[j], self.nums[low]
        if j == self.n - self.k:
            return j
        elif j > self.n - self.k:
            return self.partition(low, j - 1)
        else:
            return self.partition(j + 1, high)


def tests():
    sol = MostEfficientSolution()

    # Example 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5
    result1 = sol.findKthLargest(nums1, k1)
    assert result1 == expected1
    print(f"Test 1: Input: nums={nums1}, k={k1}. Expected: {expected1}")

    # Example 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4
    result2 = sol.findKthLargest(nums2, k2)
    assert result2 == expected2
    print(f"Test 2: Input: nums={nums2}, k={k2}. Expected: {expected2}")


if __name__ == "__main__":
    tests()
