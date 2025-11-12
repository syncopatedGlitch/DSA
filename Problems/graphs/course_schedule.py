from typing import List
from collections import deque
'''
There are a total of numCourses courses you have to
take, labeled from 0 to numCourses - 1. You are given
an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take
course 0 you have to first take course 1.
Return true if you can finish all courses.
Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0.
So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished
course 1. So it is impossible.
'''
'''
topological sort problem
'''


# class Solution:
#     def canFinish(
#             self, numCourses: int, prerequisites: List[List[int]]
#     ) -> bool:
#         # create graph from prerequisites List
#         # use adjacency list representation
#         self.graph = {}
#         for val in range(numCourses):
#             self.graph[val] = []
#         for course, prerequisite in prerequisites:
#             self.graph[prerequisite].append(course)
#         print(f"self.graph is {self.graph}")
#         # create the indegree dict
#         indegree_dict = {node: 0 for node in self.graph.keys()}
#         print(f"Indegree dict initialized: {indegree_dict}")
#         for node in self.graph:
#             for neighbour in self.graph[node]:
#                 indegree_dict[neighbour] += 1
#         # as an initialization step, create queue and add
#         # indegree 0 nodes to it
#         init_nodes = [
#             node for node, val in indegree_dict.items()
#             if val == 0
#         ]
#         if not init_nodes:
#             return False
#         queue = deque(init_nodes)
#         result = []
#         # start the Kahn's algorithm for topological sort
#         while queue:
#             node = queue.popleft()
#             result.append(node)
#             for neighbour in self.graph[node]:
#                 indegree_dict[neighbour] -= 1
#                 if indegree_dict[neighbour] == 0:
#                     queue.append(neighbour)
#         if len(result) != len(indegree_dict):
#             return False
#         return True


class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        self.graph = {}
        for val in range(numCourses):
            self.graph[val] = []
        for course, prerequisite in prerequisites:
            self.graph[prerequisite].append(course)
        visiting = set()
        visited = set()
        answer = None
        for node in self.graph:
            if node in visited:
                continue
            answer = self.dfs(node, visiting, visited)
        return answer

    def dfs(self, node, visiting, visited) -> bool:
        if node in visiting:
            return False
        if node in visited:
            return True
        visiting.add(node)
        for neighbour in self.graph[node]:
            self.dfs(neighbour, visiting, visited)
        visiting.remove(node)
        visited.add(node)
        return True

def tests():
    sol = Solution()

    # Example 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    assert sol.canFinish(numCourses1, prerequisites1) is True
    print("Test Case 1 Passed")

    # Example 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    assert sol.canFinish(numCourses2, prerequisites2) is False
    print("Test Case 2 Passed")


if __name__ == "__main__":
    tests()
