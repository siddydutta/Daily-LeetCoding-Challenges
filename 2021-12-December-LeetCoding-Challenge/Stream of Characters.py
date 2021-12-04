# -*- coding: utf-8 -*-
from typing import List


# Node for Trie data structure
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False  # Indicate end of word


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        # Crete trie data structure
        for word in words:
            node = self.root
            for ch in reversed(word):
                # Get next character's node else create new node
                node = node.children.setdefault(ch, TrieNode())
            node.is_word = True
        self.stream = list()  # For query letters

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        # Start from latest character in stream
        node, idx = self.root, len(self.stream)-1
        while node and idx >= 0:
            ch = self.stream[idx]
            node = node.children.get(ch, None)
            if node is not None and node.is_word:
                return True  # Found a word
            idx -= 1
        return False


def main():
    words = ["cd", "f", "kl"]
    streamChecker = StreamChecker(words)
    assert not streamChecker.query("a")
    assert not streamChecker.query("b")
    assert not streamChecker.query("c")
    assert streamChecker.query("d")
    assert not streamChecker.query("e")
    assert streamChecker.query("f")
    assert not streamChecker.query("g")
    assert not streamChecker.query("h")
    assert not streamChecker.query("i")
    assert not streamChecker.query("j")
    assert not streamChecker.query("k")
    assert streamChecker.query("l")


if __name__ == '__main__':
    main()
