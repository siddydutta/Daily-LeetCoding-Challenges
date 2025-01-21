from itertools import accumulate
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row1 = list(accumulate(grid[0][::-1]))[::-1] + [0]  # postfix sums
        row2 = [0] + list(accumulate(grid[1]))  # prefix sums

        res = float('inf')
        for i in range(len(grid[0])):
            # find col where robot 1 changes rows
            top_points = row1[i+1]
            bottom_points = row2[i]
            # robot1 wants to minimize what robot2 can maximize
            res = min(res, max(top_points, bottom_points))
        return res


def main():
    grid = [[2, 5, 4],
            [1, 5, 1]]
    assert Solution().gridGame(grid) == 4

    grid = [[3, 3, 1],
            [8, 5, 2]]
    assert Solution().gridGame(grid) == 4

    grid = [[1, 3, 1, 15],
            [1, 3, 3, 1]]
    assert Solution().gridGame(grid) == 7


if __name__ == '__main__':
    main()
