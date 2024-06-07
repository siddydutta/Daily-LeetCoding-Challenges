from typing import List


class Node:
    def __init__(self):
        self.children = dict()
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, Node())
        node.is_word = True

    def shortest_prefix(self, word) -> str:
        node = self.root
        prefix = str()
        for ch in word:
            if ch not in node.children:
                return word
            node = node.children[ch]
            prefix += ch
            if node.is_word:
                return prefix
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)

        sentence = sentence.split()
        sentence = map(trie.shortest_prefix, sentence)
        return ' '.join(sentence)


def main():
    dictionary = ['cat', 'bat', 'rat']
    sentence = 'the cattle was rattled by the battery'
    assert Solution().replaceWords(dictionary, sentence) == 'the cat was rat by the bat'  # noqa: E501

    dictionary = ['a', 'b', 'c']
    sentence = 'aadsfasf absbs bbab cadsfafs'
    assert Solution().replaceWords(dictionary, sentence) == 'a a b c'


if __name__ == '__main__':
    main()
