
def dfs(graph, start_node, visited=None, result=None):
    visited = visited or set()
    result = result or []
    node = start_node
    result.append(node)
    visited.add(node)
    neighbours = graph[node]
    for neighbour in neighbours:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, result)
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
    result = dfs(graph, 'A')
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

    graph_disconnected = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': [],
        'D': [],
        'G': ['H'],
        'H': []
    }
    result = dfs(graph_disconnected, 'A')
    assert result == ['A', 'B', 'D', 'C']
    assert dfs(graph_disconnected, 'G') == ['G', 'H']


if __name__ == '__main__':
    tests()
    print("All tests passed!")
