from collections import deque
from itertools import product
from typing import List


class Solution:

    DIRECTIONS = ((0, 1), (-1, 0), (1, 0), (0, -1))

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        matrix = [[None]*n for _ in range(m)]
        queue = deque([])

        for x, y in product(range(m), range(n)):
            if isWater[x][y]:
                matrix[x][y] = 0
                queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            for dx, dy in self.DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] is None:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx, ny))
        return matrix


def main():
    isWater = [[0, 1],
               [0, 0]]
    assert Solution().highestPeak(isWater) == [[1, 0],
                                               [2, 1]]

    isWater = [[0, 0, 1],
               [1, 0, 0],
               [0, 0, 0]]
    assert Solution().highestPeak(isWater) == [[1, 1, 0],
                                               [0, 1, 1],
                                               [1, 2, 2]]


if __name__ == '__main__':
    main()
