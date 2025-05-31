from collections import deque


class Solution:
    def __init__(self):
        self.n = 0

    def __get_coordinates(self, position: int) -> tuple[int, int]:
        row = (position - 1) // self.n
        col = (position - 1) % self.n
        if row % 2 == 1:
            col = self.n - 1 - col
        return self.n - 1 - row, col

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        self.n = len(board)
        queue = deque([(1, 0)])  # (position, moves)
        visited = {1}
        while queue:
            position, moves = queue.popleft()
            if position == self.n * self.n:
                return moves
            for move in range(1, 7):
                new_position = position + move
                if new_position > self.n * self.n:
                    continue
                row, col = self.__get_coordinates(new_position)
                if board[row][col] != -1:
                    new_position = board[row][col]
                if new_position not in visited:
                    queue.append((new_position, moves + 1))
                    visited.add(new_position)
        return -1


def main():
    board = [[-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1],
             [-1, 15, -1, -1, -1, -1]]
    assert Solution().snakesAndLadders(board) == 4

    board = [[-1, -1],
             [-1, 3]]
    assert Solution().snakesAndLadders(board) == 1


if __name__ == '__main__':
    main()
