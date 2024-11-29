from heapq import heappop, heappush
from typing import List


class Solution:
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        min_heap = [(0, 0, 0)]  # (time, i, j)
        visited = {(0, 0)}

        while min_heap:
            time, x, y = heappop(min_heap)
            if x == m-1 and y == n-1:
                return time

            for dx, dy in self.DIRS:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < m and 0 <= ny < n) or (nx, ny) in visited:
                    continue
                wait = int((grid[nx][ny]-time) % 2 == 0)
                next_time = max(time+1, grid[nx][ny]+wait)
                heappush(min_heap, (next_time, nx, ny))
                visited.add((nx, ny))

        return -1


def main():
    grid = [[0, 1, 3, 2],
            [5, 1, 2, 5],
            [4, 3, 8, 6]]
    assert Solution().minimumTime(grid) == 7

    grid = [[0, 2, 4],
            [3, 2, 1],
            [1, 0, 4]]
    assert Solution().minimumTime(grid) == -1


if __name__ == '__main__':
    main()
