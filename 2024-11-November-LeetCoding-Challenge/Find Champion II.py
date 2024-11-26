from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degrees = [0] * n
        for _, v in edges:
            in_degrees[v] += 1
        champion = None
        for i in range(n):
            if in_degrees[i] == 0:
                if champion is not None:
                    return -1
                champion = i
        return champion


def main():
    n = 3
    edges = [[0, 1], [1, 2]]
    assert Solution().findChampion(n, edges) == 0

    n = 4
    edges = [[0, 2], [1, 3], [1, 2]]
    assert Solution().findChampion(n, edges) == -1


if __name__ == '__main__':
    main()
