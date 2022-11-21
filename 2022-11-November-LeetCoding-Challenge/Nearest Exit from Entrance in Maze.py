from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        queue = deque([(entrance, 0)])

        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            (x, y), steps = queue.popleft()
            if (x == 0 or y == 0 or x == m-1 or y == n-1) \
                    and [x, y] != entrance:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'
                    queue.append(((nx, ny), steps+1))
        return -1


def main():
    maze = [['+', '+', '.', '+'], ['.', '.', '.', '+'], ['+', '+', '+', '.']]
    entrance = [1, 2]
    assert Solution().nearestExit(maze, entrance) == 1

    maze = [['+', '+', '+'], ['.', '.', '.'], ['+', '+', '+']]
    entrance = [1, 0]
    assert Solution().nearestExit(maze, entrance) == 2

    maze = [['.', '+']]
    entrance = [0, 0]
    assert Solution().nearestExit(maze, entrance) == -1


if __name__ == '__main__':
    main()
