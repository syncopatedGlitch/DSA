from typing import Optional

"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list
(List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's
index (1-indexed). For example, the first node with val == 1,
the second node with val == 2, and so on. The graph is
represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used
to represent a finite graph. Each list describes the set of
neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to
the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2)
and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node(val = 1)
and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2)
and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1)
and 3rd node (val = 3).

Example 2:

Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list.
The graph consists of only one node with val = 1 and it
does not have any neighbors.

Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
ƒ
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        visited = {}
        stack = [node]
        while stack:
            n = stack.pop()
            if not visited.get(n):
                clone = Node(n.val)
                visited[n] = clone
                for neighbour in n.neighbors:
                    stack.append(neighbour)
        for original, clone in visited.items():
            for neighbour in original.neighbors:
                clone.neighbors.append(visited[neighbour])
        return visited[node]


def build_graph(adjList: list[list[int]]) -> Optional[Node]:
    """Helper function to build a graph from an adjacency list."""
    if not adjList:
        return None

    nodes = {i: Node(i) for i in range(1, len(adjList) + 1)}

    for i, neighbors in enumerate(adjList, 1):
        current_node = nodes[i]
        for neighbor_val in neighbors:
            current_node.neighbors.append(nodes[neighbor_val])

    return nodes.get(1)


def graph_to_adj_list(node: Optional[Node]) -> list[list[int]]:
    """Helper function to convert a graph back to an adjacency list."""
    if not node:
        return []

    # Use BFS to find all nodes in the graph
    q = [node]
    all_nodes = {node.val: node}
    visited = {node}

    while q:
        current = q.pop(0)
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                all_nodes[neighbor.val] = neighbor
                q.append(neighbor)

    # Build the adjacency list from the collected nodes
    adj_list = []
    for i in range(1, len(all_nodes) + 1):
        current_node = all_nodes[i]
        # Sort neighbor values for consistent output
        neighbor_vals = sorted([n.val for n in current_node.neighbors])
        adj_list.append(neighbor_vals)

    return adj_list


def tests():
    sol = Solution()

    # Example 1
    adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = build_graph(adjList1)
    cloned_graph1 = sol.cloneGraph(graph1)
    result_adjList1 = graph_to_adj_list(cloned_graph1)
    # Also check that the nodes are different objects
    if graph1:
        assert graph1 is not cloned_graph1
    assert result_adjList1 == adjList1
    print("Test Case 1 Passed")

    # Example 2
    adjList2 = [[]]
    graph2 = build_graph(adjList2)
    cloned_graph2 = sol.cloneGraph(graph2)
    result_adjList2 = graph_to_adj_list(cloned_graph2)
    if graph2:
        assert graph2 is not cloned_graph2
    assert result_adjList2 == adjList2
    print("Test Case 2 Passed")

    # Example 3
    adjList3 = []
    graph3 = build_graph(adjList3)
    cloned_graph3 = sol.cloneGraph(graph3)
    result_adjList3 = graph_to_adj_list(cloned_graph3)
    assert result_adjList3 == adjList3
    print("Test Case 3 Passed")


if __name__ == "__main__":
    tests()
