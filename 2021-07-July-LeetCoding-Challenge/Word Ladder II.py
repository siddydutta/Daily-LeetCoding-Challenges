# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.ans = list()
        self.adj = defaultdict(list)

    def dfs(self, curr_word: str, end_word: str, sequence: List[str]) -> None:
        sequence.append(curr_word)
        if curr_word == end_word:
            self.ans.append(sequence.copy())
            sequence.pop()
            return
        for next_word in self.adj[curr_word]:
            self.dfs(next_word, end_word, sequence)
        sequence.pop()  # To backtrack

    def bfs(self, begin_word: str, words: List[str]) -> None:
        n = len(begin_word)  # All words are of the same length
        sequence = [begin_word]
        level = defaultdict(int)  # Depth level for each word
        level[begin_word] = 0
        while sequence:
            word = sequence.pop(0)
            for pos in range(n):
                for ch in range(26):
                    # Create all possible new combinations
                    new_word = word[:pos] + chr(97+ch) + word[pos+1:]
                    if new_word == word:
                        continue
                    if new_word in words:
                        if new_word not in level:
                            level[new_word] = level[word] + 1
                            sequence.append(new_word)
                            self.adj[word].append(new_word)
                        elif level[new_word] == level[word] + 1:
                            self.adj[word].append(new_word)

    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        words = set(wordList)  # Words are unique
        # Trivial base case
        if endWord not in words:
            return self.ans

        # Create adjacency graph using BFS
        self.bfs(beginWord, words)
        # Find all possible sequences at min-depth using DFS
        sequence = []
        self.dfs(beginWord, endWord, sequence)
        return self.ans


def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert Solution().findLadders(beginWord, endWord, wordList) == \
        [["hit", "hot", "dot", "dog", "cog"],
         ["hit", "hot", "lot", "log", "cog"]]

    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]
    assert Solution().findLadders(beginWord, endWord, wordList) == []


if __name__ == '__main__':
    main()
