from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree, out_degree = defaultdict(int), defaultdict(int)
        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        start = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start = node
                break

        result = []
        stack = [start]
        while stack:
            node = stack[-1]
            if graph[node]:
                neighbour = graph[node].pop()
                stack.append(neighbour)
            else:
                stack.pop()
                if stack:
                    result.append([stack[-1], node])
        result.reverse()
        return result


def main():
    pairs = [[5, 1], [4, 5], [11, 9], [9, 4]]
    assert Solution().validArrangement(pairs) == [[11, 9], [9, 4],
                                                  [4, 5], [5, 1]]

    pairs = [[1, 3], [3, 2], [2, 1]]
    assert Solution().validArrangement(pairs) == [[1, 3], [3, 2], [2, 1]]

    pairs = [[1, 2], [1, 3], [2, 1]]
    assert Solution().validArrangement(pairs) == [[1, 2], [2, 1], [1, 3]]


if __name__ == '__main__':
    main()
