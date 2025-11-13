from collections import deque
from typing import List

'''
A gene string can be represented by an 8-character
long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene
string startGene to a gene string endGene where one
mutation is defined as one single character changed in
the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the
valid gene mutations. A gene must be in bank to make it
a valid gene string.

Given the two gene strings startGene and endGene and
the gene bank bank, return the minimum number of
mutations needed to mutate from startGene to endGene.
If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid,
so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA",
bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA",
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:
0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the
characters ['A', 'C', 'G', 'T'].
'''
'''
This problem is a great example of how a seemingly
domain-specific problem can be modeled as a classic
graph traversal.

Key Insight: It's a Shortest Path Problem

The prompt asks for the "minimum number of mutations."
This is a classic signal that the problem can be
solved by finding the shortest path in a graph.

Since each mutation counts as exactly one step,
we are dealing with an unweighted graph. The best
algorithm for finding the shortest path in an
unweighted graph is Breadth-First Search (BFS).

Modeling the Problem as a Graph

Let's define what our graph looks like:

* Nodes (Vertices): Each valid gene string is a node.
  The startGene is our starting node, and the other
  nodes are all the genes in the bank.
* Edges: An edge exists between two gene nodes if you
  can get from one to the other in a single mutation.
  In other words, two genes are connected if they differ
  by exactly one character.

The question now becomes: "What is the length of the
shortest path from the `startGene` node to the
`endGene` node?"

The BFS Strategy

We will explore the graph layer by layer, starting
from the startGene.

1. Queue: We'll use a queue to keep track of the genes
   we need to visit. We'll store tuples of
   (current_gene, number_of_mutations).
2. Visited Set: To avoid re-processing the same gene
   and getting stuck in cycles, we'll use a set to keep
   track of the genes we've already added to our queue.
3. Bank Set: The bank is a list, and checking for
   membership in a list is slow. We can convert it into
   a set at the beginning for near-instant lookups.

The Algorithm Steps

1. Initialization:
    * Convert the bank list into a set for fast lookups.
    * Check an edge case: If endGene is not in the bank,
      it's impossible to reach, so return -1.
    * Create a queue and add the starting point:
      queue.append((startGene, 0)).
    * Create a visited set and add the starting gene:
      visited.add(startGene).

2. BFS Loop (Level-by-Level Exploration):
    * While the queue is not empty, dequeue the next
      gene to process: current_gene, num_mutations.
    * If current_gene is our endGene, we've found the
      shortest path! Return num_mutations.

3. Find Valid Neighbors (The Core Logic):
    * This is the most interesting part. We need to
      find all valid, unvisited genes that are one
      mutation away from current_gene.
    * A simple way to do this is to iterate through
      every gene in the bank and check if it's one
      character different from current_gene.
    * If a bank_gene is a valid neighbor (one character
      difference) and has not been visited:
        * Add it to the visited set.
        * Enqueue it with an incremented mutation
          count: queue.append((bank_gene, num_mutations + 1)).

4. Termination:
    * If the queue becomes empty and we haven't found
      the endGene, it means the end is unreachable from
      the start. Return -1.

So, the intuition is to re-frame the problem as a search
for the shortest path in a state graph, and then apply
BFS to systematically explore all possible mutation paths,
guaranteeing that the first time you find the endGene,
you've done so in the minimum number of steps.
'''


class Solution:
    def minMutation(
            self, startGene: str, endGene: str, bank: List[str]
    ) -> int:
        steps = 0
        queue = deque([(steps, startGene)])
        visited = {startGene}
        while queue:
            steps, new_start = queue.popleft()
            for gene in bank:
                if gene not in visited\
                        and self.difference_genes(new_start, gene):
                    if gene == endGene:
                        return steps + 1
                    else:
                        visited.add(gene)
                        queue.append((steps + 1, gene))
        return -1

    def difference_genes(self, str1, str2):
        diff_count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1


def tests():
    sol = Solution()

    # Example 1
    startGene1 = "AACCGGTT"
    endGene1 = "AACCGGTA"
    bank1 = ["AACCGGTA"]
    assert sol.minMutation(startGene1, endGene1, bank1) == 1
    print("Test Case 1 passed")

    # Example 2
    startGene2 = "AACCGGTT"
    endGene2 = "AAACGGTA"
    bank2 = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    assert sol.minMutation(startGene2, endGene2, bank2) == 2
    print("Test Case 2 passed")


if __name__ == "__main__":
    tests()
