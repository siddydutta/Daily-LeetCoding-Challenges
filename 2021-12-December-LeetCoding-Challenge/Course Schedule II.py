# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        ''' Topological sort using recursive dfs. '''
        # Make graph
        graph = defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)

        def dfs(node: int) -> bool:
            nonlocal visited
            if visited[node]:
                return False  # Cycle detected
            if visited[node] is None:
                return True  # Node is complete
            visited[node] = True  # Mark node as visited
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            visited[node] = None  # Mark node as completed
            nonlocal result
            result.append(node)
            return True

        visited = [0 for _ in range(numCourses)]
        result = list()
        for n in range(numCourses):
            if not dfs(n):
                return list()
        return result


def main():
    numCourses = 2
    prerequisites = [[1, 0]]
    assert Solution().findOrder(numCourses, prerequisites) == [0, 1]

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    assert Solution().findOrder(numCourses, prerequisites) == [0, 1, 2, 3]

    numCourses = 1
    prerequisites = []
    assert Solution().findOrder(numCourses, prerequisites) == [0]


if __name__ == '__main__':
    main()
