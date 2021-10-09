# -*- coding: utf-8 -*-
from itertools import product
from typing import List


class Node:
    ''' Node for Trie data structure. '''
    def __init__(self):
        self.children = dict()
        self.is_word = False


class Trie:
    ''' Trie implementation from 208. '''
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            # Get next character node else create new node
            node = node.children.setdefault(ch, Node())
        node.is_word = True  # Final node is word
        return

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children.get(ch)
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children.get(ch)
            else:
                return False
        return True  # If all characters in trie then prefix exists


class NotSolution:
    ''' Trie based solution. Leads to TLE. '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        # Construct trie with given words
        trie = Trie()
        for word in words:
            trie.insert(word)

        def search(row: int, col: int, string: str) -> None:
            # Base cases
            if row < 0 or row >= m or col < 0 or col >= n:
                return  # Out of bounds of board
            if not board[row][col]:
                return

            ch = board[row][col]
            string += ch
            if not trie.startsWith(string):
                return
            if trie.search(string):
                result.add(string)

            board[row][col] = None
            search(row-1, col, string)
            search(row+1, col, string)
            search(row, col-1, string)
            search(row, col+1, string)
            board[row][col] = ch

        result = set()
        for i, j in product(range(m), range(n)):
            search(i, j, "")
        return list(result)


class Solution:
    ''' Trie based solution. Based on 79 and 208. '''
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        # Construct trie with given words
        trie = Trie()
        for word in words:
            trie.insert(word)

        def search(row: int, col: int, node: Node, word: str) -> None:
            ''' DFS search. '''
            # Base cases
            if row < 0 or row >= m or col < 0 or col >= n:
                return  # Out of bounds of board
            if not board[row][col]:
                return
            if node.is_word:
                result.append(word)
                node.is_word = False  # To avoid overlapping prefixes

            ch = board[row][col]
            if ch not in node.children:
                return  # Don't proceed
            board[row][col] = None
            search(row-1, col, node.children.get(ch), word+ch)
            search(row+1, col, node.children.get(ch), word+ch)
            search(row, col-1, node.children.get(ch), word+ch)
            search(row, col+1, node.children.get(ch), word+ch)
            board[row][col] = ch

            # Edge case
            if node.children.get(ch).is_word:
                result.append(word+ch)
                node.children.get(ch).is_word = False

        result = list()
        for i, j in product(range(m), range(n)):
            search(i, j, trie.root, "")
        return result


def main():
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain"]
    assert Solution().findWords(board, words) == ["eat", "oath"] \
        or Solution().findWords(board, words) == ["oath", "eat"]

    board = [['a', 'b'],
             ['c', 'd']]
    words = ["abcb"]
    assert Solution().findWords(board, words) == []

    board = [['o', 'a', 'b', 'n'],
             ['o', 't', 'a', 'e'],
             ['a', 'h', 'k', 'r'],
             ['a', 'f', 'l', 'v']]
    words = ["oa", "oaa"]
    assert Solution().findWords(board, words) == ["oa", "oaa"] \
        or Solution().findWords(board, words) == ["oaa", "oa"]

    board = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
             ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']]
    words = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa",
             "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    assert set(Solution().findWords(board, words)) == set(words)

    board = [['a']]
    words = ["a"]
    assert Solution().findWords(board, words) == ["a"]


if __name__ == '__main__':
    main()
