def dfs(graph, start_node):
    '''
    return the resulting list of nodes by traversing the graph
    depth first
    '''
    node = start_node
    visited = set()
    result = []
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            result.append(node)
            visited.add(node)
        neighbours = graph[node]
        for neighbour in reversed(neighbours):
            if neighbour not in visited:
                stack.append(neighbour)
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
    print(f"result is {result}")
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

    graph_disconnected = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': [],
        'D': [],
        'G': ['H'],
        'H': []
    }
    assert dfs(graph_disconnected, 'A') == ['A', 'B', 'D', 'C']
    assert dfs(graph_disconnected, 'G') == ['G', 'H']


if __name__ == '__main__':
    tests()
    print("All tests passed!")
