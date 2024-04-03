from itertools import product
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(row: int, col: int, idx: int, visited: set = set()) -> bool:
            if idx == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if board[row][col] != word[idx] or (row, col) in visited:
                return False
            visited.add((row, col))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if dfs(row+dx, col+dy, idx+1, visited):
                    return True
            visited.remove((row, col))
            return False

        for x, y in product(range(rows), range(cols)):
            if dfs(x, y, 0):
                return True
        return False


def main():
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    word = 'ABCCED'
    assert Solution().exist(board, word)

    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    word = 'SEE'
    assert Solution().exist(board, word)

    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    word = 'ABCB'
    assert not Solution().exist(board, word)
