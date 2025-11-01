import heapq

"""
Implementation of Prim's algorithm to find the
Minimum Spanning Tree (MST) of a graph represented
by an adjacency matrix.

Its more efficient for dense graphs with a lot of
edges. Since adjacency matrix is more suited for
representing dense graphs, this implementation uses
the same.
"""


def prims_algorithm(graph):
    """
    Finds the Minimum Spanning Tree (MST) of a graph
    using Prim's algorithm.

    Args:
        graph: A square 2D list (adjacency matrix)
        representing the graph, where:
        graph[i][j] is the weight of the edge from
        vertex i to j.
        Use float('inf') for no edge and 0 for self-loops.

    Returns:
        The total weight of the MST. Returns 0 if the graph
        is empty.
    """
    visited = set()
    # start the algorithm from node 0
    visited.add(0)
    # initialize priority queue with all the edges connected
    # to node 0.
    # format (edge weight, from_node(row), to_node(column))
    priority_queue = []
    for idx, item in enumerate(graph[0]):
        if idx == 0:
            continue
        if item != float("inf"):
            edge = (item, 0, idx)
            priority_queue.append(edge)
    heapq.heapify(priority_queue)
    mst_weight = 0
    num_vertices = len(graph)
    while len(visited) < num_vertices and priority_queue:
        weight, _, to_node = heapq.heappop(priority_queue)
        if to_node not in visited:
            # add to visited set
            visited.add(to_node)
            # add the weight to talk weight
            mst_weight += weight
            # add the outgoing edges to the current node
            # to priority queue
            for ind, item in enumerate(graph[to_node]):
                if ind == to_node:
                    continue
                if item != float("inf"):
                    edge = (item, to_node, ind)
                    heapq.heappush(priority_queue, edge)
    return mst_weight


def tests():
    """
    Contains test cases for the Prim's algorithm implementation.
    """
    print("--- Running Prim's Algorithm Tests ---")

    inf = float("inf")

    # Test Case 1: A small, 4x4 complete (fully dense) graph
    graph1 = [[0, 2, 9, 3], [2, 0, 4, 1], [9, 4, 0, 8], [3, 1, 8, 0]]
    expected_mst_weight1 = 7  # Edges: (1,3) w=1 + (0,1) w=2 + (1,2) w=4
    print("\nTest Case 1: A small, 4x4 complete graph.")
    print("Adjacency Matrix:")
    for row in graph1:
        print(f"  {row}")
    print(f"The expected MST weight is {expected_mst_weight1}.")
    mst_weight1 = prims_algorithm(graph1)
    print(f"Got: {mst_weight1}")
    assert mst_weight1 == expected_mst_weight1
    print("-" * 20)

    # Test Case 2: A 5x5 dense graph
    graph2 = [
        [0, 10, 1, 8, inf],
        [10, 0, 2, inf, 7],
        [1, 2, 0, 3, 4],
        [8, inf, 3, 0, 5],
        [inf, 7, 4, 5, 0],
    ]
    expected_mst_weight2 = (
        10  # Edges: (0,2) w=1 + (2,1) w=2 + (2,3) w=3 + (2,4) w=4
    )
    print("Test Case 2: A 5x5 dense graph.")
    print("Adjacency Matrix (inf represents no direct edge):")
    for row in graph2:
        print(f"  {row}")
    print(f"The expected MST weight is {expected_mst_weight2}.")
    mst_weight2 = prims_algorithm(graph2)
    print(f"Got: {mst_weight2}")
    assert mst_weight2 == expected_mst_weight2
    print("-" * 20)

    # Test Case 3: Another dense graph with some equal weight edges
    graph3 = [
        [0, 2, 2, inf, 5],
        [2, 0, 3, 3, inf],
        [2, 3, 0, 3, 1],
        [inf, 3, 3, 0, 4],
        [5, inf, 1, 4, 0],
    ]
    expected_mst_weight3 = (
        8  # Edges: (2,4) w=1 + (0,1) w=2 + (0,2) w=2 + (1,3) w=3
    )
    print("Test Case 3: A dense graph with equal weight edges.")
    print("Adjacency Matrix:")
    for row in graph3:
        print(f"  {row}")
    print(f"The expected MST weight is {expected_mst_weight3}.")
    mst_weight3 = prims_algorithm(graph3)
    print(f"Got: {mst_weight3}")
    assert mst_weight3 == expected_mst_weight3
    print("-" * 20)

    print("--- Tests Complete ---")


if __name__ == "__main__":
    tests()
