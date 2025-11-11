from typing import List
'''
You are given an array of variable pairs equations and
an array of real numbers values, where
equations[i] = [Ai, Bi] and values[i] represent the equation
Ai / Bi = values[i]. Each Ai or Bi is a string that
represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj]
represents the jth query where you must find the answer for
Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot
be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating
the queries will not result in division by zero and that there
is no contradiction.

Note: The variables that do not occur in the list of equations
are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"]],
values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]],
values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5],
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
'''
'''
Think of each variable (like "a", "b", "c") as a node
in a graph.

An equation like a / b = 1.5 represents a directed edge
between the nodes. But it actually gives us two pieces
of information:
1. a / b = 1.5: This is a directed edge from a to b with
   a weight of 1.5.
2. b / a = 1 / 1.5: This is a directed edge from b to a
   with a weight of 1 / 1.5.

A query, like a / c = ?, becomes a graph problem:
"Find the path from node `a` to node `c` and multiply
the weights of all the edges along the way."

Why multiply? Because a / c = (a / b) * (b / c).

If you can't find a path, the answer is -1.0.

The Crucial Point for Example 2

The most confusing part of Example 2 is the variable
names: ["bc", "cd"].

You must treat `"bc"` and `"cd"` as single, unique
variable names. They are just labels. They have no
mathematical relationship to the variables "b" or "c".
The problem could have used "apple" / "banana" = 5.0
and the logic would be identical.

So, in Example 2, you have five distinct nodes:
a, b, c, bc, cd.

Let's Build the Graph for Example 2

1. ["a", "b"], value = 1.5
    * Creates edge a -> b (weight 1.5)
    * Creates edge b -> a (weight 1 / 1.5)
2. ["b", "c"], value = 2.5
    * Creates edge b -> c (weight 2.5)
    * Creates edge c -> b (weight 1 / 2.5)
3. ["bc", "cd"], value = 5.0
    * Creates edge bc -> cd (weight 5.0)
    * Creates edge cd -> bc (weight 1 / 5.0)

Notice you have two separate, disconnected groups
of nodes: (a, b, c) and (bc, cd).

Evaluating the Queries for Example 2

Now let's solve the queries by finding paths in this graph:

1. `["a", "c"]` => `a / c = ?`
    * Path: a -> b -> c
    * Calculation: (weight of a->b) * (weight of b->c)
      = 1.5 * 2.5 = `3.75`

2. `["c", "b"]` => `c / b = ?`
    * Path: c -> b (a direct edge we created)
    * Calculation: weight of c->b = 1 / 2.5 = `0.4`

3. `["bc", "cd"]` => `bc / cd = ?`
    * Path: bc -> cd (a direct edge)
    * Calculation: weight of bc->cd = `5.0`

4. `["cd", "bc"]` => `cd / bc = ?`
    * Path: cd -> bc (a direct edge)
    * Calculation: weight of cd->bc = 1 / 5.0 = `0.2`

This graph-based approach, especially the rule about
treating variables like "bc" as unique labels, is the
fundamental intuition needed to solve the problem.
'''


class Solution:
    def calcEquation(
            self,
            equations: List[List[str]],
            values: List[float],
            queries: List[List[str]]
    ) -> List[float]:
        length = len(equations)
        self.graph = {}
        for i in range(length):
            n, m = equations[i]
            val = values[i]
            if self.graph.get(n):
                existing_n = self.graph[n]
                existing_n.update({m: val})
            else:
                self.graph[n] = {m: val}
            if self.graph.get(m):
                existing_m = self.graph[m]
                existing_m.update({n: 1 / val})
            else:
                self.graph[m] = {n: 1 / val}
        result = []
        length_q = len(queries)
        for j in range(length_q):
            start, end = queries[j]
            visited = set()
            ans = self.find_path(start, end, visited)
            result.append(ans)
        return result

    def find_path(self, start, end, visited=set(), product_so_far=1.0):
        if not self.graph.get(start):
            return -1.0
        neighbors = self.graph[start]
        visited.add(start)
        if end in neighbors:
            product_so_far *= neighbors[end]
            return product_so_far
        else:
            for key, val in neighbors.items():
                if key in visited:
                    continue
                else:
                    res = self.find_path(
                        key, end, visited, product_so_far * val
                    )
                    if res == -1.0:
                        continue
                    else:
                        return res
            return -1.0


def tests():
    sol = Solution()

    # Example 1
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [
        ["a", "c"],
        ["b", "a"],
        ["a", "e"],
        ["a", "a"],
        ["x", "x"]
    ]
    expected1 = [6.0, 0.5, -1.0, 1.0, -1.0]
    result1 = sol.calcEquation(equations1, values1, queries1)
    print(f"result1 is {result1}")
    assert result1 == expected1
    print("Test Case 1 Passed")

    # Example 2
    equations2 = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values2 = [1.5, 2.5, 5.0]
    queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    expected2 = [3.75, 0.4, 5.0, 0.2]
    result2 = sol.calcEquation(equations2, values2, queries2)
    # # Comparing floats requires a tolerance
    assert all(abs(r - e) < 1e-5 for r, e in zip(result2, expected2))
    print("Test Case 2 Passed (placeholder)")

    # Example 3
    equations3 = [["a", "b"]]
    values3 = [0.5]
    queries3 = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected3 = [0.5, 2.0, -1.0, -1.0]
    result3 = sol.calcEquation(equations3, values3, queries3)
    assert result3 == expected3
    print("Test Case 3 Passed (placeholder)")


if __name__ == "__main__":
    tests()
