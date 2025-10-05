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
