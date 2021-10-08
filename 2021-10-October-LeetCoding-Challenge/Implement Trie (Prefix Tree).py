# -*- coding: utf-8 -*-
class Node:
    ''' Node for Trie data structure. '''
    def __init__(self):
        self.children = dict()
        self.is_word = False


class Trie:
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


def main():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")

    trie = Trie()
    assert not trie.startsWith("a")


if __name__ == '__main__':
    main()
