'''
Maximize Profit with Task Deadlines and Multiple Servers
Given n tasks with deadlines and profits, and m servers, schedule tasks to maximize total profit. Each task takes one time unit, up to m tasks can run per time slot, and each task must finish by its deadline.

Examples
Example 1

Input:

n = 3
m = 1
deadlines = [2, 1, 3]
profits = [20, 10, 30]
Output:

60
Explanation: With one server (m=1) and three tasks:

Sort or consider scheduling by profit within deadlines:
Task 2 (profit 30, deadline 3) → assign to time slot 3
Task 0 (profit 20, deadline 2) → assign to time slot 2
Task 1 (profit 10, deadline 1) → assign to time slot 1
Each fits before its deadline and we have exactly one task per slot.
Total profit = 30 + 20 + 10 = 60.
Example 2

Input:

n = 7
m = 2
deadlines = [1, 1, 1, 2, 2, 3, 3]
profits = [10, 20, 5, 30, 25, 15, 18]
Output:

118
Explanation: We have 7 tasks and 2 servers per time unit. We fill from the latest slot back:

Time slot 3 (capacity 2): tasks with deadline ≥ 3 are #5 (15) and #6 (18). Schedule both → profit = 15 + 18 = 33.
Time slot 2 (capacity 2): remaining tasks with deadline ≥ 2 are #3 (30) and #4 (25). Schedule both → profit = 30 + 25 = 55.
Time slot 1 (capacity 2): remaining tasks with deadline ≥ 1 are #0 (10), #1 (20), #2 (5). Pick the top 2 profits: 20 and 10 → profit = 30. Total profit = 33 + 55 + 30 = 118.
'''

'''
 Intuition for the Correct Approach

  Let's rethink the problem from a greedy perspective. What is the most important factor?
  Profit. We always want to complete the tasks with the highest profit. The deadlines are
  constraints we must work around.

  Here's the intuition for a successful greedy strategy:

   1. Prioritize High-Profit Tasks: It always makes sense to consider tasks from the most
      profitable to the least profitable. So, the first step should be to sort all tasks
      by their profit in descending order.

   2. Schedule as Late as Possible (The "Aha!" Moment): Now, iterate through your
      profit-sorted tasks. For each task, you have to decide when to schedule it. Let's
      say a task has a profit of 1000 and a deadline of 3. You could schedule it at time
      1, 2, or 3.
       * If you schedule it at time 1, you've used up a very valuable early time slot.
         This might prevent another task that only has a deadline of 1 from being
         scheduled.
       * If you schedule it at time 3 (its deadline), you keep time slots 1 and 2 open
         for other tasks. This is the key insight: By scheduling a task at the latest
         possible moment, you maximize the availability of earlier time slots for other
         tasks that might have tighter deadlines.

   3. Putting It Together (Working Backwards): This leads to a powerful strategy:
       * Iterate through your time slots backwards, from the maximum possible deadline
         down to 1.
       * At each time slot t, you have m available server slots.                         ▄
       * What are the best tasks you can possibly run at time t? They are the most       ▀
         profitable tasks whose deadline is t or later (deadline >= t).
       * As you iterate from t_max down to 1, you can maintain a collection of all tasks
         that have become "available" (i.e., whose deadline you have reached). From this
         collection, you can pick the top m most profitable ones to "schedule" at time t.

  Hint for the Fix:
  To implement this "work backwards" approach, you'll need to process tasks sorted by one
  criterion (deadline) while maintaining a pool of available tasks sorted by another
  criterion (profit). Think about what data structure would be perfect for efficiently
  adding tasks to a pool and then always being able to pull out the most profitable ones.
'''

def maximizeParallelTaskProfit(n, m, deadlines, profits):
    if not n:
        return 0
    total_profit = 0
    sorted_data = sorted(list(zip(profits, deadlines)), key=lambda x: x[1])
    max_deadline = sorted_data[-1][1]
    max_heap = []
    for time in range(max_deadline, 0, -1):
        # gathering eligible tasks, since we are going backwards,
        # at time 3, any task that has deadline more than or equal to 3
        # can be picked up for scheduling
        while sorted_data and sorted_data[-1][1] >= time:
            profit, deadline = sorted_data.pop()
            heapq.heappush(max_heap, -profit)
        # scheduling loop
        for _ in range(m):
            if not max_heap:
                break
            profit = heapq.heappop(max_heap)
            profit = -profit
            total_profit += profit

    return total_profit