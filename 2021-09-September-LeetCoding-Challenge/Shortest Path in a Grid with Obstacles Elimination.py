# -*- coding: utf-8 -*-
from collections import deque
from functools import lru_cache
from math import inf
from typing import List


class NotSolution:
    ''' DFS Solution, leads to TLE. '''
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        min_steps = inf
        visited = set()

        @lru_cache(None)
        def dfs(x: int, y: int, r: int, s: int) -> None:
            if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or r > k:
                return

            if x == m-1 and y == n-1:
                nonlocal min_steps
                min_steps = min(min_steps, s)  # Update minimum

            r += grid[x][y]  # Update obstacles, if any
            visited.add((x, y))  # Mark cell as visited
            dfs(x-1, y, r, s+1)
            dfs(x+1, y, r, s+1)
            dfs(x, y+1, r, s+1)
            dfs(x, y-1, r, s+1)
            visited.remove((x, y))  # For backtracking

        dfs(0, 0, 0, 0)
        return min_steps if min_steps != inf else -1


class Solution:
    ''' BFS Solution. '''
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, k)])  # Data Structure: (x, y, obstacles)
        visited = set()
        visited.add((0, 0, k))

        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y, k = queue.popleft()
                if x == m-1 and y == n-1:
                    return steps

                for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if dx < 0 or dx >= m or dy < 0 or dy >= n:
                        continue
                    dk = k - grid[dx][dy]
                    next_state = (dx, dy, dk)
                    if dk >= 0 and next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)
            steps += 1

        return -1


def main():
    grid = [[0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0]]
    k = 1
    assert Solution().shortestPath(grid, k) == 6

    grid = [[0, 1, 1],
            [1, 1, 1],
            [1, 0, 0]]
    k = 1
    assert Solution().shortestPath(grid, k) == -1

    grid = [[0, 1, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 0]]
    k = 18
    assert Solution().shortestPath(grid, k) == 7


if __name__ == '__main__':
    main()
