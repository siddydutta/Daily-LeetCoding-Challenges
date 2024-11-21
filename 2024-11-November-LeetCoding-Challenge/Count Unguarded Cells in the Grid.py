from itertools import product
from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in walls:
            grid[x][y] = 1
        for x, y in guards:
            grid[x][y] = 2

        for x, y in guards:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n and grid[nx][ny] <= 0:
                    grid[nx][ny] = -1
                    nx += dx
                    ny += dy

        unguarded = 0
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 0:
                unguarded += 1
        return unguarded


def main():
    m = 4
    n = 6
    guards = [[0, 0], [1, 1], [2, 3]]
    walls = [[0, 1], [2, 2], [1, 4]]
    assert Solution().countUnguarded(m, n, guards, walls) == 7

    m = 3
    n = 3
    guards = [[1, 1]]
    walls = [[0, 1], [1, 0], [2, 1], [1, 2]]
    assert Solution().countUnguarded(m, n, guards, walls) == 4


if __name__ == '__main__':
    main()
