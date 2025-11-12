from collections import deque
from typing import Optional
'''
1. The Intuition

Imagine you have a list of university courses and their prerequisites.
You can't take "Algorithms" before you've taken "Data Structures."
A topological sort is simply an ordered list of all the courses you
need to take, from start to finish, without violating any prerequisite
rules.

The core idea is simple:
1. Find a course that has no prerequisites. You can definitely take
    this one first.
2. "Take" that course. Add it to your final ordered list.
3. By taking it, you have now fulfilled that prerequisite for other
    courses. So, you go to all the courses that depended on the one
    you just took and "cross off" that requirement.
4. Now, look again: is there another course that now has no remaining
   prerequisites? If so, repeat the process.
5. You keep doing this—finding a course with no remaining prerequisites,
   taking it, and updating the requirements for other courses—until
   you've taken them all.

The final list of courses in the order you took them is a valid topological
sort. If at any point you can't find a course with zero remaining
prerequisites, but you still have courses left to take, it means there's a
circular dependency (e.g., Course A requires B, and Course B requires A).
This is called a cycle, and a topological sort is not possible.
'''
'''
Finding a cycle in a DAG using Breadcrumbs analogy
The Intuition: Breadcrumbs for Your Walk

  Imagine the graph is a large, complex cave system with one-way passages.
  You want to find out if there's any path that leads you back to where you
  started (a cycle). To do this, you use two colors of breadcrumbs:

1. Grey Breadcrumbs (The `grey_set`): You drop these along the single,
   continuous path you are currently walking. If you enter cave A,
   then go to B, then to C, you'll have grey breadcrumbs in A, B, and C.
   This set represents the nodes in your current recursion stack—the path
   you took to get where you are right now.

2. Black Breadcrumbs (The `black_set`): You drop these in a cave only
   after you have explored every single passage leading out of it and
   have found no cycles. A black breadcrumb means "This area is fully
   explored and safe. You don't need to check it again."

The Rule for Detecting a Cycle is Simple:
If, during your walk, you encounter a passage that leads to a cave that
already has a grey breadcrumb in it, you've found a cycle. You've stumbled
upon your own current path.

Encountering a black breadcrumb is fine—it just means you've found a
different way to a previously cleared area.
'''
'''
The main intutition is to do these things before the actual algorithm
starts the DFS on the graph:
1. Find the indegrees of all the nodes in the graph. maintain the count
of indegrees against each node in the graph upfront. Maybe in a dict.
2. maintain a separate queue where all the nodes that have indegree 0,
get added to.
3. Start to pop the node from the queue, and visit the neighbours of
that node, and everytime you visit a neighbour, decrement their
indegree by 1.
4. at the end of each iteration, check for any node that has become
indegree 0, and if yes, add it to the queue.
5. when the queue is empty, algorithm finishes.
'''


def dfs(graph, node, visiting, visited, result, cycle):
    if node in visiting:
        print("Cycle Detected. Topological sort not possible")
        cycle = True
        return (result, cycle)
    if node in visited:
        return (result, cycle)
    visiting.add(node)
    for neighbour in graph[node]:
        res, cyc = dfs(graph, neighbour, visiting, visited, result, cycle)
        if cyc:
            return (res, cyc)
    visiting.remove(node)
    visited.add(node)
    result.appendleft(node)
    return (result, cycle)


def topological_sort_dfs(graph) -> Optional[list]:
    if not graph:
        print("EMPTY GRAPH")
        return []
    nodes = list(graph.keys())
    visiting = set()
    visited = set()
    result = deque()
    cycle = False
    for node in nodes:
        if node in visited:
            continue
        answer, cycle = dfs(graph, node, visiting, visited, result, cycle)
        if cycle:
            print("Not possible. Cycle detected")
            return None
    print(f"DFS Topological sort is {list(answer)}")
    return list(answer)


def indegree_count(graph) -> dict:
    '''calculates indegree value for all nodes'''
    # initialize all nodes with 0 first
    indegree_dict = {node: 0 for node in graph}
    # increment indegree by 1 for all occurences in the edges
    for node in graph:
        for neighbour in graph[node]:
            indegree_dict[neighbour] += 1
    return indegree_dict


def topological_sort_kahn(graph) -> Optional[list}:
    if not graph:
        return []
    indegree_dict = indegree_count(graph)
    # print(f"Indegree dict for graph is {indegree_dict}")
    init_nodes = [node for node, val in indegree_dict.items() if val == 0]
    queue = deque(init_nodes)  # to keep all indegree 0 nodes
    result = []  # topologically sorted list to return
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbour in graph[node]:
            indegree_dict[neighbour] -= 1
            if indegree_dict[neighbour] == 0:
                queue.append(neighbour)
    if len(result) != len(indegree_dict):
        return None
    return result


def tests():
    # 1. Simple DAG (courses with prerequisites)
    # prerequisites are keys, values are courses
    graph1 = {
        'Data Structures': ['Algorithms', 'Databases'],
        'Algorithms': ['AI'],
        'Databases': ['AI', 'Web'],
        'AI': [],
        'Web': []
        }
    # Valid topological order (one possible order)
    result1 = topological_sort_kahn(graph1)
    assert result1.index('Data Structures') < result1.index('Algorithms')
    assert result1.index('Data Structures') < result1.index('Databases')
    assert result1.index('Algorithms') < result1.index('AI')
    assert result1.index('Databases') < result1.index('AI')
    assert result1.index('Databases') < result1.index('Web')
    result11 = topological_sort_dfs(graph1)
    assert result11.index('Data Structures') < result11.index('Algorithms')
    assert result11.index('Data Structures') < result11.index('Databases')
    assert result11.index('Algorithms') < result11.index('AI')
    assert result11.index('Databases') < result11.index('AI')
    assert result11.index('Databases') < result11.index('Web')

    # 2. Graph with a cycle (should detect cycle)
    graph2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'],  # cycle: A -> B -> C -> A
    }
    result = topological_sort_kahn(graph2)
    assert result is None
    result2 = topological_sort_dfs(graph2)
    assert result2 is None

    # 3. Disconnected graph (multiple independent courses)
    graph3 = {
        'Math': [],
        'Physics': [],
        'Chemistry': [],
    }
    result3 = topological_sort_kahn(graph3)
    assert set(result3) == {'Math', 'Physics', 'Chemistry'}
    result31 = topological_sort_dfs(graph3)
    assert set(result31) == {'Math', 'Physics', 'Chemistry'}

    # 4. Single node graph
    graph4 = {
        'Solo': [],
    }
    result4 = topological_sort_kahn(graph4)
    assert result4 == ['Solo']
    result41 = topological_sort_dfs(graph4)
    assert result41 == ['Solo']

    # 5. Empty graph
    graph5 = {}
    result5 = topological_sort_kahn(graph5)
    assert result5 == []
    result51 = topological_sort_dfs(graph5)
    assert result51 == []

    print("All topological sort tests passed!")


if __name__ == '__main__':
    tests()
