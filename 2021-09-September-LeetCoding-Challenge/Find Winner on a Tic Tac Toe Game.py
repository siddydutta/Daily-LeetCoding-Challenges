# -*- coding: utf-8 -*-
from typing import List


class Solution:
    ''' Simulation based answer. '''
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None for _ in range(3)] for _ in range(3)]
        player = 'X'
        for x, y in moves:
            board[x][y] = player
            player = 'X' if player == 'O' else 'O'
            # Check rows
            for row in range(3):
                if board[row][0] and board[row][0] == board[row][1] == board[row][2]:
                    return 'A' if board[row][0] == 'X' else 'B'
            # Check cols
            for col in range(3):
                if board[0][col] and board[0][col] == board[1][col] == board[2][col]:
                    return 'A' if board[0][col] == 'X' else 'B'
            # Check diagonals
            if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
                return 'A' if board[0][0] == 'X' else 'B'
            if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
                return 'A' if board[0][2] == 'X' else 'B'

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"


def main():
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    assert Solution().tictactoe(moves) == "A"

    moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    assert Solution().tictactoe(moves) == "B"

    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    assert Solution().tictactoe(moves) == "Draw"

    moves = [[0, 0], [1, 1]]
    assert Solution().tictactoe(moves) == "Pending"


if __name__ == '__main__':
    main()
