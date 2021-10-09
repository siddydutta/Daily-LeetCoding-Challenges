# -*- coding: utf-8 -*-
from itertools import product
from typing import List


class Solution:
    ''' Backtracking with DFS based solution. '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)

        def search(row: int, col: int, index: int) -> bool:
            # Base cases
            if index == length:
                return True  # Word found
            if row < 0 or row >= m or col < 0 or col >= n:
                return  # Out of bounds of board

            ch = board[row][col]
            if ch != word[index]:
                return False  # Expected character not found

            board[row][col] = None  # Mark as visited
            res = search(row-1, col, index+1) \
                    or search(row+1, col, index+1) \
                    or search(row, col-1, index+1) \
                    or search(row, col+1, index+1)
            board[row][col] = ch  # Reset board cell for backtracking
            return res

        for i, j in product(range(m), range(n)):
            # Start search from each cell in the board
            if search(i, j, 0):
                return True
        return False


def main():
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    assert Solution().exist(board, word)

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "SEE"
    assert Solution().exist(board, word)

    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCB"
    assert not Solution().exist(board, word)

    board = [["a"]]
    word = "a"
    assert Solution().exist(board, word)


if __name__ == '__main__':
    main()
