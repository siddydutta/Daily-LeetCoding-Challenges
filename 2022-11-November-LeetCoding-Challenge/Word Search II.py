from itertools import product
from typing import List, Tuple


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

    def insert(self, word: str) -> None:
        node: TrieNode = self
        for ch in word:
            if ch not in node.children:
                # create new child node for letter
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True  # last node is end of word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct Trie
        root = TrieNode()
        for word in words:
            root.insert(word)

        def search(row: int, col: int, node: TrieNode, word: str) -> None:
            if row < 0 or col < 0 or row == m or col == n:
                return
            if board[row][col] not in node.children or (row, col) in visited:
                return

            visited.add((row, col))  # start backtracking
            # continue with next character of current word
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.is_word:
                result.append(word)
                node.is_word = False  # to prevent duplicates

            # bottom, top, right, left
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                search(row+dr, col+dc, node, word)
            visited.remove((row, col))  # end backtracking

        m, n = len(board), len(board[0])
        result, visited = list(), set()
        for i, j in product(range(m), range(n)):
            # attempt search of words from each cell
            search(i, j, root, "")
        return result


def main():
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    words = ['oath', 'pea', 'eat', 'rain']
    assert Solution().findWords(board, words) == ['oath', 'eat']

    board = [['a', 'b'],
             ['c', 'd']]
    words = ['abcb']
    assert Solution().findWords(board, words) == []


if __name__ == '__main__':
    main()
