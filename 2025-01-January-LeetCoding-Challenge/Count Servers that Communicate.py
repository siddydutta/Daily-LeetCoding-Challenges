from itertools import product
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_sums, col_sums = [0] * m, [0] * n
        servers = []

        for x, y in product(range(m), range(n)):
            if grid[x][y] == 0:
                continue
            row_sums[x] += 1
            col_sums[y] += 1
            servers.append((x, y))

        count = 0
        for x, y in servers:
            if row_sums[x] > 1 or col_sums[y] > 1:
                count += 1
        return count


def main():
    grid = [[1, 0],
            [0, 1]]
    assert Solution().countServers(grid) == 0

    grid = [[1, 0],
            [1, 1]]
    assert Solution().countServers(grid) == 3

    grid = [[1, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]
    assert Solution().countServers(grid) == 4


if __name__ == '__main__':
    main()
