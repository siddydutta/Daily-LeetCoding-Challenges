from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        importance = [0] * n
        for u, v in roads:
            importance[u] += 1
            importance[v] += 1
        importance.sort()
        return sum((i + 1) * importance[i] for i in range(n))


def main():
    n = 5
    roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    assert Solution().maximumImportance(n, roads) == 43

    n = 5
    roads = [[0, 3], [2, 4], [1, 3]]
    assert Solution().maximumImportance(n, roads) == 20


if __name__ == '__main__':
    main()
