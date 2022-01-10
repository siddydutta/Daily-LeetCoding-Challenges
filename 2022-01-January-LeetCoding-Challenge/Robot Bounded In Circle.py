# -*- coding: utf-8 -*-
class Solution:
    def isRobotBounded(self, instructions):
        ''' Simulation based answer. '''
        x, y = 0, 0  # Initial robot starting position
        dx, dy = 0, 1  # Initially the robot faces north
        # Repeating the instructions four times should return robot to origin
        for instr in 4*instructions:
            # Move robot
            if instr == "G":
                x, y = x+dx, y+dy
            # Change direction
            elif instr == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx

        return x == 0 and y == 0  # Check if robot is back at origin


def main():
    instructions = "GGLLGG"
    assert Solution().isRobotBounded(instructions)

    instructions = "GG"
    assert not Solution().isRobotBounded(instructions)

    instructions = "GL"
    assert Solution().isRobotBounded(instructions)


if __name__ == '__main__':
    main()
