# -*- coding: utf-8 -*-
from itertools import product
from typing import List


class Solution:
    ''' DFS based solution. '''
    def __dfs(self, board: List[List[str]], x: int, y: int) -> None:
        if 0 <= x < self.m and 0 <= y < self.n and board[x][y] == 'O':
            board[x][y] = None  # Border cell
            self.__dfs(board, x+1, y)
            self.__dfs(board, x-1, y)
            self.__dfs(board, x, y+1)
            self.__dfs(board, x, y-1)

    def solve(self, board: List[List[str]]) -> None:
        self.m, self.n = len(board), len(board[0])

        for row, col in product([0, self.m-1], range(self.n)):
            self.__dfs(board, row, col)  # First and last row
        for row, col in product(range(self.m), [0, self.n-1]):
            self.__dfs(board, row, col)  # First and last column

        for row, col in product(range(self.m), range(self.n)):
            if board[row][col] != 'X':
                board[row][col] = 'X' if board[row][col] == 'O' else 'O'

        return board


def main():
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    assert Solution().solve(board) == [['X', 'X', 'X', 'X'],
                                       ['X', 'X', 'X', 'X'],
                                       ['X', 'X', 'X', 'X'],
                                       ['X', 'O', 'X', 'X']]

    board = [['X']]
    assert Solution().solve(board) == [['X']]


if __name__ == '__main__':
    main()
