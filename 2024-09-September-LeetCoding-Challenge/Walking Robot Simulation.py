from typing import List


class Solution:
    DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}
        x, y = 0, 0
        curr_d = 0
        max_dist = 0
        for command in commands:
            if command == -1:
                # Turn right
                curr_d = (curr_d + 1) % 4
            elif command == -2:
                # Turn left
                curr_d = (curr_d - 1) % 4
            else:
                for _ in range(command):
                    dx, dy = self.DIRECTIONS[curr_d]
                    if (x+dx, y+dy) in obstacles:
                        continue
                    x, y = x+dx, y+dy
                max_dist = max(max_dist, x**2+y**2)
        return max_dist


def main():
    commands = [4, -1, 3]
    obstacles = []
    assert Solution().robotSim(commands, obstacles) == 25

    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    assert Solution().robotSim(commands, obstacles) == 65

    commands = [6, -1, -1, 6]
    obstacles = []
    assert Solution().robotSim(commands, obstacles) == 36


if __name__ == '__main__':
    main()
