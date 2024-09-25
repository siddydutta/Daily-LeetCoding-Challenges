from typing import List


class Node:
    def __init__(self):
        self.children = dict()
        self.count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, Node())
            node.count += 1

    def get_count(self, word: str) -> int:
        count = 0
        node = self.root
        for ch in word:
            node = node.children[ch]
            count += node.count
        return count


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        return [trie.get_count(word) for word in words]


def main():
    words = ['abc', 'ab', 'bc', 'b']
    assert Solution().sumPrefixScores(words) == [5, 4, 3, 2]

    words = ['abcd']
    assert Solution().sumPrefixScores(words) == [4]


if __name__ == '__main__':
    main()
