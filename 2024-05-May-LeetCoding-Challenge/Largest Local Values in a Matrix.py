from typing import List


class Solution:
    DELTA = ((-1, -1), (-1, 0), (-1, 1),
             (0, -1), (0, 0), (0, 1),
             (1, -1), (1, 0), (1, 1))

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        return [
            [
                max(grid[i+dx][j+dy] for dx, dy in self.DELTA)
                for j in range(1, n-1)
            ]
            for i in range(1, n-1)
        ]


def main():
    grid = [[9, 9, 8, 1],
            [5, 6, 2, 6],
            [8, 2, 6, 4],
            [6, 2, 2, 2]]
    assert Solution().largestLocal(grid) == [[9, 9],
                                             [8, 6]]

    grid = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]
    assert Solution().largestLocal(grid) == [[2, 2, 2],
                                             [2, 2, 2],
                                             [2, 2, 2]]


if __name__ == '__main__':
    main()
