"""
Dijkstra's Algorithm: A Detailed Guide for Interviews and Review

Purpose:
    Dijkstra's algorithm finds the shortest paths from a single source node to
    all other nodes in a weighted graph. It is a cornerstone algorithm for
    solving shortest-path problems where all edge weights are non-negative.

Core Idea:
    The algorithm works by iteratively "visiting" nodes, starting from the
    source. It maintains a set of unvisited nodes and a record of the
    currently known shortest distances from the source. At each step, it
    greedily selects the unvisited node with the smallest known distance,
    marks its path as final, and then updates the distances of its neighbors
    if a shorter path is found through the current node.

Analogy: The Expanding Ripple
    Imagine dropping a stone in a pond. The source node is where the stone
    hits the water. The ripples expand outwards, reaching closer points
    first, then farther ones. Dijkstra's algorithm works similarly: it
    "explores" the graph outwards from the source, always advancing the
    "wavefront" to the nearest unvisited node. Once a point is engulfed by
    the ripple (visited), its shortest distance from the center is finalized,
    because the ripple can't backtrack to find a shorter path.

Key Constraint:
    - Non-Negative Edge Weights: The algorithm's greedy strategy relies on
      the assumption that once we finalize the shortest path to a node, no
      longer path can later become shorter. A negative edge could violate
      this, allowing a path with more edges to have a smaller total weight.
      For graphs with negative edges, use the Bellman-Ford algorithm.

Data Structures:
    1. Graph Representation: An adjacency list is typically most efficient,
       mapping each node to a list of its neighbors and the corresponding
       edge weights. E.g., `graph = { 'A': [('B', 2), ('C', 5)], ... }`.

    2. Distances (or Costs) Map: Stores the shortest distance found *so far*
       from the source to every other node. It is initialized with infinity
       for all nodes except the source, which is set to 0.
       E.g., `distances = { 'A': 0, 'B': float('inf'), 'C': float('inf') }`.

    3. Priority Queue: The heart of the algorithm's efficiency. It stores
       tuples of `(distance, node)` for all nodes that have been reached but
       not yet finalized. The priority queue ensures that we can always
       extract the unvisited node with the smallest current distance in
       O(log V) time.

    4. Visited Set: A set to keep track of nodes for which the shortest path
       has been finalized. This prevents reprocessing nodes and getting
       stuck in cycles.

Algorithm Steps:
    1. Initialization:
       - Create a `distances` map, setting the source node's distance to 0
         and all others to infinity.
       - Create a priority queue and add the source node with its distance:
         `pq.put((0, source_node))`.
       - Create an empty `visited` set.

    2. Main Loop:
       - While the priority queue is not empty:
         a. Pop the element with the smallest distance. This gives you the
            current `(distance, node)`. Let's call them `current_distance`
            and `current_node`.

         b. If `current_node` is already in the `visited` set, `continue`.
            (This handles cases where we've found a shorter path to a node
            that was already in the queue with a higher cost).

         c. Add `current_node` to the `visited` set. Its shortest path is now
            considered final and will not be changed.

         d. For each `(neighbor, edge_weight)` of `current_node`:
            i.  **The Relaxation Step:** Calculate the new potential distance
                to this neighbor by going through `current_node`:
                `new_distance = current_distance + edge_weight`.

            ii. If `new_distance` is less than the known distance to the
                neighbor (`distances[neighbor]`), it means we've found a
                shorter path.
                - Update the neighbor's distance: `distances[neighbor] = new_distance`.
                - Push the neighbor and its new, shorter distance to the
                  priority queue: `pq.put((new_distance, neighbor))`.

    3. Completion:
       - Once the loop finishes, the `distances` map contains the shortest
         path distances from the source to all reachable nodes. Any node
         still at infinity is unreachable.

Example Walkthrough:
    Graph: A ->(1)-> B, A ->(4)-> C, B ->(2)-> C, B ->(5)-> D, C ->(3)-> D
    Source: A

    1. Init:
       - distances = {A: 0, B: inf, C: inf, D: inf}
       - pq = [(0, A)]
       - visited = {}

    2. Pop (0, A):
       - visited = {A}
       - Neighbors of A are B and C.
       - Relax A->B: new_dist = 0 + 1 = 1. Update dist[B]=1. pq.put((1, B)).
       - Relax A->C: new_dist = 0 + 4 = 4. Update dist[C]=4. pq.put((4, C)).
       - pq is now [(1, B), (4, C)]

    3. Pop (1, B):
       - visited = {A, B}
       - Neighbors of B are C and D.
       - Relax B->C: new_dist = 1 + 2 = 3. Update dist[C]=3. pq.put((3, C)).
       - Relax B->D: new_dist = 1 + 5 = 6. Update dist[D]=6. pq.put((6, D)).
       - pq is now [(3, C), (4, C), (6, D)]  (Note: (4,C) is a stale entry)

    4. Pop (3, C):
       - visited = {A, B, C}
       - Neighbor of C is D.
       - Relax C->D: new_dist = 3 + 3 = 6. dist[D] is already 6. No update.
       - pq is now [(4, C), (6, D)]

    5. Pop (4, C):
       - C is already in visited. Continue.

    6. Pop (6, D):
       - visited = {A, B, C, D}
       - No unvisited neighbors.

    7. PQ is empty. End.

    Final Distances: {A: 0, B: 1, C: 3, D: 6}

Complexity Analysis:
    - V: Number of vertices (nodes)
    - E: Number of edges

    - Time Complexity: O(E log V)
      - Every edge is processed once during the relaxation step (O(E)).
      - For each relaxation that results in an update, we perform a push
        operation on the priority queue, which takes O(log V) time.
      - We also perform V pop operations, each taking O(log V).
      - The dominant factor is O(E * log V).

    - Space Complexity: O(V + E)
      - O(E) for the adjacency list representation of the graph.
      - O(V) for the distances map and the visited set.
      - O(V) for the priority queue in the worst case.
"""

import heapq
import math
from typing import Tuple, Dict

sample_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 5, 'E': 2},
    'C': {'D': 1},
    'D': {},
    'E': {'D': 2}
}


def dijkstra_with_path(graph, start_node) -> Tuple[Dict, Dict]:
    # 1. Initialize distances and the priority queue
    # Guard clause: If the start node isn't in the graph, we can't proceed.
    if start_node not in graph:
        return {}, {}

    distances = {node: math.inf for node in graph}
    distances[start_node] = 0
    # 1. Initialize the predecessors dictionary
    predecessors = {node: None for node in graph}
    # The priority queue will store tuples of (distance, node).
    # heapq sorts by the first element of the tuple, so distance comes first.
    priority_queue = [(0, start_node)]
    while priority_queue:
        # Get the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)
        # If we've already found a shorter path to this node, skip.
        # This is an important optimization.
        if current_distance > distances[current_node]:
            continue
        # Explore neighbors and "relax" the edge
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If we found a new shorter path to the neighbor,
            if distance < distances[neighbor]:
                # update its distance and add it to the priority queue
                # to visit later
                distances[neighbor] = distance
                # When we find a shorter path, update the predecessor
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances, predecessors


def reconstruct_path(predecessors, start_node, end_node):
    """
    Helper function to reconstruct the shortest path
    from the predecessors dict.
    """
    path = []
    # If the end node is not in the predecessors map,
    # it's not part of the graph traversal.
    if end_node not in predecessors:
        return None

    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = predecessors[current_node]
    # If the path reconstruction did not end at the start_node,
    # it means there is no path.
    path.reverse()
    if path[0] == start_node:
        return path
    else:
        return []


def tests():
    """Test suite for Dijkstra's algorithm implementation."""
    print("--- Running Test Case 1: Standard Graph ---")
    distances, predecessors = dijkstra_with_path(sample_graph, 'A')
    print(f"Predecessor dict is {predecessors}")
    expected_distances = {'A': 0, 'B': 1, 'C': 4, 'D': 5, 'E': 3}
    assert distances == expected_distances
    f"Expected {expected_distances}, but got {distances}"

    # Reconstruct and verify the path to 'D'
    path_to_d = reconstruct_path(predecessors, 'A', 'D')
    # Note: The path could be ['A', 'C', 'D'] or ['A', 'B', 'E', 'D']
    # as both have weight 5.
    # The implementation finds ['A', 'B', 'E', 'D'] due to the
    # priority queue order.
    expected_path_d = ['A', 'B', 'E', 'D']
    assert path_to_d == expected_path_d
    f"Expected path {expected_path_d}, but got {path_to_d}"

    print("\nAll tests passed!")


if __name__ == '__main__':
    tests()
