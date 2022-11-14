from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited, n_islands = [False for _ in range(len(stones))], int()

        def dfs(row: List[int]) -> None:
            for i, nr in enumerate(stones):
                if not visited[i] and (row[0] == nr[0] or row[1] == nr[1]):
                    visited[i] = True
                    dfs(nr)

        for i, row in enumerate(stones):
            if not visited[i]:
                visited[i] = True
                dfs(row)
                n_islands += 1
        return len(stones) - n_islands


def main():
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    assert Solution().removeStones(stones) == 5

    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    assert Solution().removeStones(stones) == 3


if __name__ == '__main__':
    main()
