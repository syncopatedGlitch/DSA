def dfs(graph, node, visited=None, result=None):
    num_nodes = len(graph)
    visited = visited or [False] * num_nodes
    result = result or []
    if not visited[node]:
        result.append(node)
        visited[node] = True
    for i in range(0, num_nodes):
        if graph[node][i] == 1 and not visited[i]:
            dfs(graph, i, visited, result)
    return result


def dfs_recursive(graph, start_node):
    if not graph:
        print("EMPTY GRAPH")
        return None
    result = dfs(graph, start_node)
    return result


def tests():
    graph = [
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 0, 0, 1],
    ]
    result = dfs_recursive(graph, 0)
    print(f"result is {result}")
    assert result == [0, 1, 2, 3]
    empty_graph = []
    assert dfs_recursive(empty_graph, 0) is None


if __name__ == '__main__':
    tests()
    print("All tests passed")
