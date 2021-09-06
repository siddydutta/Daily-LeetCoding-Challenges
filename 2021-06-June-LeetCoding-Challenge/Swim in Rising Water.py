# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    This solution uses a DFS approach to check if it is possible to reach
    grid square (N-1, N-1) from (0, 0) at a particular time t.
    To find the ideal time t, a binary search approach is used.
    Time Complexity: n^2 for DFS and log n for BS -> O(n^2 log n)
    '''
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)  # NxN grid
        minDepth = 0
        maxDepth = N**2 - 1  # According to constraints

        def dfs(x: int, y: int) -> None:
            if not visited[x][y] and grid[x][y] <= midDepth:
                # We can access grid at current depth t
                visited[x][y] = True
                if x-1 >= 0:
                    dfs(x-1, y)  # Move left
                if x+1 < N:
                    dfs(x+1, y)  # Move right
                if y-1 >= 0:
                    dfs(x, y-1)  # Move top
                if y+1 < N:
                    dfs(x, y+1)  # Move bottom

        while minDepth < maxDepth:
            midDepth = (minDepth + maxDepth) // 2
            visited = [[False]*N for _ in range(N)]
            dfs(0, 0)  # Start from first grid square with minDepth
            if visited[-1][-1]:
                # We can reach the last grid square
                maxDepth = midDepth
            else:
                # We cannot reach the last grid square with current depth
                minDepth = midDepth + 1

        return minDepth


def main():
    obj = Solution()
    # grid[i][j] represents the elevation at that point (i,j)
    grid = [[0, 2],
            [1, 3]]
    assert obj.swimInWater(grid) == 3

    grid = [[0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]]
    assert obj.swimInWater(grid) == 16


if __name__ == '__main__':
    main()
