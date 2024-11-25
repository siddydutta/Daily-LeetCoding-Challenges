from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        start = ''.join(str(num) for row in board for num in row)
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        queue = deque([(start, start.index('0'), 0)])
        visited = {start}

        while queue:
            state, zero, steps = queue.popleft()
            if state == target:
                return steps
            for neighbor in neighbors[zero]:
                new_state = list(state)
                new_state[zero] = new_state[neighbor]
                new_state[neighbor] = new_state[zero]
                new_state = ''.join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, neighbor, steps + 1))

        return -1


def main():
    board = [[1, 2, 3],
             [4, 0, 5]]
    assert Solution().slidingPuzzle(board) == 1

    board = [[1, 2, 3],
             [5, 4, 0]]
    assert Solution().slidingPuzzle(board) == -1

    board = [[4, 1, 2],
             [5, 0, 3]]
    assert Solution().slidingPuzzle(board) == 5


if __name__ == '__main__':
    main()
