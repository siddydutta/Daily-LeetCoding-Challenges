from itertools import product
from typing import List


class Solution:
    def countSubIslands(
            self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        m, n = len(grid1), len(grid1[0])

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= m or y < 0 or y >= n or grid2[x][y] == 0:
                return
            grid2[x][y] = 0
            for dx, dy in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                dfs(x+dx, y+dy)

        # remove non-common sub-islands
        for i, j in product(range(m), range(n)):
            if grid1[i][j] == 0 and grid2[i][j] == 1:
                dfs(i, j)
        # count sub-islands
        count = 0
        for i, j in product(range(m), range(n)):
            if grid2[i][j] == 1:
                dfs(i, j)
                count += 1
        return count


def main():
    grid1 = [[1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 1, 1]]
    grid2 = [[1, 1, 1, 0, 0],
             [0, 0, 1, 1, 1],
             [0, 1, 0, 0, 0],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 1, 0]]
    assert Solution().countSubIslands(grid1, grid2) == 3

    grid1 = [[1, 0, 1, 0, 1],
             [1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [1, 0, 1, 0, 1]]
    grid2 = [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1]]
    assert Solution().countSubIslands(grid1, grid2) == 2


if __name__ == '__main__':
    main()
