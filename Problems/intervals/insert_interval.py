from typing import List

"""
You are given an array of non-overlapping intervals
"intervals" where intervals[i] = [start-i, end-i]
represent the start and the end of the ith interval
and intervals is sorted in ascending order by start-i.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals such that intervals
is still sorted in ascending order by start-i and
intervals still does not have any overlapping intervals
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place.
You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps
with [3,5],[6,7],[8,10].
"""


def insert_interval(
    intervals: List[List[int]], new_interval: List[int]
) -> List[List[int]]:
    n = len(intervals)
    result = []
    i = 0
    # add the intervals coming before the new interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    print(f"added intervals before index {i}")
    # merge the overlapping intervals
    # dont need to check for
    # current interval end > new interval start as the
    # while loop above has already done that
    # so just check for end value conditions, i.e
    # current start <= new_end
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    result.append(new_interval)
    # add the remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    return result


def tests():
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    res = insert_interval(intervals, new_interval)
    print(
        f"result for {intervals} and new interval", f"{new_interval} is {res}"
    )
    assert res == [[1, 5], [6, 9]]
    inte = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_int = [4, 8]
    r = insert_interval(inte, new_int)
    print(f"result for {inte} and new interval", f"{new_int} is {r}")
    assert r == [[1, 2], [3, 10], [12, 16]]

    interval3 = [[1, 2], [3, 8], [9, 10], [11, 12]]
    new_interval3 = [4, 8]
    result = insert_interval(interval3, new_interval3)
    print(f"result for {interval3} and new interval", f"{new_interval3} is {result}")
    assert result == [[1, 2], [3, 8], [9, 10], [11, 12]]

tests()
