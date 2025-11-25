from typing import List
import heapq
'''
Suppose LeetCode will start its IPO soon. In order to sell
a good price of its shares to Venture Capital, LeetCode
would like to work on some projects to increase its capital
before the IPO. Since it has limited resources, it can only
finish at most k distinct projects before the IPO. Help
LeetCode design the best way to maximize its total capital
after finishing at most k distinct projects.

You are given n projects where the ith project has a pure
profit profits[i] and a minimum capital of capital[i] is
needed to start it.

Initially, you have w capital. When you finish a project,
you will obtain its pure profit and the profit will be added
to your total capital.

Pick a list of at most k distinct projects from given projects
to maximize your final capital, and return the final maximized
capital.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only
start the project indexed 0.
After finishing it you will obtain profit 1 and your capital
becomes 1.
With capital 1, you can either start the project indexed 1
or the project indexed 2.
Since you can choose at most 2 projects, you need to finish
the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is:
0 + 1 + 3 = 4.

Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6
'''

'''
the strategy for each of the k investments is:

1. Look at all the projects available.
2. Filter them down to a list of only the ones you can
   afford right now (where project_capital <= w).
3. From this affordable list, pick the one with the
   absolute highest profit.
4. Add that profit to your capital w and repeat.

The Problem with the Naive Strategy: Efficiency

If you were to implement that directly, it would be slow.
For each of the k times you make a choice, you'd have to
scan the entire list of n projects to find the affordable
ones. This would be too inefficient.

This is where we need the right tools to make the two
key steps fast:
1. "Finding all affordable projects."
2. "Picking the most profitable one from that group."

The Efficient Solution: Using Heaps (Priority Queues)

We can optimize this with a combination of sorting and
a max-heap.

1. Handle Affordability (Sorting): How can we quickly
   find projects as they become affordable? First, sort
   all the projects based on their capital requirement,
   from smallest to largest. This creates an orderly
   line of projects. As your capital w grows, you can
   just walk down this line and "unlock" projects in
   order.

2. Handle "Best Profit" (Max-Heap): A max-heap is the
   perfect data structure for repeatedly finding the
   largest element in a changing set. We will use a
   max-heap to store the profits of all the projects
   that are currently affordable but not yet chosen.

The Final Algorithm

Here is the complete, efficient greedy algorithm:

1. Sort: Create pairs of (capital, profit) for all
   projects and sort this list based on capital.

2. Initialize: Create an empty max-heap, which will
   store the profits of projects you can afford.

3. Loop `k` times (for each investment you can make):
    a. Add Affordable Projects: Go through your
       sorted list of projects and add the profits of
       all projects you can now afford (i.e.,
       capital <= w) into the max-heap.
Since the list is sorted, you can just continue from
where you left off in the previous iteration.
    b. Check for Viable Investments: If the max-heap
       is empty, it means you can't afford any of the
       remaining projects. You're stuck, so you can stop
       early.
    c. Make the Best Investment: If the heap is not
       empty, pop the largest value from it (this is
       your most profitable choice). Add this profit
       to your capital w.

4. Return `w`: After the loop finishes, w will be your
   maximized capital.

This approach ensures that at every step, you are
efficiently finding and choosing the most profitable
project available, leading to the optimal final result.
'''


class Solution:
    def findMaximizedCapital(
            self,
            k: int,
            w: int,
            profits: List[int],
            capital: List[int]
    ) -> int:
        # create an array with (capital, profit) tuple to sort it
        # with capital and efficiently find the affordable projects
        projects = sorted(zip(capital, profits), key=lambda x: (x[0], -x[1]))
        # create a max heap for finding the project with max profit
        max_profit = []
        k = min(k, len(profits))
        i = 0
        # i = None
        while k > 0:
            while i < len(profits) and projects[i][0] <= w:
                heapq.heappush(max_profit, -projects[i][1])
                i += 1
            if max_profit:
                profit = heapq.heappop(max_profit)
                w -= profit
            else:
                break
            k -= 1
        return w


def tests():
    sol = Solution()

    # Example 1
    k1 = 2
    w1 = 0
    profits1 = [1, 2, 3]
    capital1 = [0, 1, 1]
    expected1 = 4
    result1 = sol.findMaximizedCapital(k1, w1, profits1, capital1)
    assert result1 == expected1
    print(f"Test Case 1 Passed: Result={result1}")

    # Example 2
    k2 = 3
    w2 = 0
    profits2 = [1, 2, 3]
    capital2 = [0, 1, 2]
    expected2 = 6
    result2 = sol.findMaximizedCapital(k2, w2, profits2, capital2)
    assert result2 == expected2
    print(f"Test Case 2 Passed: Result={result2}")

    # exmaple 3
    k3 = 1
    w3 = 0
    profits3 = [1, 2, 3]
    capital3 = [1, 1, 2]
    expected3 = 0
    result3 = sol.findMaximizedCapital(k3, w3, profits3, capital3)
    assert result3 == expected3
    print(f"Test Case 2 Passed: Result={result3}")

    # exmaple 4
    k4 = 10
    w4 = 0
    profits4 = [1, 2, 3]
    capital4 = [0, 1, 2]
    expected4 = 6
    result4 = sol.findMaximizedCapital(k4, w4, profits4, capital4)
    assert result4 == expected4
    print(f"Test Case 2 Passed: Result={result4}")

    # exmaple 5
    k5 = 2
    w5 = 0
    profits5 = [1, 2, 3]
    capital5 = [0, 9, 10]
    expected5 = 1
    result5 = sol.findMaximizedCapital(k5, w5, profits5, capital5)
    print(f"result5 is {result5}")
    assert result5 == expected5
    print(f"Test Case 2 Passed: Result={result5}")


if __name__ == "__main__":
    tests()
