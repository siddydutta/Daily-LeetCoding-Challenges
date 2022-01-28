# -*- coding: utf-8 -*-
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = bool()


class WordDictionary:
    ''' Trie-based solution, using DFS for searching. '''
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            # Either get child or create new Trie node
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True  # Set end of word flag

    def search(self, word):
        def dfs(node: TrieNode, ind: int) -> bool:
            if ind == len(word):
                return node.is_word  # Check end of word flag
            if word[ind] == ".":
                # Iterate over all possible children, as .
                # can be replaced with any child character
                for child in node.children:
                    if dfs(node.children[child], ind+1):
                        return True
            elif word[ind] in node.children:
                # Otherwise continue traversing children
                return dfs(node.children[word[ind]], ind+1)
            return False  # Word not found
        return dfs(self.root, 0)


def main():
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    assert not wordDictionary.search("pad")
    assert wordDictionary.search("bad")
    assert wordDictionary.search(".ad")
    assert wordDictionary.search("b..")


if __name__ == '__main__':
    main()
