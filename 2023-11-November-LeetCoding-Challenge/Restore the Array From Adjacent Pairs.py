from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # construct graph
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # find a starting element
        start = None
        for key, value in graph.items():
            if len(value) == 1:
                start = key
                break

        # dfs to construct restored array
        restored, visited = list(), set()
        def dfs(node: int) -> None:
            restored.append(node)
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        dfs(start)
        return restored


def main():
    adjacentPairs = [[2, 1], [3, 4], [3, 2]]
    assert Solution().restoreArray(adjacentPairs) == [1, 2, 3, 4]

    adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
    assert Solution().restoreArray(adjacentPairs) == [-2, 4, 1, -3]

    adjacentPairs = [[100000, -100000]]
    assert Solution().restoreArray(adjacentPairs) == [100000, -100000]


if __name__ == '__main__':
    main()
