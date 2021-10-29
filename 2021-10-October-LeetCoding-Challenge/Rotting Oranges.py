# -*- coding: utf-8 -*-
from collections import deque
from itertools import product
from typing import List


class Solution:
    ''' BFS Solution. '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rotten = deque()  # Queue for positions of rotten oranges
        fresh = 0  # To account for fresh oranges to avoid infinite loop
        minutes = 0

        # Initial queue is all initial rotten oranges
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 2:
                rotten.append((x, y))
            elif grid[x][y] == 1:
                fresh += 1

        while rotten and fresh > 0:
            minutes += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                # Check neighbours
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x+dx < m and 0 <= y+dy < n:
                        if grid[x+dx][y+dy] == 1:
                            grid[x+dx][y+dy] = 2
                            # Add to queue to check for next neighbours
                            rotten.append((x+dx, y+dy))
                            fresh -= 1

        return minutes if fresh == 0 else -1  # Handle edge case


def main():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert Solution().orangesRotting(grid) == 4

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert Solution().orangesRotting(grid) == -1

    grid = [[0, 2]]
    assert Solution().orangesRotting(grid) == 0


if __name__ == '__main__':
    main()
