import heapq
'''
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where
moveTime[i][j] represents the minimum time in seconds
when you can start moving to that room. You start from
the room (0, 0) at time t = 0 and can move to an adjacent
room. Moving between adjacent rooms takes one second for
one move and two seconds for the next, alternating
between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall,
either horizontally or vertically.

Example 1:

Input: moveTime = [[0,4],[4,4]]
Output: 7

Explanation:
The minimum time required is 7 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.

Example 2:

Input: moveTime = [[0,0,0,0],[0,0,0,0]]
Output: 6

Explanation:
The minimum time required is 6 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.

Example 3:

Input: moveTime = [[0,1],[1,2]]
Output: 4
'''
'''
 The Core Idea

Think of the grid not just as a map of rooms, but as a graph where
the "path length" is the time taken. Dijkstra's algorithm is
perfect for finding the minimum time to reach a destination,
which is exactly what the problem asks for.

The main challenge is that the time to move between rooms isn't
constant; it alternates between 1 and 2 seconds. This means the
cost of an edge in our graph depends on the path you took to
get there.

Graph Nodes: Beyond Just Location

Because the move cost depends on whether you've made an odd or
even number of moves, a simple (row, col) coordinate is not
enough to define a "node" in our graph. Knowing you are at
(r, c) isn't enough; you also need to know if your next move
will be a 1-second move or a 2-second move.

Therefore, the nodes in our graph for Dijkstra's algorithm
should represent a state, which is a combination of location
and move parity. You can think of each physical room as
having two distinct states to visit:

1. `(row, col, 'next_move_is_1_sec')`: You have arrived
    at room (r, c), and your next move will cost 1 second.
    This happens when you've made an even number of total
    moves so far.
2. `(row, col, 'next_move_is_2_sec')`: You have arrived at
    room (r, c), and your next move will cost 2 seconds.
    This happens when you've made an odd number of total moves.

The distances Structure

The distances data structure in your algorithm will store
the minimum time found so far to reach each of these specific
states. It wouldn't just map a room to a time, but a
state to a time.

You could structure it as a dictionary or a 3D array where
the keys/indices would be:
(row, column, move_parity)

And the value would be the minimum time to arrive at that
state. For example:

* distances[(r, c, 0)] = 10 would mean: "The fastest we've
  managed to get to room (r, c) in a state where our next
  move will cost 1 second is 10 seconds."
* distances[(r, c, 1)] = 13 would mean: "The fastest we've
  managed to get to room (r, c) in a state where our next
  move will cost 2 seconds is 13 seconds."

When you run Dijkstra's, your priority queue will be pulling
the state with the overall minimum time, and you will then
explore its neighbors, calculating the arrival time based on
the current state's move cost and the moveTime constraint
of the neighboring room.
'''


def min_time_to_room(move_time: list) -> int:
    if not move_time or not move_time[0]:
        return 0
    n, m = len(move_time), len(move_time[0])
    # State: (row, col, moves_made_parity) -> min_time
    # moves_made_parity = 0 for even moves, 1 for odd moves
    distances = {}
    # Priority queue: (time, row, col, moves_made)
    pq = [(0, 0, 0, 0)]
    # The key for distances must include the move parity
    distances[(0, 0, 0)] = 0

    while pq:
        time, row, column, moves = heapq.heappop(pq)
        # if we have found the result, return immediately
        if row == n - 1 and column == m - 1:
            return time
        # Check against the time for this specific state (including move parity)
        if time > distances.get((row, column, moves % 2), float('inf')):
            continue
        # determine the move cost of the next move
        move_cost = 1 if moves % 2 == 0 else 2
        # visit neighbours
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_row = row + dr
            next_column = column + dc
            # check if new row and column are within bounds
            if 0 <= next_row < n and 0 <= next_column < m:
                # we can only start if the total time lapsed
                # is more than currently paosed time
                start_move_time = max(time, move_time[next_row][next_column])
                total_time = start_move_time + move_cost
                new_moves_count = moves + 1
                new_moves_parity = new_moves_count % 2
                if total_time < distances.get(
                    (next_row, next_column, new_moves_parity), float('inf')
                ):
                    distances[(next_row, next_column, new_moves_parity)] = total_time
                    heapq.heappush(
                        pq,
                        (total_time, next_row, next_column, new_moves_count)
                    )
    # Should not be reached if a path exists
    return -1


def tests():
    move_time = [[0, 4], [4, 4]]
    res = min_time_to_room(move_time)
    print(f"minimum time for move time {move_time} is {res}")
    assert res == 7
    move_time = [[0, 0, 0, 0], [0, 0, 0, 0]]
    res = min_time_to_room(move_time)
    print(f"minimum time for move time {move_time} is {res}")
    assert res == 6
    move_time = [[0, 1], [1, 2]]
    res = min_time_to_room(move_time)
    print(f"minimum time for move time {move_time} is {res}")
    assert res == 4


tests()
