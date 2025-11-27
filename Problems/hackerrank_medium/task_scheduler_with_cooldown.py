from collections import Counter, deque
import heapq

'''
Task Scheduler with Cooldown and Multiple Machines
Given an array tasks and m machines, find the minimum time to complete all tasks. Each time unit can process up to m tasks in parallel. A machine cannot process the same task type again for k time units.

Examples
Example 1

Input:

tasks = [1, 1, 2, 1]
m = 2
k = 2
Output:

3
Explanation:

We have 4 tasks: [1,1,2,1] and 2 machines with cooldown k=2.
Time unit 1: schedule type 1 on both machines → remaining [2,1].
Time unit 2: neither machine can run type 1 (cooldown until time 3), so we run task 2 on one machine; the other is idle → remaining [1].
Time unit 3: cooldown for type 1 has passed on at least one machine, so we schedule the last task 1. Total time = 3.
Example 2

Input:

tasks = [1, 1, 1, 2, 2, 3]
m = 3
k = 2
Output:

2
Explanation:

We have 6 tasks and 3 machines, k=2.
Time unit 1: schedule three tasks of type 1 in parallel → remaining [2,2,3].
Time unit 2: all machines are free to run types 2, 2, and 3 (none violate cooldown) → remaining [].
All tasks complete in 2 time units.
'''
'''
The problem states the
cooldown is per-machine, not global. Your insight that you're "not maintaining machine
to task type combination" is spot on.

However, tracking each of the m machines individually would be very complicated. The
efficient intuition is to reframe the problem: at any given time unit, what are the
best tasks to run on our m available machines?

The Core Intuition: A Greedy Simulation

This is a scheduling problem that can be solved with a greedy simulation, one time unit
at a time. The core greedy strategy is:

At each time unit, always try to run the most frequent tasks that are currently
available (i.e., not on cooldown).

Why is this optimal? The most frequent tasks are the biggest "problem" as they are most
likely to cause conflicts and force idle time. By prioritizing them, you get them into
their cooldown period as early as possible, creating more flexibility to schedule less
frequent tasks in the gaps.

How to Implement This Efficiently

Instead of tracking individual machines, we can abstract the process by tracking the
state of task types. We need two key data structures to manage this simulation:

1. A Max Heap (Priority Queue): To instantly know which available tasks are the most
    frequent. We can store (frequency, task_type) tuples in the heap. This lets us pull
    the highest-priority tasks to run at any time.

2. A Cooldown Queue: To keep track of tasks that have been recently run and are now on
    cooldown. When a task is run at time, we can put it in this queue with a note that
    it will be available again at time + k + 1. A simple queue (like a deque) works
    perfectly.

The Simulation Algorithm

Here's how the simulation flows, time unit by time unit:

1. Initialization:
    * Count the frequency of all tasks and populate your Max Heap.
    * Create an empty Cooldown Queue.
    * Set time = 0.

2. Run the Simulation Loop (continue as long as there are tasks in the heap or in the
    cooldown queue):
    * Increment time.
    * Check Cooldowns: Look at the front of the cooldown queue. Are there any tasks
        whose cooldown period has just ended (i.e., their available_time is equal to the
        current time)? If so, move them from the queue back into the max heap, making
        them available to be scheduled again.
    * Schedule Tasks: Now, "run" up to m tasks for the current time unit.
        * Pop up to m of the highest-priority (most frequent) tasks from the max heap.
        * For each task you "run," if it still needs to be executed more times, add it
            to the cooldown queue with its new available_time set to time + k + 1.

3. End Condition: When both the max heap and the cooldown queue are empty, all tasks
    have been completed. The final value of time is your answer.

This approach correctly models the constraints. The max heap helps you make the best
greedy choice, and the cooldown queue correctly enforces the waiting period without
needing to manage each of the m machines' states individually.
       

'''

def calculateMinimumTimeUnits(tasks, m, k):
    if not tasks:
        return 0
    if m >= len(tasks):
        return 1
    freq_map = Counter(tasks)
    task_max_heap = [(-freq, task_type) for task_type, freq in freq_map.items()]
    heapq.heapify(task_max_heap)
    cooldown_queue = deque()
    time = 0
    while task_max_heap or cooldown_queue:
        machines = m
        # fetch any tasks that have cooled down and push them back on
        # to max heap
        while cooldown_queue and cooldown_queue[0][0] <= time:
            _, freq, task_type = cooldown_queue.popleft()
            heapq.heappush(task_max_heap, (-freq, task_type))
        # pull tasks from max_heap to run while machines are still available
        time += 1
        while machines > 0 and task_max_heap:
            freq, task = heapq.heappop(task_max_heap)
            freq = -freq
            remaining_machines = machines - freq
            if remaining_machines < 0:
                machines = 0
                cooldown_queue.append((time + k, -remaining_machines, task))
            elif remaining_machines == 0:
                break
            else:
                machines = remaining_machines
    return time