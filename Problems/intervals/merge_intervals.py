from typing import List

"""
Given an array of intervals where
intervals[i] = [starti, endi], merge all overlapping
intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap,
merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered
overlapping.

Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered
overlapping.
"""


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = [sorted_intervals.pop(0)]
    for s in sorted_intervals:
        start, end = s[0], s[1]
        # compare with last entry in merged interval
        _, last_end = merged_intervals[-1][0], merged_intervals[-1][1]
        if start <= last_end:
            merged_intervals[-1][1] = max(end, last_end)
        else:
            merged_intervals.append(s)
    return merged_intervals


def tests():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    res = merge_intervals(intervals)
    print(f"merged intervals for {intervals} are {res}")
    assert res == [[1, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    res = merge_intervals(intervals)
    print(f"merged intervals for {intervals} are {res}")
    assert res == [[1, 5]]
    intervals = [[4, 7], [1, 4]]
    res = merge_intervals(intervals)
    print(f"merged intervals for {intervals} are {res}")
    assert res == [[1, 7]]


tests()
