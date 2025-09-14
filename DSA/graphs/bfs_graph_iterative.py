'''
implement Breadth first search (BFS) algorithm with adjacency list
for a directed graph using an iterative approach.
'''
from collections import deque


def bfs(graph, start):
    visited = set()
    result = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
        level_set = graph[node]
        for node in level_set:
            if node not in visited:
                queue.append(node)
    return result


def tests():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']


if __name__ == '__main__':
    tests()
    print("All tests passed!")
