import heapq
'''
295. Find Median from Data Stream
Hard
Topics
premium lock icon
Companies
The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value,
and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data
stream to the data structure.
double findMedian() returns the median of all elements so
far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian",
"addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure
before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100],
how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range
[0, 100], how would you optimize your solution?
'''

'''
The classic and most efficient solution to this problem is to
use two heaps:

1. A Max-Heap (let's call it lo) to store the smaller half
   of the numbers.
2. A Min-Heap (let's call it hi) to store the larger half
   of the numbers.

The core idea is to always keep the data stream divided into
these two halves. By looking at the top of both heaps, we can
always know where the middle of the entire sorted data set is.

The Invariants (Rules we must maintain)

1. Partitioning: Every number in the lo heap is less than or
equal to every number in the hi heap.

2. Balancing: The two heaps are always kept at roughly the
same size. Their sizes can differ by at most 1.

How It Works

* `addNum(num)`:
    1. Add the new number to the lo (max-heap).
    2. To maintain the partitioning rule, take the largest element
       from lo (its root) and move it to the hi (min-heap).
    3. To maintain the balancing rule, if the hi heap now has more
       elements than the lo heap, take the smallest element from hi
       (its root) and move it back to lo.

    After these steps, the two heaps are re-balanced and
    partitioned correctly, with the new number incorporated.
    Each addNum operation takes O(log n) time.

* `findMedian()`:
    This becomes very simple and fast (O(1)):
    * If the total number of elements is odd, one heap will have
      one more element than the other (by our balancing logic,
      it will be the lo heap). The median is simply the top
      element of the lo heap.
    * If the total number of elements is even, the heaps will be
      the same size. The median is the average of the top of the
      lo heap (the largest number in the small half) and the top
      of the hi heap (the smallest number in the large half).

This two-heap structure perfectly balances the need for
efficient additions and quick median calculations.

The most intuitive way to handle a new number is to not
decide upfront. Instead, you follow a simple, consistent
recipe for every single number you add. This recipe
automatically maintains the two crucial rules (the partition
rule and the balance rule).

Here is the intuition for the recipe:

Let's designate one heap as the "default" entry point.
We'll use the lo (max-heap) for this.

For any new number, num, we perform these steps:

1. Add to `lo` (the max-heap):
    Always push the new num into the lo heap.
    * Problem: The lo heap might now contain a value
      that is actually larger than the smallest value in the
      hi heap. This would break our rule that "everything
      in lo must be smaller than everything in hi".

2. Balance by moving the largest from `lo` to `hi`:
    To fix this, immediately take the largest item from
    lo (which is its root/top element) and push it into
    the hi heap.
    * Result: Now the partition rule is guaranteed to be fixed.
      The largest of the "small numbers" has been promoted into
      the "large numbers" heap.
    * New Problem: The heaps might now be unbalanced in size.
      For example, we might have 3 elements in lo and 5 in hi.

3. Re-balance sizes if necessary:
    Finally, check the heap sizes. If the hi heap has become
    too large (i.e., it has more elements than lo), we fix the
    balance by taking the smallest item from hi (its root/top)
    and moving it back to lo.
    * Result: The heaps are now perfectly balanced (or differ
      by at most 1), and the partition rule is still correct.
'''


class MedianFinder:

    def __init__(self):
        # max heap to store the left half of the list
        self.lo = []
        # min heap to store the right half of the list
        self.high = []

    def addNum(self, num: int) -> None:
        # add by default to left half or lo "max_heap"
        # defined above
        heapq.heappush(self.lo, -num)
        # push the largest element from lo to
        # self.high, unconditionally. This will ensure
        # lo is never bigger than high
        element = heapq.heappop(self.lo)
        heapq.heappush(self.high, -element)
        # rebalance lists if difference in length is more
        # than 1
        if len(self.high) - len(self.lo) > 1:
            item = heapq.heappop(self.high)
            heapq.heappush(self.lo, -item)

    def findMedian(self) -> float:
        if (len(self.high) + len(self.lo)) % 2 == 0:
            one, two = -self.lo[0], self.high[0]
            return (one + two) / 2
        else:
            return self.high[0]


def tests():
    """
    Test cases for the MedianFinder class.
    """
    # Example 1
    print("--- Running Test Case 1 ---")
    medianFinder = MedianFinder()

    medianFinder.addNum(1)
    print("addNum(1) called. Current stream: [1]")

    medianFinder.addNum(2)
    print("addNum(2) called. Current stream: [1, 2]")

    median1 = medianFinder.findMedian()
    print(f"findMedian() -> Expected: 1.5, Got: {median1}")
    assert median1 == 1.5

    medianFinder.addNum(3)
    print("addNum(3) called. Current stream: [1, 2, 3]")

    median2 = medianFinder.findMedian()
    print(f"findMedian() -> Expected: 2.0, Got: {median2}")
    assert median2 == 2.0

    print("--- Test Case 1 Finished ---")


if __name__ == "__main__":
    tests()
