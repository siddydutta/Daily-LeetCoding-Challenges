from functools import lru_cache
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row: int, col: int) -> int:
            if row == m:
                # ball is out of the box
                return col

            if grid[row][col] == 1:
                # if current box is 1, box to the right must be 1
                if col+1 < n and grid[row][col+1] == 1:
                    return dfs(row+1, col+1)
                else:
                    return -1
            if grid[row][col] == -1:
                # if current box is -1, box to the left must be -1
                if col-1 >= 0 and grid[row][col-1] == -1:
                    return dfs(row+1, col-1)
                else:
                    return -1

        return [dfs(0, i) for i in range(n)]


def main():
    grid = [[1, 1, 1, -1, -1],
            [1, 1, 1, -1, -1],
            [-1, -1, -1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1]]
    assert Solution().findBall(grid) == [1, -1, -1, -1, -1]

    grid = [[-1]]
    assert Solution().findBall(grid) == [-1]

    grid = [[1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1],
            [1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1]]
    assert Solution().findBall(grid) == [0, 1, 2, 3, 4, -1]


if __name__ == '__main__':
    main()
