'''
1. What is a Minimum Spanning Tree?

  Let's break down the name:

   * Tree: In graph theory, a tree is a connected graph that has no cycles.
   Think of a family tree; you can't be your own great-grandfather.
   * Spanning: A "spanning tree" is a tree that connects all the vertices
   (nodes) in a larger graph. It forms a skeleton of the original graph,
   ensuring every node is reachable from every other node.
   * Minimum: This applies to weighted graphs, where each edge has a cost
   or weight (like distance, price, or time). A Minimum Spanning Tree is
   the spanning tree with the lowest possible total weight.

  So, a Minimum Spanning Tree (MST) is a subset of the edges from a connected,
  weighted, and undirected graph that connects all the vertices together,
  with no cycles, and with the minimum possible total edge weight.

  Imagine you have several cities and the cost to build a road between any
  two of them. The MST would represent the cheapest possible road network
  that connects all the cities.

The Intuition (How to Find an MST)

  The beautiful thing about MST algorithms is that they are greedy.
  A greedy algorithm makes the locally optimal choice at each step,
  and in this case, it actually leads to the globally optimal solution.

  Kruskal's Algorithm:
   * Intuition: Build a forest of trees that gradually merge into one.
   * Process:
       1. Consider all the edges in the entire graph, sorted from
          cheapest to most expensive.
       2. Go through the sorted edges. For each edge, if adding it
          to your collection does not form a cycle, add it.
       3. If it does form a cycle, discard it and move to the next
          cheapest edge.
       4. Stop when you have added V-1 edges (where V is the number
          of vertices), as this is the number of edges in a spanning tree.
'''
'''
The Union-Find data structure (also called Disjoint Set Union or DSU) is
a fascinating and powerful tool. Let's break it down in detail, focusing
on the union and find operations and the critical role of the rank
optimization.

The Core Idea: Managing Groups
Imagine you have a set of elements, and you want to dynamically group them
into disjoint (non-overlapping) sets. Union-Find is designed to do two
things very efficiently:

1. `find(element)`: Determine which group an element belongs to.
2. `union(element1, element2)`: Merge the groups that two elements belong to.

To do this, we represent our groups as trees. Each tree corresponds to one
group. The root of the tree is the unique identifier or "representative"
of that group.

Our main data structure is a parent dictionary (or array) where parent[i]
stores the parent of element i. If parent[i] == i, then i is a root.

---

The Naive Approach (and why it's flawed)

Let's start without any optimizations.

`find(i)`: To find the group representative for i, we just travel up the
tree by following the parent pointers until we hit a root.

`union(i, j)`: We find the root of i (let's call it root_i) and the
root of j (root_j). Then, we simply make one root the parent of the other.
For example, we could always set parent[root_i] = root_j.

Example and Problem:

Let's say we have elements {0, 1, 2, 3}. Initially, each is its own root.
parent = {0:0, 1:1, 2:2, 3:3}

Pictorially:
[0]  [1]  [2]  [3]

Now, let's perform some unions:
1. union(0, 1): root_0 is 0, root_1 is 1. We set parent[0] = 1.
    [2]  [3]    1
                |
                0
2. union(1, 2): root_1 is 1, root_2 is 2. We set parent[1] = 2.
    [3]      2
            |
            1
            |
            0
3. union(2, 3): root_2 is 2, root_3 is 3. We set parent[2] = 3.
    3
    |
    2
    |
    1
    |
    0

We've created a long, skinny chain. Now, if we call find(0), the code has
to traverse all the way up the chain: 0 -> 1 -> 2 -> 3. This takes a time
proportional to the number of elements, O(N). We can do much better.

---

Optimization 1: Union by Rank

This is where rank comes in. The problem above is that we created a tall,
unbalanced tree. The goal of Union by Rank is to always keep our trees as
flat (short) as possible.

The `rank` array stores the "height" or "depth" of the tree rooted at each
element.

The rule for union is modified: Always attach the root of the shorter tree
to the root of the taller tree.

Let's see how this works.

`union(i, j)` with Rank:
1. Find the roots: root_i = find(i), root_j = find(j).
2. If they are already the same root, do nothing.
3. Compare their ranks: rank[root_i] vs rank[root_j].
  * If `rank[root_i] < rank[root_j]`: root_j's tree is taller.
    So, attach root_i under root_j. The height of the combined tree is
    still just the height of root_j's tree, so no ranks need to change.
  * If `rank[root_i] > rank[root_j]`: root_i's tree is taller. Attach
    root_j under root_i.
  * If `rank[root_i] == rank[root_j]`: The trees are equally tall.
    It doesn't matter which you attach to which. Let's attach root_j
    under root_i. But now, the resulting tree is one level taller,
    so we must increment the rank of the new root: rank[root_i] += 1.

Example with Union by Rank:

Elements {0, 1, 2, 3, 4, 5}. Initially, all have rank = 0.

1. union(0, 1): Ranks are equal (0). Attach 0 to 1. parent[0]=1.
   Increment rank[1] to 1.
    1 (rank=1)
    |
    0

2. union(2, 3): Ranks are equal (0). Attach 2 to 3. parent[2]=3.
   Increment rank[3] to 1.
    1 (rank=1)      3 (rank=1)
    |               |
    0               2

3. union(0, 2): root_0 is 1, root_2 is 3. Their ranks are equal (both are 1).
   Attach 3 to 1. parent[3]=1. Increment rank[1] to 2.

        1 (rank=2)
        / \
        /   \
    0 (r=0) 3 (r=1)
            |
            2 (r=0)

Notice how the tree is much flatter than our naive example.
A find(2) operation now takes only two steps (2 -> 3 -> 1) instead of
potentially many more. Union by Rank prevents the creation of long chains.

---

Optimization 2: Path Compression

This is another powerful optimization that works on the find operation.
It's based on a simple idea: when we do a find(i), we travel up the tree
to find the root. On our way back down, we can make every node we visited
point directly to the root.

This dramatically flattens the tree for all future find operations
on those nodes.

`find(i)` with Path Compression:

1 def find(parent, i):
2     # If i is the root, return it
3     if parent[i] == i:
4         return i
5
6     # Recursively find the root
7     root = find(parent, parent[i])
8
9     # The compression step: Set my parent directly to the root
10     parent[i] = root
11
12     return root

Example with Path Compression:

Let's use the tree from our last example and call find(2).

Before `find(2)`:
    1 (root)
    / \
    0   3
        |
        2

1. find(2) is called. parent[2] is 3, not 2.
2. It recursively calls find(3). parent[3] is 1, not 3.
3. It recursively calls find(1). parent[1] is 1. It's the root! It returns 1.
4. The find(3) call receives 1 as the root. It now performs the compression
   step: parent[3] = 1. It returns 1.
5. The original find(2) call receives 1 as the root. It performs its
   compression step: parent[2] = 1.

After `find(2)`:
    1 (root)
    /|\
    / | \
    0  3  2

Look at that! The path has been completely flattened. The next time we call
find(2) or find(3), it will be an instantaneous O(1) operation,
as they now point directly to the root.

Summary

* Union-Find is a data structure for managing groups.
* A naive implementation can lead to tall, skinny trees, making find operations
  slow (O(N)).
* Union by Rank is a union optimization that keeps trees short by always
  attaching the shorter tree to the taller one. This prevents the worst-case
  chain scenario.
* Path Compression is a find optimization that flattens the tree structure by
  making every node on a path point directly to the root.
* When used together, these two optimizations make Union-Find incredibly fast,
  with an amortized time complexity that is nearly constant for all practical
  purposes. This is why it's the go-to solution for cycle detection in
  algorithms like Kruskal's.
'''
'''
In the kruskal_mst method, the rank variable is a dictionary that is created
at the very beginning of the function. It is not a single value, but a
complete data structure that maps every vertex to its current rank.

Let's break it down.

1. Initialization:
    At the start of kruskal_mst, we see this line:
    rank = {v: 0 for v in vertices}
    This creates a dictionary named rank. If our vertices are
    ['A', 'B', 'C', 'D'], this dictionary will look like this:
    rank = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    This signifies that, initially, every vertex is in its own set,
    and the "tree" for each set has a height (rank) of 0.

2. Passing to `union`:
   When we call union(parent, rank, u, v), we are passing the entire
   `rank` dictionary into the function.
    In Python, objects like dictionaries are passed by "object reference."
    This means the union function receives a reference to the exact same
    dictionary that was created in kruskal_mst. It does not get a copy.

3. Modification inside `union`:
   The union function's job is to modify the parent and rank dictionaries
   based on its logic. When the ranks of two sets are equal and they
   are merged, the union function executes this line:

   rank[i_root] += 1
   Because union is working on the original dictionary, this change is
   permanent. The rank dictionary back in the kruskal_mst function is
   now updated.
'''
'''
Data structures needed for this algo:
1. Parent dict containing mapping of each node to its parent.
2. Rank dict containing rank of each node.
3. mst_edges list to return the mst edges as result
'''


def find(parent, i):
    '''find the parent of a node and return it'''
    if parent[i] == i:
        return i
    root = find(parent, parent[i])
    parent[i] = root  # compression
    return root


def union(parent, rank, i, j):
    root_i = find(parent, i)
    root_j = find(parent, j)
    if rank[root_i] < rank[root_j]:
        parent[root_i] = root_j
    elif rank[root_j] > rank[root_i]:
        parent[root_j] = root_i
    else:
        parent[root_i] = root_j
        rank[root_j] += 1


def kruskal_mst(nodes, edges):
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    result = []
    sorted_edges = sorted(edges, key=lambda x: x[2])
    print(f"sorted edges are {sorted_edges}")
    for edge in sorted_edges:
        i, j, weight = edge
        if find(parent, i) == find(parent, j):
            continue
        union(parent, rank, i, j)
        result.append(edge)
    total_weight = 0
    for edge in result:
        _, _, weight = edge
        total_weight += weight
    print(f"mst edges are {result}")
    print(f"total weight is {total_weight}")
    return result, total_weight


def tests():
    # Test Case 1: Standard simple graph
    vertices1 = ['A', 'B', 'C', 'D', 'E', 'F']
    edges1 = [
        ('A', 'B', 4), ('A', 'C', 4),
        ('B', 'C', 2),
        ('C', 'D', 3), ('C', 'E', 2), ('C', 'F', 4),
        ('D', 'F', 3),
        ('E', 'F', 3)
    ]
    # Expected MST Edges: [('B', 'C', 2), ('C', 'E', 2), ('D', 'F', 3),
    # ('C', 'D', 3), ('A', 'B', 4)]
    # Note: ('A', 'B', 4) could be swapped for ('A', 'C', 4). The total
    # weight is key.
    mst_edges1, total_weight1 = kruskal_mst(vertices1, edges1)
    assert total_weight1 == 14
    assert len(mst_edges1) == 5  # V-1 edges

    # Test Case 2: Graph with edges of same weight
    vertices2 = ['A', 'B', 'C', 'D']
    edges2 = [
        ('A', 'B', 1), ('A', 'C', 2), ('A', 'D', 3),
        ('B', 'C', 1), ('B', 'D', 2),
        ('C', 'D', 1)
    ]
    # Expected MST Edges: [('A', 'B', 1), ('B', 'C', 1), ('C', 'D', 1)]
    mst_edges2, total_weight2 = kruskal_mst(vertices2, edges2)
    assert total_weight2 == 3
    assert len(mst_edges2) == 3

    # Test Case 3: Linear graph (already a tree)
    vertices3 = ['A', 'B', 'C', 'D']
    edges3 = [('A', 'B', 10), ('B', 'C', 20), ('C', 'D', 30)]
    mst_edges3, total_weight3 = kruskal_mst(vertices3, edges3)
    assert total_weight3 == 60
    assert len(mst_edges3) == 3
    # The set of edges should be the same as the input
    assert set(mst_edges3) == set(edges3)

    # Test Case 4: Graph with a clear cycle to be avoided
    vertices4 = ['A', 'B', 'C']
    edges4 = [('A', 'B', 1), ('B', 'C', 2), ('A', 'C', 10)]
    # The edge ('A', 'C', 10) should be discarded as it forms a cycle
    mst_edges4, total_weight4 = kruskal_mst(vertices4, edges4)
    assert total_weight4 == 3
    assert len(mst_edges4) == 2

    # Test Case 5: Single vertex
    vertices5 = ['A']
    edges5 = []
    mst_edges5, total_weight5 = kruskal_mst(vertices5, edges5)
    assert total_weight5 == 0
    assert len(mst_edges5) == 0

    # Test Case 6: Two vertices
    vertices6 = ['A', 'B']
    edges6 = [('A', 'B', 5)]
    mst_edges6, total_weight6 = kruskal_mst(vertices6, edges6)
    assert total_weight6 == 5
    assert len(mst_edges6) == 1

    print("All Kruskal's MST tests passed!")


if __name__ == '__main__':
    tests()
