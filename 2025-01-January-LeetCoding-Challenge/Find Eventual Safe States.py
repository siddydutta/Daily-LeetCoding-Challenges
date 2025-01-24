from enum import Enum
from functools import lru_cache
from typing import List


class State(Enum):
    SAFE = 0
    UNSAFE = 1


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [None] * n

        @lru_cache(n)
        def dfs(node: int) -> bool:
            nonlocal state
            if state[node] is not None:
                return state[node] == State.SAFE
            state[node] = State.UNSAFE
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            state[node] = State.SAFE
            return True

        return list(filter(dfs, range(n)))


def main():
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    assert Solution().eventualSafeNodes(graph) == [2, 4, 5, 6]

    graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    assert Solution().eventualSafeNodes(graph) == [4]


if __name__ == '__main__':
    main()
