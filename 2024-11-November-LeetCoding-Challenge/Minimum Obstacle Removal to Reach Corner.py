from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = map(len, (grid, grid[0]))
        distance = [[float('inf')] * n for _ in range(m)]
        distance[0][0] = 0
        queue = deque([(0, 0, 0)])
        while queue:
            o, r, c = queue.popleft()
            for i, j in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if m > i >= 0 <= j < n and distance[i][j] == float('inf'):
                    if grid[i][j] == 1:
                        distance[i][j] = o + 1
                        queue.append((o+1, i, j))
                    else:
                        distance[i][j] = o
                        queue.appendleft((o, i, j))
        return distance[-1][-1]


def main():
    grid = [[0, 1, 1],
            [1, 1, 0],
            [1, 1, 0]]
    assert Solution().minimumObstacles(grid) == 2

    grid = [[0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0]]
    assert Solution().minimumObstacles(grid) == 0


if __name__ == '__main__':
    main()
